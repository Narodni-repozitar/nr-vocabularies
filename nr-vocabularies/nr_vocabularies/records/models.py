from invenio_db import db
from invenio_records.models import RecordMetadataBase
from oarepo_vocabularies.records.models import OARepoVocabularyMetadataBase


class NRVocabulariesMetadata(
    OARepoVocabularyMetadataBase, db.Model, RecordMetadataBase
):
    """Model for NRVocabulary metadata."""

    __tablename__ = "nrvocabularies_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
