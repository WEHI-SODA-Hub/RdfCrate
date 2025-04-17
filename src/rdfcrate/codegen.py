"""
Generates URIs for everything in the RO-Crate context
"""

import ast
from dataclasses import dataclass, field
import itertools
from pathlib import Path
from typing import Any, Iterable, cast
import keyword
from rdflib import BNode, Graph, RDFS, RDF, URIRef, OWL
from rdflib.plugins.shared.jsonld.context import Context
from rdflib.query import ResultRow
from rdflib.graph import _TripleType
from rdflib.namespace import Namespace

from rdfcrate.spec_version import all_specs, SpecVersion, ROCrate1_2
from graphlib import TopologicalSorter

#: HTTP URI for schema.org
SDO = Namespace("http://schema.org/")


def frozen_dataclass_decorator() -> ast.expr:
    """
    Returns the frozen dataclass decorator
    """
    return ast.Call(
        func=ast.Name("dataclass"),
        args=[],
        keywords=[ast.keyword(arg="frozen", value=ast.Constant(value=True))],
    )


def find_classes(graph: Graph) -> Iterable[URIRef]:
    """
    Yields all classes that aren't Literals
    """
    # These help us to find subclasses of OWL classes
    graph.add((OWL.Class, RDFS.subClassOf, RDFS.Class))
    for result in graph.query(
        """
        SELECT DISTINCT ?class
        WHERE {
            # Follow any super class relationships
            ?class rdfs:subClassOf* ?superclass .
            ?superclass a rdfs:Class .
            FILTER NOT EXISTS {
                ?class rdfs:subClassOf* ?literal_superclass .
                ?literal_superclass rdfs:subClassOf rdfs:Literal .
            }
            FILTER NOT EXISTS {
                ?class rdfs:subClassOf* ?dt_superclass .
                ?dt_superclass a schema:DataType .
            }
            # We don't care about blank nodes or literals
            FILTER isIRI(?class)
        }
    """,
        initNs={"rdfs": RDFS, "schema": SDO},
    ):
        if isinstance(result, ResultRow) and isinstance(
            cls_id := result["class"], URIRef
        ):
            yield cls_id


def find_enum_values(graph: Graph) -> Iterable[URIRef]:
    """
    Yields all enum instances, such as https://schema.org/Hardcover,
    but not enum classes like https://schema.org/BookFormatType
    """
    for result in graph.query(
        """
        SELECT DISTINCT ?class
        WHERE {
            ?class a* ?type .
            ?type rdfs:subClassOf* schema:Enumeration .
        }
    """,
        initNs={"rdfs": RDFS, "schema": SDO},
    ):
        if isinstance(result, ResultRow) and isinstance(
            cls_id := result["class"], URIRef
        ):
            yield cls_id


def find_datatypes(graph: Graph) -> Iterable[URIRef]:
    """
    Yields all datatypes that aren't classes
    """
    # Schema.org datatypes are should be treated as datatypes, even though they aren't.
    # See https://github.com/schemaorg/schemaorg/issues/4325
    for result in graph.query(
        """
        SELECT DISTINCT ?class
        WHERE {
            {
                ?class rdfs:subClassOf* ?superclass .
                ?superclass a rdfs:Literal .
            }
            UNION 
            {
                ?class rdfs:subClassOf* ?superclass .
                ?superclass a schema:DataType .
            }
        }
    """,
        initNs={"rdfs": RDFS, "schema": SDO},
    ):
        if isinstance(result, ResultRow) and isinstance(
            cls_id := result["class"], URIRef
        ):
            yield cls_id


def find_properties(graph: Graph) -> Iterable[URIRef]:
    """
    Yields all properties that aren't classes
    """
    for result in graph.query(
        """
        SELECT DISTINCT ?property
        WHERE {
            # It's a property if we can find rdf:Property by following rdf:type once and rdfs:subClassOf any number of times
            # Note that finding owl:DatatypeProperty etc will require owl to be in the graph
            ?property a ?type .
            ?type rdfs:subClassOf* rdf:Property .

            # We don't care about blank nodes or literals
            FILTER isIRI(?property)
        }
    """,
        initNs={"rdfs": RDFS, "schema": SDO},
    ):
        if isinstance(result, ResultRow) and isinstance(
            prop_id := result["property"], URIRef
        ):
            yield prop_id
        else:
            raise ValueError("Invalid query response")


