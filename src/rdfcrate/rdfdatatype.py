from typing import Any, ClassVar, cast
from typing_extensions import Self
from rdflib.term import Literal

from rdfcrate.rdfterm import RdfTerm


class RdfDataType(Literal):
    """
    Broadly represents an rdfs:Literal or any of its subclasses: https://www.w3.org/TR/rdf-schema/#ch_literal.
    ie a value and not an ID.
    """

    def __new__(
        cls,
        lexical_or_value: Any,
        lang: str | None = None,
        datatype: str | None = None,
        normalize: bool | None = None,
    ) -> Self:
        # This is just a workaround to https://github.com/RDFLib/rdflib/issues/3107
        return cast(
            Self, super().__new__(cls, lexical_or_value, lang, datatype, normalize)
        )

    term: ClassVar[RdfTerm]
