from invenio_db import db
from invenio_records.models import RecordMetadataBase


class ExampleMetadata(db.Model, RecordMetadataBase):
    """Model for ExampleRecord metadata."""

    __tablename__ = "example_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}
