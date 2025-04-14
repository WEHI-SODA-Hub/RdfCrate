from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdfdatatype import RdfDataType
from rdfcrate.rdfclass import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from dataclasses import dataclass
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import geo


class SpatialObjectCollection(rdfs.Container):
    term = RdfTerm(
        "SpatialObjectCollection",
        "http://www.opengis.net/ont/geosparql#SpatialObjectCollection",
        [],
    )


class SpatialObject(RdfClass):
    term = RdfTerm(
        "SpatialObject", "http://www.opengis.net/ont/geosparql#SpatialObject", []
    )


class FeatureCollection(SpatialObjectCollection):
    term = RdfTerm(
        "FeatureCollection",
        "http://www.opengis.net/ont/geosparql#FeatureCollection",
        [],
    )


class GeometryCollection(SpatialObjectCollection):
    term = RdfTerm(
        "GeometryCollection",
        "http://www.opengis.net/ont/geosparql#GeometryCollection",
        [],
    )


class Feature(SpatialObject):
    term = RdfTerm("Feature", "http://www.opengis.net/ont/geosparql#Feature", [])


class Geometry(SpatialObject):
    term = RdfTerm(
        "Geometry", "http://www.opengis.net/ont/geosparql#Geometry", ["1.2-DRAFT"]
    )


@dataclass(frozen=True)
class defaultGeometry(RdfProperty):
    term = RdfTerm(
        "defaultGeometry", "http://www.opengis.net/ont/geosparql#defaultGeometry", []
    )
    object: geo.Geometry


@dataclass(frozen=True)
class hasDefaultGeometry(RdfProperty):
    term = RdfTerm(
        "hasDefaultGeometry",
        "http://www.opengis.net/ont/geosparql#hasDefaultGeometry",
        [],
    )
    object: geo.Geometry


