import json

from clld import RESOURCES

assert json



def language_detail_html(context=None, request=None, **kw):
    return context.render_inventory(request=request)


def dataset_detail_html(context=None, request=None, **kw):
    return dict(
        stats=context.get_stats(
            [rsc for rsc in RESOURCES if rsc.name in ['language', 'parameter', 'value']])
    )
