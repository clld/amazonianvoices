from zope.interface import implementer
from sqlalchemy import (
    Column,
    Unicode,
    Integer,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship, backref

from clld import interfaces
from clld.db.meta import Base, CustomModelMixin
from clld.db.models import common
from pyclts.ipachart import Segment


@implementer(interfaces.ILanguage)
class Variety(CustomModelMixin, common.Language):
    pk = Column(Integer, ForeignKey('language.pk'), primary_key=True)
    glottocode = Column(Unicode)
    family = Column(Unicode)
    contribution_pk = Column(Integer, ForeignKey('contribution.pk'))
    contribution = relationship(common.Contribution, backref=backref('variety', uselist=False))
    count_lexemes = Column(Integer)
    count_concepts = Column(Integer)
    count_soundfiles = Column(Integer)

    @property
    def inventory(self):
        return [Segment(
            sound_bipa=k,
            sound_name=v,
            href='https://clts.clld.org/parameters/{}'.format(v.replace(' ', '_')),
        ) for k, v in self.jsondata['inventory']]

    def get_identifier_objs(self, type_):
        o = common.Identifier()
        if getattr(type_, 'value', type_) == str(common.IdentifierType.glottolog):
            if not self.glottocode:
                return []
            o.name = self.glottocode
            o.type = str(common.IdentifierType.glottolog)
            return [o]
        if hasattr(self, 'iso'):
            if getattr(type_, 'value', type_) == str(common.IdentifierType.iso):
                if not self.iso:
                    return []
                o.name = self.iso
                o.type = str(common.IdentifierType.iso)
                return [o]
        return []


@implementer(interfaces.IParameter)
class Concept(CustomModelMixin, common.Parameter):
    pk = Column(Integer, ForeignKey('parameter.pk'), primary_key=True)
    concepticon_id = Column(Unicode)
    concepticon_gloss = Column(Unicode)
    concepticon_semantic_field = Column(Unicode)
    scientific_name = Column(Unicode)
    count_lexemes = Column(Integer)
