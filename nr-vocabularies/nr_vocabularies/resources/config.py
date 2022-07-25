from invenio_records_resources.resources import (
    RecordResourceConfig as InvenioRecordResourceConfig,
)
from oarepo_vocabularies.resources.config import OARepoVocabulariesResourceConfigBase


class NRVocabulariesResourceConfig(
    OARepoVocabulariesResourceConfigBase, InvenioRecordResourceConfig
):
    """NRVocabulary resource config."""

    blueprint_name = "NRVocabularies"
    url_prefix = "/v/"
