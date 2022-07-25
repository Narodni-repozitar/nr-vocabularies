from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from oarepo_vocabularies.services.config import OARepoVocabulariesServiceConfigBase

from nr_vocabularies.records.api import NRVocabulary
from nr_vocabularies.services.permissions import NRVocabulariesPermissionPolicy
from nr_vocabularies.services.schema import NRVocabularySchema
from nr_vocabularies.services.search import NRVocabulariesSearchOptions


class NRVocabulariesServiceConfig(
    OARepoVocabulariesServiceConfigBase, InvenioRecordServiceConfig
):
    """NRVocabulary service config."""

    permission_policy_cls = NRVocabulariesPermissionPolicy
    schema = NRVocabularySchema
    search = NRVocabulariesSearchOptions
    record_cls = NRVocabulary

    components = [*OARepoVocabulariesServiceConfigBase.components]

    model = "nr_vocabularies"