@dataclass
class CodegenState:
    context_map: dict[SpecVersion, dict[str, Any]] = field(
        init=False, default_factory=dict
    )
    #: A map of URIs to Python modules in which they are located. This is used for resolving imports "
    module_map: dict[str, str] = field(init=False, default_factory=dict)
    #: List of class definitions. Functions should append to this to define new classes.
    classes: list[ast.ClassDef] = field(init=False)
    #: List of imports, which can be appended to.
    imports: list[str] = field(init=False)
    #: Keeps track of which terms have already been defined. This helps when processing contexts, which duplicate many terms from the vocabs
    terms: set[tuple[str, str]] = field(init=False, default_factory=set)
    #: The cumulative graph of all the vocabularies
    graph: Graph = field(default_factory=Graph)

    def __post_init__(self):
        # This setup is done per-vocabulary
        self.reset()

        # This only needs to be done once, not per vocabulary
        for spec in all_specs:
            self.context_map[spec] = spec.get_context()

    def reset(self):
        """
        Called when a new vocabulary needs to be processed
        """
        # self.graph = Graph()
        self.classes = []
        self.imports = [
            "__future__.annotations",
            "rdflib.term.Identifier",
            "rdfcrate.rdfdatatype.RdfDataType",
            "rdfcrate.rdfclass.RdfClass",
            "rdfcrate.rdfprop.RdfProperty",
            "rdfcrate.rdfterm.RdfTerm",
            "dataclasses.dataclass",
        ]

    def add_import(self, uri: str) -> str:
        """
        Given a URI, looks up the module it's defined in.
        This might e.g. return `rdfcrate.vocabs.schemaorg.CoverArt`.
        Then, we add an import to `rdfcrate.vocabs.schemaorg`.
        Finally, we return `schemaorg.CoverArt` to allow for use in the code
        """
        imp = self.module_map[uri]
        *a, b, c = imp.split(".")

        base = ".".join([*a, b])
        if base not in self.imports:
            self.imports.append(base)
        return f"{b}.{c}"

    def import_stmts(self) -> Iterable[ast.ImportFrom]:
        """
        Yields the source code for all the imports in the current module
        """
        for imp in self.imports:
            module, name = imp.rsplit(".", 1)
            yield ast.ImportFrom(module=module, names=[ast.alias(name)], level=0)

    def property_range(self, prop: URIRef) -> ast.expr:
        """
        Returns the range of a property, as a type annotation
        """
        range_options = []
        for range_ in itertools.chain(
            self.graph.objects(subject=prop, predicate=RDFS.range),
            self.graph.objects(subject=prop, predicate=SDO.rangeIncludes),
        ):
            if isinstance(range_, BNode):
                # Skip blank node ranges
                continue

            _, _, range_name = self.graph.compute_qname(range_)
            if range_ in self.module_map:
                # Import the range type from the other module
                range_options.append(self.add_import(range_))
            elif (range_, RDF.type, RDFS.Class) in self.graph:
                # If the range is a class in the current graph, use it directly
                range_options.append(range_name)

        if len(range_options) == 0:
            # If no range is found, use the default
            return ast.Name("Identifier")
        elif len(range_options) == 1:
            # If one range is found, use it
            return ast.Name(range_options[0])
        else:
            # If multiple ranges are found, use a type union with `|`
            union_expr = ast.BinOp(
                left=ast.Name(range_options[0]),
                op=ast.BitOr(),
                right=ast.Name(range_options[1]),
            )
            for range_name in range_options[2:]:
                union_expr = ast.BinOp(
                    left=union_expr, op=ast.BitOr(), right=ast.Name(range_name)
                )
            return union_expr

    def term_with_specs(self, term: str, uri: str) -> ast.Call:
        """
        Creates the term definition source code for a term. e.g.
        ```python
        RdfTerm('CoverArt', 'http://schema.org/CoverArt', ['0.2', '1.0', '1.1', '1.2-DRAFT'])
        ```
        """
        self.terms.add((term, str(uri)))
        return ast.Call(
            func=ast.Name("RdfTerm"),
            args=[
                ast.Constant(term),
                ast.Constant(str(uri)),
                ast.List(
                    [
                        # Add RO-Crate specs that this term is defined in
                        ast.Constant(spec.version)
                        for spec, ctx in self.context_map.items()
                        if ctx.get(term) == str(uri)
                    ]
                ),
            ],
            keywords=[],
        )

    def visit_enums(self):
        """
        Processes the enums in the graph
        """
        for enum in find_enum_values(self.graph):
            _, _, name = self.graph.compute_qname(enum)
            # Ignore enums for now
            self.terms.add((name, str(enum)))

    def properties_from_rdfs(self, module_base: str) -> None:
        """
        Processes the properties in the graph.
        """
        for prop in find_properties(self.graph):
            if prop in self.module_map:
                # Skip properties that are already defined
                continue

            _, _, name = self.graph.compute_qname(prop)

            # Register this URI as being defined in this module
            self.module_map[prop] = f"{module_base}.{name}"
            self.classes.append(
                ast.ClassDef(
                    name=sanitize_cls_name(name),
                    type_params=[],
                    bases=[
                        # Set T to the range of the property
                        ast.Subscript(
                            value=ast.Name("RdfProperty"),
                            slice=self.property_range(prop),
                        )
                    ],
                    keywords=[],
                    body=[
                        ast.Assign(
                            targets=[ast.Name("term")],
                            value=self.term_with_specs(name, str(prop)),
                            type_comment=None,
                        )
                    ],
                    decorator_list=[],
                )
            )

    def datatypes_from_rdfs(self, module_base: str):
        """
        Processes the datatypes in the graph.
        Each will become a class that inherits from RdfDataType
        """
        for datatype in find_datatypes(self.graph):
            if datatype in self.module_map:
                # Skip datatypes that are already defined
                continue

            _, _, name = self.graph.compute_qname(datatype)
            # Register this URI as being defined in this module
            self.module_map[datatype] = f"{module_base}.{name}"
            self.classes.append(
                ast.ClassDef(
                    name=sanitize_cls_name(name),
                    type_params=[],
                    bases=[ast.Name("RdfDataType")],
                    keywords=[],
                    body=[
                        ast.Assign(
                            targets=[ast.Name("term")],
                            value=self.term_with_specs(name, str(datatype)),
                            type_comment=None,
                        )
                    ],
                    decorator_list=[],
                )
            )

    def _find_superclasses(
        self, cls_uri: URIRef
    ) -> tuple[list[ast.expr], list[URIRef]]:
        """
        Finds all the superclasses of a class

        Returns:
            - names: A list of ast.Name objects that can be used to define a child class
            - uris: A list of URIs for these base classes
        """
        names: list[ast.expr] = []
        uris: list[URIRef] = []
        for superclass_uri in self.graph.objects(
            subject=cls_uri, predicate=RDFS.subClassOf
        ):
            if not isinstance(superclass_uri, URIRef):
                # Skip blank node superclasses
                continue
            _, _, superclass_term = self.graph.compute_qname(superclass_uri)
            superclass_name = sanitize_cls_name(superclass_term)
            if superclass_uri in self.module_map:
                # If we find a previously defined superclass, we need to import it
                names.append(ast.Name(self.add_import(superclass_uri)))
            elif (superclass_uri, RDF.type, RDFS.Class) in self.graph:
                names.append(ast.Name(superclass_name))
                uris.append(superclass_uri)
                # Update dependencies, but only if it's in the current class
                # class_deps[cls_uri].append(superclass_uri)

        if len(names) == 0:
            # If no superclasses are found, use the default
            names = [ast.Name("RdfClass")]
        return names, uris

    def classes_from_rdfs(self, module_base: str) -> None:
        """
        Processes the classes in the graph.
        """
        # Map of class names to their definitions
        classes: dict[str, ast.ClassDef] = {}
        # Map of class names to the parent classes they depend on
        class_deps: dict[str, list[str]] = {}
        for cls_uri in find_classes(self.graph):
            if cls_uri in self.module_map:
                # Skip classes that are already defined
                continue

            # Compute the short term name by removing the base URI
            _, _, term_name = self.graph.compute_qname(cls_uri)
            cls_name = sanitize_cls_name(term_name)

            # Determine the base classes from rdfs:subClassOf
            class_deps[cls_uri] = []
            superclass_names, superclass_uris = self._find_superclasses(cls_uri)
            for superclass_uri in superclass_uris:
                class_deps[cls_uri].append(superclass_uri)

            classes[cls_uri] = ast.ClassDef(
                name=cls_name,
                type_params=[],
                bases=superclass_names,
                keywords=[],
                body=[
                    ast.Assign(
                        targets=[ast.Name("term")],
                        value=self.term_with_specs(term_name, cls_uri),
                        type_comment=None,
                    )
                ],
                decorator_list=[],
            )

        # Sort the classes topologically so that parent classes are defined before child classes
        sorter = TopologicalSorter(class_deps)
        for cls_uri in sorter.static_order():
            cls_def = classes[cls_uri]
            self.classes.append(cls_def)
            # Update the term map only at the end, so that future modules know how to import these classes
            self.module_map[cls_uri] = f"{module_base}.{cls_def.name}"

    def type_module(self) -> ast.Module:
        """
        Creates a module that lists all the classes and properties in the graph
        """
        return ast.fix_missing_locations(
            ast.Module([*self.import_stmts(), *self.classes], type_ignores=[])
        )

    def parse_context(self, context: Context) -> None:
        """
        Creates class definitions from a JSON-LD context
        """
        for term, uri in context.to_dict().items():
            # Workaround for invalid Python identifiers
            field_name = term
            # uri = context.expand(uri)
            if (not field_name.isidentifier()) or keyword.iskeyword(field_name):
                field_name = "_" + field_name.replace("-", "_")

            # Need to fix this separately in the context
            uri = uri.replace("https://schema.org/", "http://schema.org/")

            if (term, uri) in self.terms:
                # Skip terms that are already defined
                continue

            if uri.endswith("#") or uri.endswith("/"):
                # Assume these are prefixes
                continue

            if term[0].isupper():
                # Assume it's a class if the first letter is uppercase
                superclass_names, superclass_uris = self._find_superclasses(URIRef(uri))
                self.classes.append(
                    ast.ClassDef(
                        name=sanitize_cls_name(term),
                        type_params=[],
                        bases=superclass_names,
                        keywords=[],
                        body=[
                            ast.Assign(
                                targets=[ast.Name("term")],
                                value=self.term_with_specs(term, str(uri)),
                                type_comment=None,
                            )
                        ],
                        decorator_list=[],
                    )
                )
            else:
                self.classes.append(
                    ast.ClassDef(
                        name=sanitize_cls_name(term),
                        type_params=[],
                        bases=[ast.Name("RdfProperty")],
                        keywords=[],
                        body=[
                            ast.Assign(
                                targets=[ast.Name("term")],
                                value=self.term_with_specs(term, str(uri)),
                                type_comment=None,
                            ),
                            ast.AnnAssign(
                                target=ast.Name("object"),
                                annotation=self.property_range(URIRef(uri)),
                                value=None,
                                simple=1,
                            ),
                        ],
                        decorator_list=[frozen_dataclass_decorator()],
                    )
                )


