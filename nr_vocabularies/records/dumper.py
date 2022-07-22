from invenio_records.dumpers import ElasticsearchDumper as InvenioElasticsearchDumper
from oarepo_vocabularies.records.dumper import OARepoVocabularyDumperBase


class NRVocabulariesDumper(OARepoVocabularyDumperBase, InvenioElasticsearchDumper):
    """NRVocabulary elasticsearch dumper."""
