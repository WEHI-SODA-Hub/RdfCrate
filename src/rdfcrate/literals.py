"""
Literal subclasses for specific data types.
These behave identically at runtime, but allow static typing
"""

from rdflib import Literal, XSD


class IntLiteral(Literal):
    def __new__(
        cls,
        lexical_or_value: int,
    ):
        return super().__new__(
            cls, lexical_or_value=lexical_or_value, datatype=XSD.integer
        )


class FloatLiteral(Literal):
    def __new__(
        cls,
        lexical_or_value: float,
    ):
        return super().__new__(
            cls, lexical_or_value=lexical_or_value, datatype=XSD.float
        )


class BoolLiteral(Literal):
    def __new__(
        cls,
        lexical_or_value: bool,
    ):
        return super().__new__(
            cls, lexical_or_value=lexical_or_value, datatype=XSD.boolean
        )


class StringLiteral(Literal):
    def __new__(
        cls,
        lexical_or_value: str,
    ):
        return super().__new__(
            cls, lexical_or_value=lexical_or_value, datatype=XSD.string
        )
