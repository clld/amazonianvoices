import pathlib
import collections

from pycldf import Sources, Wordlist
from clldutils.color import qualitative_colors
from clldutils.misc import nfilter
from clldutils.misc import slug
from clldutils import licenses
from clld.cliutil import Data, bibtex2source
from clld.db.meta import DBSession
from clld.db.models import common
from clld.lib import bibtex
from nameparser import HumanName
from cldfbench import get_dataset
from clld_audio_plugin.models import Counterpart
from clld_audio_plugin import util as audioutil
from pyclts import CLTS
from sqlalchemy import func
from sqlalchemy.orm import joinedload

import amazonianvoices
from amazonianvoices import models


def main(args):  # pragma: no cover
    license = licenses.find(args.cldf.properties['dc:license'])
    assert license and license.id.startswith('CC-')

    clts = CLTS(input('Path to cldf-clts/clts:') or '../../cldf-clts/clts-data')

    data = Data()
    ds = data.add(
        common.Dataset,
        amazonianvoices.__name__,
        id=amazonianvoices.__name__,
        name='Amazonian Voices',
        domain='amazonianvoices.clld.org',
        contact="dlce.rdm@eva.mpg.de",
        publisher_name="Max Planck Institute for Evolutionary Anthropology",
        publisher_place="Leipzig",
        publisher_url="https://www.eva.mpg.de",
        license=license.url,
        jsondata={
            'license_icon': '{}.png'.format(
                '-'.join([p.lower() for p in license.id.split('-')[:-1]])),
            'license_name': license.name},

    )
    form2audio = audioutil.form2audio(args.cldf, 'audio/mpeg')

    r = get_dataset('amazonianvoices', ep='lexibank.dataset')
    authors, _ = r.get_creators_and_contributors()
    for ord, author in enumerate(authors):
        cid = slug(HumanName(author['name']).last)
        c = data.add(
            common.Contributor,
            cid,
            id=cid,
            name=author['name'],
            description=author.get('description'),
        )

    for ord, cid in enumerate(['vasquez', 'zariquiey', 'bibiko', 'gray']):
        DBSession.add(common.Editor(
            ord=ord,
            dataset=ds,
            contributor=data['Contributor'][cid]))

    contribs = collections.defaultdict(lambda: collections.defaultdict(list))

    for lang in args.cldf.iter_rows('LanguageTable', 'id', 'glottocode', 'name', 'latitude', 'longitude', 'Family'):
        contrib = data.add(
            common.Contribution,
            lang['id'],
            id=lang['id'],
            name='Wordlist for {}'.format(lang['name']),
        )
        data.add(
            models.Variety,
            lang['id'],
            id=lang['id'],
            name=lang['name'],
            latitude=lang['latitude'],
            longitude=lang['longitude'],
            glottocode=lang['glottocode'],
            family = lang['Family'],
            contribution=contrib,
        )

    colors = dict(zip(
        set(lg.family for lg in data['Variety'].values()),
        qualitative_colors(len(set(lg.family for lg in data['Variety'].values())))))
    for lg in data['Variety'].values():
        lg.jsondata = dict(color=colors[lg.family].replace('#', ''))

    refs = collections.defaultdict(list)

    for param in args.cldf.iter_rows('ParameterTable', 'id', 'concepticonReference', 'name', 'Scientific_Name', ):
        data.add(
            models.Concept,
            param['id'],
            id=param['id'],
            name=param['name'],
            description=param['Spanish_Gloss'],
            concepticon_id=param['concepticonReference'],
            concepticon_gloss=param['Concepticon_Gloss'],
            scientific_name=param['Scientific_Name'],
            concepticon_semantic_field=param['Concepticon_SemanticField'],
        )

    inventories = collections.defaultdict(collections.Counter)
    for form in args.cldf.iter_rows('FormTable', 'id', 'form', 'segments', 'languageReference', 'parameterReference', 'source'):
        inventories[form['languageReference']].update(form['Segments'])
        vsid = (form['languageReference'], form['parameterReference'])
        vs = data['ValueSet'].get(vsid)
        if not vs:
            vs = data.add(
                common.ValueSet,
                vsid,
                id='-'.join(vsid),
                language=data['Variety'][form['languageReference']],
                parameter=data['Concept'][form['parameterReference']],
                contribution=data['Contribution'][form['languageReference']],
            )
        for ref in form.get('source', []):
            sid, pages = Sources.parse(ref)
            refs[(vsid, sid)].append(pages)
        data.add(
            Counterpart,
            form['id'],
            id=form['id'],
            name=form['form'].replace('_', ' '),
            description=' '.join(form['segments']),
            valueset=vs,
            audio=form2audio.get(form['id'])
        )

    for (vsid, sid), pages in refs.items():
        DBSession.add(common.ValueSetReference(
            valueset=data['ValueSet'][vsid],
            source=data['Source'][sid],
            description='; '.join(nfilter(pages))
        ))

    for lid, inv in inventories.items():
        inv = [clts.bipa[c] for c in inv]
        data['Variety'][lid].update_jsondata(
            inventory=[(str(c), c.name) for c in inv if getattr(c, 'name', None)])


def prime_cache(args):
    """If data needs to be denormalized for lookup, do that here.
    This procedure should be separate from the db initialization, because
    it will have to be run periodically whenever data has been updated.
    """

    for cpt in DBSession.query(
        models.Concept, func.count(models.Concept.pk))\
            .join(common.ValueSet).join(common.Value).group_by(
                models.Concept.pk, common.Parameter.pk):
        cpt[0].count_lexemes = cpt[1]

    for language in DBSession.query(common.Language).options(
            joinedload(common.Language.valuesets, common.ValueSet.references)):
        language.count_concepts = len(language.valuesets)
        language.count_lexemes = len(DBSession.query(common.Value.id)
                                     .filter(common.ValueSet.language_pk == language.pk)
                                     .join(common.ValueSet).all())
        language.count_soundfiles = len(DBSession.query(Counterpart.id)
                                     .filter(common.ValueSet.language_pk == language.pk)
                                     .filter(Counterpart.audio.isnot(None))
                                     .join(common.ValueSet).all())