@dataclass(frozen=True)
class ehContains(RdfProperty):
    term = RdfTerm("ehContains", "http://www.opengis.net/ont/geosparql#ehContains", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehCoveredBy(RdfProperty):
    term = RdfTerm(
        "ehCoveredBy", "http://www.opengis.net/ont/geosparql#ehCoveredBy", []
    )
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehCovers(RdfProperty):
    term = RdfTerm("ehCovers", "http://www.opengis.net/ont/geosparql#ehCovers", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehDisjoint(RdfProperty):
    term = RdfTerm("ehDisjoint", "http://www.opengis.net/ont/geosparql#ehDisjoint", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehEquals(RdfProperty):
    term = RdfTerm("ehEquals", "http://www.opengis.net/ont/geosparql#ehEquals", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehInside(RdfProperty):
    term = RdfTerm("ehInside", "http://www.opengis.net/ont/geosparql#ehInside", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehMeet(RdfProperty):
    term = RdfTerm("ehMeet", "http://www.opengis.net/ont/geosparql#ehMeet", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class ehOverlap(RdfProperty):
    term = RdfTerm("ehOverlap", "http://www.opengis.net/ont/geosparql#ehOverlap", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class hasGeometry(RdfProperty):
    term = RdfTerm(
        "hasGeometry", "http://www.opengis.net/ont/geosparql#hasGeometry", []
    )
    object: geo.Geometry


@dataclass(frozen=True)
class hasBoundingBox(RdfProperty):
    term = RdfTerm(
        "hasBoundingBox", "http://www.opengis.net/ont/geosparql#hasBoundingBox", []
    )
    object: geo.Geometry


@dataclass(frozen=True)
class hasCentroid(RdfProperty):
    term = RdfTerm(
        "hasCentroid", "http://www.opengis.net/ont/geosparql#hasCentroid", []
    )
    object: geo.Geometry


@dataclass(frozen=True)
class hasLength(RdfProperty):
    term = RdfTerm("hasLength", "http://www.opengis.net/ont/geosparql#hasLength", [])
    object: Identifier


@dataclass(frozen=True)
class hasPerimeterLength(RdfProperty):
    term = RdfTerm(
        "hasPerimeterLength",
        "http://www.opengis.net/ont/geosparql#hasPerimeterLength",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class hasArea(RdfProperty):
    term = RdfTerm("hasArea", "http://www.opengis.net/ont/geosparql#hasArea", [])
    object: Identifier


@dataclass(frozen=True)
class hasVolume(RdfProperty):
    term = RdfTerm("hasVolume", "http://www.opengis.net/ont/geosparql#hasVolume", [])
    object: Identifier


@dataclass(frozen=True)
class hasSpatialResolution(RdfProperty):
    term = RdfTerm(
        "hasSpatialResolution",
        "http://www.opengis.net/ont/geosparql#hasSpatialResolution",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class hasSpatialAccuracy(RdfProperty):
    term = RdfTerm(
        "hasSpatialAccuracy",
        "http://www.opengis.net/ont/geosparql#hasSpatialAccuracy",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class rcc8dc(RdfProperty):
    term = RdfTerm("rcc8dc", "http://www.opengis.net/ont/geosparql#rcc8dc", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8ec(RdfProperty):
    term = RdfTerm("rcc8ec", "http://www.opengis.net/ont/geosparql#rcc8ec", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8eq(RdfProperty):
    term = RdfTerm("rcc8eq", "http://www.opengis.net/ont/geosparql#rcc8eq", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8ntpp(RdfProperty):
    term = RdfTerm("rcc8ntpp", "http://www.opengis.net/ont/geosparql#rcc8ntpp", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8ntppi(RdfProperty):
    term = RdfTerm("rcc8ntppi", "http://www.opengis.net/ont/geosparql#rcc8ntppi", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8po(RdfProperty):
    term = RdfTerm("rcc8po", "http://www.opengis.net/ont/geosparql#rcc8po", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8tpp(RdfProperty):
    term = RdfTerm("rcc8tpp", "http://www.opengis.net/ont/geosparql#rcc8tpp", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class rcc8tppi(RdfProperty):
    term = RdfTerm("rcc8tppi", "http://www.opengis.net/ont/geosparql#rcc8tppi", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfContains(RdfProperty):
    term = RdfTerm("sfContains", "http://www.opengis.net/ont/geosparql#sfContains", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfCrosses(RdfProperty):
    term = RdfTerm("sfCrosses", "http://www.opengis.net/ont/geosparql#sfCrosses", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfDisjoint(RdfProperty):
    term = RdfTerm("sfDisjoint", "http://www.opengis.net/ont/geosparql#sfDisjoint", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfEquals(RdfProperty):
    term = RdfTerm("sfEquals", "http://www.opengis.net/ont/geosparql#sfEquals", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfIntersects(RdfProperty):
    term = RdfTerm(
        "sfIntersects", "http://www.opengis.net/ont/geosparql#sfIntersects", []
    )
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfOverlaps(RdfProperty):
    term = RdfTerm("sfOverlaps", "http://www.opengis.net/ont/geosparql#sfOverlaps", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfTouches(RdfProperty):
    term = RdfTerm("sfTouches", "http://www.opengis.net/ont/geosparql#sfTouches", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class sfWithin(RdfProperty):
    term = RdfTerm("sfWithin", "http://www.opengis.net/ont/geosparql#sfWithin", [])
    object: geo.SpatialObject


@dataclass(frozen=True)
class hasSize(RdfProperty):
    term = RdfTerm("hasSize", "http://www.opengis.net/ont/geosparql#hasSize", [])
    object: Identifier


@dataclass(frozen=True)
class asGML(RdfProperty):
    term = RdfTerm("asGML", "http://www.opengis.net/ont/geosparql#asGML", [])
    object: Identifier


@dataclass(frozen=True)
class asWKT(RdfProperty):
    term = RdfTerm("asWKT", "http://www.opengis.net/ont/geosparql#asWKT", ["1.2-DRAFT"])
    object: Identifier


@dataclass(frozen=True)
class asGeoJSON(RdfProperty):
    term = RdfTerm("asGeoJSON", "http://www.opengis.net/ont/geosparql#asGeoJSON", [])
    object: Identifier


@dataclass(frozen=True)
class asKML(RdfProperty):
    term = RdfTerm("asKML", "http://www.opengis.net/ont/geosparql#asKML", [])
    object: Identifier


@dataclass(frozen=True)
class asDGGS(RdfProperty):
    term = RdfTerm("asDGGS", "http://www.opengis.net/ont/geosparql#asDGGS", [])
    object: Identifier


@dataclass(frozen=True)
class coordinateDimension(RdfProperty):
    term = RdfTerm(
        "coordinateDimension",
        "http://www.opengis.net/ont/geosparql#coordinateDimension",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class dimension(RdfProperty):
    term = RdfTerm("dimension", "http://www.opengis.net/ont/geosparql#dimension", [])
    object: Identifier


@dataclass(frozen=True)
class hasSerialization(RdfProperty):
    term = RdfTerm(
        "hasSerialization", "http://www.opengis.net/ont/geosparql#hasSerialization", []
    )
    object: rdfs.Literal


@dataclass(frozen=True)
class isEmpty(RdfProperty):
    term = RdfTerm("isEmpty", "http://www.opengis.net/ont/geosparql#isEmpty", [])
    object: Identifier


@dataclass(frozen=True)
class isSimple(RdfProperty):
    term = RdfTerm("isSimple", "http://www.opengis.net/ont/geosparql#isSimple", [])
    object: Identifier


@dataclass(frozen=True)
class spatialDimension(RdfProperty):
    term = RdfTerm(
        "spatialDimension", "http://www.opengis.net/ont/geosparql#spatialDimension", []
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricSpatialResolution(RdfProperty):
    term = RdfTerm(
        "hasMetricSpatialResolution",
        "http://www.opengis.net/ont/geosparql#hasMetricSpatialResolution",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricSpatialAccuracy(RdfProperty):
    term = RdfTerm(
        "hasMetricSpatialAccuracy",
        "http://www.opengis.net/ont/geosparql#hasMetricSpatialAccuracy",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricLength(RdfProperty):
    term = RdfTerm(
        "hasMetricLength", "http://www.opengis.net/ont/geosparql#hasMetricLength", []
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricPerimeterLength(RdfProperty):
    term = RdfTerm(
        "hasMetricPerimeterLength",
        "http://www.opengis.net/ont/geosparql#hasMetricPerimeterLength",
        [],
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricArea(RdfProperty):
    term = RdfTerm(
        "hasMetricArea", "http://www.opengis.net/ont/geosparql#hasMetricArea", []
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricVolume(RdfProperty):
    term = RdfTerm(
        "hasMetricVolume", "http://www.opengis.net/ont/geosparql#hasMetricVolume", []
    )
    object: Identifier


@dataclass(frozen=True)
class hasMetricSize(RdfProperty):
    term = RdfTerm(
        "hasMetricSize", "http://www.opengis.net/ont/geosparql#hasMetricSize", []
    )
    object: Identifier