def camel_to_snake(camel: str) -> str:
    """
    Converts a camel case string to snake case
    """
    segments = []
    start = 0
    i = 0
    for i, letter in enumerate(camel):
        if letter.isupper():
            segments.append(camel[start:i].lower())
            start = i

    segments.append(camel[start:].lower())
    return "_".join(segments)


def sanitize_cls_name(name: str) -> str:
    """
    Sanitizes a class name to be a valid Python identifier
    """
    name = name.replace("-", "_")
    if not name.isidentifier() or keyword.iskeyword(name):
        return f"_{name}"
    return name


def schema_org_https(graph: Graph):
    """
    Rewrites the schema.org URIs in the graph to use http instead of https.
    This is recommended by the RO-Crate context.
    """
    for triple in graph:
        new_triple = tuple(
            [
                URIRef(uri.replace("https://schema.org/", "http://schema.org/"))
                if isinstance(uri, URIRef)
                else uri
                for uri in triple
            ]
        )
        if triple != new_triple:
            graph.remove(triple)
            graph.add(cast(_TripleType, new_triple))


def generate_modules(
    vocabs: dict[str, str],
    contexts: dict[str, dict[str, str]],
    base_module: str,
    out_dir: Path,
):
    """
    Generates a module in the given directory for each vocabulary

    Params:
        vocabs: A dictionary of vocabulary names to URIs RDFS URIs. This should be ordered such that dependencies like schema.org come first.
        out_dir: The output directory
    """
    state = CodegenState()
    for vocab, uri in vocabs.items():
        state.reset()
        state.graph.parse(uri)
        schema_org_https(state.graph)
        module_base = f"{base_module}.{vocab}"
        state.datatypes_from_rdfs(module_base)
        state.classes_from_rdfs(module_base)
        state.properties_from_rdfs(module_base)
        state.visit_enums()
        module = state.type_module()
        out_path = out_dir / f"{vocab}.py"
        out_path.write_text(ast.unparse(module))
    for name, context in contexts.items():
        state.reset()
        state.parse_context(Context(context))
        module = state.type_module()
        out_path = out_dir / f"{name}.py"
        out_path.write_text(ast.unparse(module))


def core_vocab():
    generate_modules(
        {
            "rdfs": "https://www.w3.org/2000/01/rdf-schema",
            "rdf": "https://www.w3.org/1999/02/22-rdf-syntax-ns",
            "owl": "https://www.w3.org/2002/07/owl",
            "dc": "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl",
            "pcdm": "https://pcdm.org/models.rdf",
            "prov": "https://www.w3.org/ns/prov.ttl",
            "pav": "http://purl.org/pav",
            "prof": "https://www.w3.org/TR/dx-prof/rdf/prof.ttl",
            "geo": "https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl",
            "schemaorg": "https://schema.org/version/latest/schemaorg-all-http.jsonld",
            "bioschemas": "https://bioschemas.org/types/bioschemas_types.jsonld",
            "bioschemas_drafts": "https://bioschemas.org/types/bioschemas_draft_types.jsonld",
        },
        {"rocrate": ROCrate1_2.get_context()},
        "rdfcrate.vocabs",
        Path("src/rdfcrate/vocabs"),
    )


if __name__ == "__main__":
    core_vocab()
