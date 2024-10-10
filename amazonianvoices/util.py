from pyclts.ipachart import VowelTrapezoid, PulmonicConsonants
from clld import RESOURCES


def language_detail_html(context=None, request=None, **kw):
    res = {}
    d = VowelTrapezoid()
    covered = d.fill_slots(context.inventory)
    res['vowels_html'], res['vowels_css'] = d.render()
    d = PulmonicConsonants()
    covered = covered.union(d.fill_slots(context.inventory))
    res['consonants_html'], res['consonants_css'] = d.render()
    res['uncovered'] = [p for i, p in enumerate(context.inventory) if i not in covered]
    return res

def dataset_detail_html(context=None, request=None, **kw):
    return dict(
        stats=context.get_stats(
            [rsc for rsc in RESOURCES if rsc.name in ['language', 'parameter', 'value']])
    )
