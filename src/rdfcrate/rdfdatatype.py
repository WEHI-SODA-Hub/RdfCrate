from typing import Any, ClassVar, Self, cast
from rdflib.term import Literal

from rdfcrate.rdfterm import RdfTerm

class RdfDataType(Literal):
    def __new__(
        cls,
        lexical_or_value: Any,
        lang: str | None = None,
        datatype: str | None = None,
        normalize: bool | None = None,
    ) -> Self:
        # This is just a workaround to https://github.com/RDFLib/rdflib/issues/3107
        return cast(Self, super().__new__(cls, lexical_or_value, lang, datatype, normalize))

    term: ClassVar[RdfTerm]
