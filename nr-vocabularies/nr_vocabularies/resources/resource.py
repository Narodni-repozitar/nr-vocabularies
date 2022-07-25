from invenio_records_resources.resources import RecordResource as InvenioRecordResource
from oarepo_vocabularies.resources.resource import OARepoVocabulariesResourceBase


class NRVocabulariesResource(OARepoVocabulariesResourceBase, InvenioRecordResource):
    """NRVocabulary resource."""

    # here you can for example redefine
    # create_url_rules function to add your own rules
