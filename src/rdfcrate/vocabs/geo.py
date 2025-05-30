from __future__ import annotations
from rdflib.term import Identifier
from rdfcrate.rdftype import RdfClass
from rdfcrate.rdfprop import RdfProperty
from rdfcrate.rdfterm import RdfTerm
from rdfcrate.vocabs import rdfs
from rdfcrate.vocabs import geo
from rdfcrate.rdftype import RdfType

class SpatialObjectCollection(rdfs.Container):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#SpatialObjectCollection', 'SpatialObjectCollection')

class SpatialObject(RdfClass):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#SpatialObject', 'SpatialObject')

class FeatureCollection(SpatialObjectCollection):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#FeatureCollection', 'FeatureCollection')

class GeometryCollection(SpatialObjectCollection):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#GeometryCollection', 'GeometryCollection')

class Feature(SpatialObject):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#Feature', 'Feature')

class Geometry(SpatialObject):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#Geometry', 'Geometry')

class defaultGeometry(RdfProperty[geo.Geometry]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#defaultGeometry', 'defaultGeometry')

class hasDefaultGeometry(RdfProperty[geo.Geometry]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasDefaultGeometry', 'hasDefaultGeometry')

class ehContains(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehContains', 'ehContains')

class ehCoveredBy(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehCoveredBy', 'ehCoveredBy')

class ehCovers(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehCovers', 'ehCovers')

class ehDisjoint(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehDisjoint', 'ehDisjoint')

class ehEquals(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehEquals', 'ehEquals')

class ehInside(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehInside', 'ehInside')

class ehMeet(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehMeet', 'ehMeet')

class ehOverlap(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#ehOverlap', 'ehOverlap')

class hasGeometry(RdfProperty[geo.Geometry]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasGeometry', 'hasGeometry')

class hasBoundingBox(RdfProperty[geo.Geometry]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasBoundingBox', 'hasBoundingBox')

class hasCentroid(RdfProperty[geo.Geometry]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasCentroid', 'hasCentroid')

class hasLength(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasLength', 'hasLength')

class hasPerimeterLength(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasPerimeterLength', 'hasPerimeterLength')

class hasArea(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasArea', 'hasArea')

class hasVolume(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasVolume', 'hasVolume')

class hasSpatialResolution(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasSpatialResolution', 'hasSpatialResolution')

class hasSpatialAccuracy(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasSpatialAccuracy', 'hasSpatialAccuracy')

class rcc8dc(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8dc', 'rcc8dc')

class rcc8ec(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8ec', 'rcc8ec')

class rcc8eq(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8eq', 'rcc8eq')

class rcc8ntpp(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8ntpp', 'rcc8ntpp')

class rcc8ntppi(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8ntppi', 'rcc8ntppi')

class rcc8po(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8po', 'rcc8po')

class rcc8tpp(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8tpp', 'rcc8tpp')

class rcc8tppi(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#rcc8tppi', 'rcc8tppi')

class sfContains(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfContains', 'sfContains')

class sfCrosses(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfCrosses', 'sfCrosses')

class sfDisjoint(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfDisjoint', 'sfDisjoint')

class sfEquals(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfEquals', 'sfEquals')

class sfIntersects(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfIntersects', 'sfIntersects')

class sfOverlaps(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfOverlaps', 'sfOverlaps')

class sfTouches(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfTouches', 'sfTouches')

class sfWithin(RdfProperty[geo.SpatialObject]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#sfWithin', 'sfWithin')

class hasSize(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasSize', 'hasSize')

class asGML(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#asGML', 'asGML')

class asWKT(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#asWKT', 'asWKT')

class asGeoJSON(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#asGeoJSON', 'asGeoJSON')

class asKML(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#asKML', 'asKML')

class asDGGS(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#asDGGS', 'asDGGS')

class coordinateDimension(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#coordinateDimension', 'coordinateDimension')

class dimension(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#dimension', 'dimension')

class hasSerialization(RdfProperty[rdfs.Literal]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasSerialization', 'hasSerialization')

class isEmpty(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#isEmpty', 'isEmpty')

class isSimple(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#isSimple', 'isSimple')

class spatialDimension(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#spatialDimension', 'spatialDimension')

class hasMetricSpatialResolution(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricSpatialResolution', 'hasMetricSpatialResolution')

class hasMetricSpatialAccuracy(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricSpatialAccuracy', 'hasMetricSpatialAccuracy')

class hasMetricLength(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricLength', 'hasMetricLength')

class hasMetricPerimeterLength(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricPerimeterLength', 'hasMetricPerimeterLength')

class hasMetricArea(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricArea', 'hasMetricArea')

class hasMetricVolume(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricVolume', 'hasMetricVolume')

class hasMetricSize(RdfProperty[RdfType]):
    term = RdfTerm('http://www.opengis.net/ont/geosparql#hasMetricSize', 'hasMetricSize')