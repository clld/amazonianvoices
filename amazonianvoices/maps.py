from clld.db.meta import DBSession
from clld.db.models import common
from clld.web.maps import Map, ParameterMap, Layer
from clld.web.util.helpers import JS


class LanguagesMap(Map):
    def get_options(self):
        return {
            'max_zoom': 17,
            'show_labels': False,
        }

    def get_layers(self):
        yield from Map.get_layers(self)
        yield Layer(
            'polys',
            'polys',
            dict(
                type='FeatureCollection',
                features=[l.jsondata['area'] for l in DBSession.query(common.Language)]))


class ConceptMap(ParameterMap):
    def get_options(self):
        return {
            'on_init': JS('AMAZONIANVOICES.map_with_taxa_on_init'),
            'with_audioplayer': True,
            'max_zoom': 17,
            'show_labels': False,
        }


def includeme(config):
    config.register_map('languages', LanguagesMap)
    config.register_map('parameter', ConceptMap)
