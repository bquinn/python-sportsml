#!/usr/bin/env python

import xml.etree.ElementTree as etree
from .core import NEWSMLG2_NS, BaseObject
from .base_metadata import BaseMetadata, CommonAttributes


class CatalogRefs(BaseObject):
    # TODO
    pass

class SportsTitles(BaseObject):
    # TODO
    pass

class SportsTitle(BaseObject):
    # TODO
    pass

class Advisory(CommonAttributes):
    # TODO
    pass

class FeatureNames(BaseObject):
    # TODO
    pass

class FeatureName(BaseObject):
    # TODO
    pass

class SportsMetadata(BaseMetadata):
    # A reference to document(s) listing externally-supplied controlled vocabularies.
    # The catalog file can be in NewsML 1.
    catalog_refs = None
    # A short textual description of the document.
    # Can  show up in search results.
    sports_titles = None    
    # A short textual message to editors receiving the document.
    # Not generally published through to end-users.
    advisory = None
    # A displayable name for the resource identified by the fixture-key.
    feature_names = None
    attributes = {
        # The often-unique ID of the document, tracked by publishers.
        'doc-id': 'docId',
        # Publisher of the data.
        'publisher': 'publisher',
        # Date-timestamp for the document, normalized to ISO 8601 extended format: YYYY-MM-DDTHH:MM:SS+HH:MM. Use YYYY-MM-DD when no time is available
        'date-time': 'dateTime',
        # The default language of the document. NAR-construction. Values must be valid BCP 47 language tags.
        'language': 'language',
        # A keyword used by editors to refer to the document.
        'slug': 'slug',
        # A category code for the document type (fixture-key).
        # Recommended categories contained in SportsML vocabulary uri: http://cv.iptc.org/newscodes/spct/
        'document-class': 'documentClass',
        # A publisher-specific key for the type of regularly-published document
        # (or genre) being transmitted. Eg. event-stats, roster, standings (table), etc.
        # SportsML vocabulary uri: http://cv.iptc.org/newscodes/spfixt/
        'fixture-key': 'fixtureKey',
    }

    def __init__(self, **kwargs):
        super(SportsMetadata, self).__init__(**kwargs)
        xmlelement = kwargs.get('xmlelement')
        if type(xmlelement) == etree.Element:
            self.catalog_refs = CatalogRefs(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'catalogRef')
            )
            self.sports_titles = SportsTitles(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'sports-title')
            )
            self.advisory = Advisory(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'advisory')
            )
            self.feature_names = FeatureNames(
                xmlarray = xmlelement.findall(NEWSMLG2_NS+'feature-name')
            )

    def as_dict(self):
        dict = super(SportsMetadata, self).as_dict()
        if self.catalog_refs:
            self.dict.update({'catalogRefs': self.catalog_refs.as_dict() })
        if self.sports_titles:
            self.dict.update({'sportsTitles': self.sports_titles.as_dict() })
        if self.advisory:
            self.dict.update({'advisory': self.advisory.as_dict() })
        if self.feature_names:
            self.dict.update({'featureNames': self.feature_names.as_dict() })
        return self.dict
