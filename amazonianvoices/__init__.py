from pyramid.config import Configurator
from clld.web.icon import MapMarker
from clld.interfaces import IMapMarker, IValueSet, IValue, ILanguage
from clldutils.svg import icon, data_url


# we must make sure custom models are known at database initialization!
from amazonianvoices import models
from clld_audio_plugin import models as audiomodels

_ = lambda s: s
_('Languages')
_('Parameters')
_('Language')
_('Parameter')
_('Values')
_('Value')
_('Contributors')
_('Download')
_('Contact')
_('Credits')
_('Legal')
_('Home')
_('You can contact us via email at')
_('Latitude')
_('Longitude')
_('Map')
_('Alternative names')

# Maps
_('Icon size')
_('Show/hide Labels')

# DataTables
_("Next")
_("Previous")
_("First")
_("Last")
_("No data available in table")
_("Showing _START_ to _END_ of _TOTAL_ entries")
_("Showing 0 to 0 of 0 entries")
_("(filtered from _MAX_ total entries)")
_("Show _MENU_ entries")
_("Loading...")
_("Processing...")
_("Search:")
_("Search")
_("No matching records found")



class LanguageByFamilyMapMarker(MapMarker):
    def __call__(self, ctx, req):
        if IValue.providedBy(ctx):
            return data_url(icon('c' + ctx.valueset.language.jsondata['color']))
        if IValueSet.providedBy(ctx):
            return data_url(icon('c' + ctx.language.jsondata['color']))
        elif ILanguage.providedBy(ctx):
            return data_url(icon('c' + ctx.jsondata['color']))

        return super(LanguageByFamilyMapMarker, self).__call__(ctx, req)  # pragma: no cover


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('clld.web.app')

    config.include('clldmpg')
    config.include('clld_audio_plugin')
    config.registry.registerUtility(LanguageByFamilyMapMarker(), IMapMarker)
    config.register_map('parameter', maps.ConceptMap)
    return config.make_wsgi_app()
