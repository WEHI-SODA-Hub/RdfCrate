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


class defaultGeometry(RdfProperty[geo.Geometry]):
    term = RdfTerm(
        "defaultGeometry", "http://www.opengis.net/ont/geosparql#defaultGeometry", []
    )


class hasDefaultGeometry(RdfProperty[geo.Geometry]):
    term = RdfTerm(
        "hasDefaultGeometry",
        "http://www.opengis.net/ont/geosparql#hasDefaultGeometry",
        [],
    )


class ehContains(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehContains", "http://www.opengis.net/ont/geosparql#ehContains", [])


class ehCoveredBy(RdfProperty[geo.SpatialObject]):
    term = RdfTerm(
        "ehCoveredBy", "http://www.opengis.net/ont/geosparql#ehCoveredBy", []
    )


class ehCovers(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehCovers", "http://www.opengis.net/ont/geosparql#ehCovers", [])


class ehDisjoint(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehDisjoint", "http://www.opengis.net/ont/geosparql#ehDisjoint", [])


class ehEquals(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehEquals", "http://www.opengis.net/ont/geosparql#ehEquals", [])


class ehInside(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehInside", "http://www.opengis.net/ont/geosparql#ehInside", [])


class ehMeet(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehMeet", "http://www.opengis.net/ont/geosparql#ehMeet", [])


class ehOverlap(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("ehOverlap", "http://www.opengis.net/ont/geosparql#ehOverlap", [])


class hasGeometry(RdfProperty[geo.Geometry]):
    term = RdfTerm(
        "hasGeometry", "http://www.opengis.net/ont/geosparql#hasGeometry", []
    )


class hasBoundingBox(RdfProperty[geo.Geometry]):
    term = RdfTerm(
        "hasBoundingBox", "http://www.opengis.net/ont/geosparql#hasBoundingBox", []
    )


class hasCentroid(RdfProperty[geo.Geometry]):
    term = RdfTerm(
        "hasCentroid", "http://www.opengis.net/ont/geosparql#hasCentroid", []
    )


class hasLength(RdfProperty[Identifier]):
    term = RdfTerm("hasLength", "http://www.opengis.net/ont/geosparql#hasLength", [])


class hasPerimeterLength(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasPerimeterLength",
        "http://www.opengis.net/ont/geosparql#hasPerimeterLength",
        [],
    )


class hasArea(RdfProperty[Identifier]):
    term = RdfTerm("hasArea", "http://www.opengis.net/ont/geosparql#hasArea", [])


class hasVolume(RdfProperty[Identifier]):
    term = RdfTerm("hasVolume", "http://www.opengis.net/ont/geosparql#hasVolume", [])


class hasSpatialResolution(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasSpatialResolution",
        "http://www.opengis.net/ont/geosparql#hasSpatialResolution",
        [],
    )


class hasSpatialAccuracy(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasSpatialAccuracy",
        "http://www.opengis.net/ont/geosparql#hasSpatialAccuracy",
        [],
    )


class rcc8dc(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8dc", "http://www.opengis.net/ont/geosparql#rcc8dc", [])


class rcc8ec(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8ec", "http://www.opengis.net/ont/geosparql#rcc8ec", [])


class rcc8eq(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8eq", "http://www.opengis.net/ont/geosparql#rcc8eq", [])


class rcc8ntpp(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8ntpp", "http://www.opengis.net/ont/geosparql#rcc8ntpp", [])


class rcc8ntppi(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8ntppi", "http://www.opengis.net/ont/geosparql#rcc8ntppi", [])


class rcc8po(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8po", "http://www.opengis.net/ont/geosparql#rcc8po", [])


class rcc8tpp(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8tpp", "http://www.opengis.net/ont/geosparql#rcc8tpp", [])


class rcc8tppi(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("rcc8tppi", "http://www.opengis.net/ont/geosparql#rcc8tppi", [])


class sfContains(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfContains", "http://www.opengis.net/ont/geosparql#sfContains", [])


class sfCrosses(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfCrosses", "http://www.opengis.net/ont/geosparql#sfCrosses", [])


class sfDisjoint(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfDisjoint", "http://www.opengis.net/ont/geosparql#sfDisjoint", [])


class sfEquals(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfEquals", "http://www.opengis.net/ont/geosparql#sfEquals", [])


class sfIntersects(RdfProperty[geo.SpatialObject]):
    term = RdfTerm(
        "sfIntersects", "http://www.opengis.net/ont/geosparql#sfIntersects", []
    )


class sfOverlaps(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfOverlaps", "http://www.opengis.net/ont/geosparql#sfOverlaps", [])


class sfTouches(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfTouches", "http://www.opengis.net/ont/geosparql#sfTouches", [])


class sfWithin(RdfProperty[geo.SpatialObject]):
    term = RdfTerm("sfWithin", "http://www.opengis.net/ont/geosparql#sfWithin", [])


class hasSize(RdfProperty[Identifier]):
    term = RdfTerm("hasSize", "http://www.opengis.net/ont/geosparql#hasSize", [])


class asGML(RdfProperty[Identifier]):
    term = RdfTerm("asGML", "http://www.opengis.net/ont/geosparql#asGML", [])


class asWKT(RdfProperty[Identifier]):
    term = RdfTerm("asWKT", "http://www.opengis.net/ont/geosparql#asWKT", ["1.2-DRAFT"])


class asGeoJSON(RdfProperty[Identifier]):
    term = RdfTerm("asGeoJSON", "http://www.opengis.net/ont/geosparql#asGeoJSON", [])


class asKML(RdfProperty[Identifier]):
    term = RdfTerm("asKML", "http://www.opengis.net/ont/geosparql#asKML", [])


class asDGGS(RdfProperty[Identifier]):
    term = RdfTerm("asDGGS", "http://www.opengis.net/ont/geosparql#asDGGS", [])


class coordinateDimension(RdfProperty[Identifier]):
    term = RdfTerm(
        "coordinateDimension",
        "http://www.opengis.net/ont/geosparql#coordinateDimension",
        [],
    )


class dimension(RdfProperty[Identifier]):
    term = RdfTerm("dimension", "http://www.opengis.net/ont/geosparql#dimension", [])


class hasSerialization(RdfProperty[rdfs.Literal]):
    term = RdfTerm(
        "hasSerialization", "http://www.opengis.net/ont/geosparql#hasSerialization", []
    )


class isEmpty(RdfProperty[Identifier]):
    term = RdfTerm("isEmpty", "http://www.opengis.net/ont/geosparql#isEmpty", [])


class isSimple(RdfProperty[Identifier]):
    term = RdfTerm("isSimple", "http://www.opengis.net/ont/geosparql#isSimple", [])


class spatialDimension(RdfProperty[Identifier]):
    term = RdfTerm(
        "spatialDimension", "http://www.opengis.net/ont/geosparql#spatialDimension", []
    )


class hasMetricSpatialResolution(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricSpatialResolution",
        "http://www.opengis.net/ont/geosparql#hasMetricSpatialResolution",
        [],
    )


class hasMetricSpatialAccuracy(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricSpatialAccuracy",
        "http://www.opengis.net/ont/geosparql#hasMetricSpatialAccuracy",
        [],
    )


class hasMetricLength(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricLength", "http://www.opengis.net/ont/geosparql#hasMetricLength", []
    )


class hasMetricPerimeterLength(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricPerimeterLength",
        "http://www.opengis.net/ont/geosparql#hasMetricPerimeterLength",
        [],
    )


class hasMetricArea(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricArea", "http://www.opengis.net/ont/geosparql#hasMetricArea", []
    )


class hasMetricVolume(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricVolume", "http://www.opengis.net/ont/geosparql#hasMetricVolume", []
    )


class hasMetricSize(RdfProperty[Identifier]):
    term = RdfTerm(
        "hasMetricSize", "http://www.opengis.net/ont/geosparql#hasMetricSize", []
    )
