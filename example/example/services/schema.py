import marshmallow as ma
import marshmallow.fields as ma_fields
import marshmallow.validate as ma_valid
from invenio_records_resources.services.records.schema import BaseRecordSchema
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from marshmallow import ValidationError
from marshmallow import validates as ma_validates
from nr_vocabularies.services.schema import NRVocabularySchema
from oarepo_vocabularies.services.schema import VocabularyRelationField

from example.records.api import ExampleRecord


class ExampleSchema(
    BaseRecordSchema,
):
    """ExampleSchema schema."""

    title = ma_fields.String()

    lang = VocabularyRelationField(
        NRVocabularySchema, related_field=ExampleRecord.relations.lang, many=False
    )

    created = ma_fields.Date(dump_only=True)

    updated = ma_fields.Date(dump_only=True)

    affiliations = VocabularyRelationField(
        NRVocabularySchema,
        related_field=ExampleRecord.relations.affiliations,
        many=True,
    )

    subjects = VocabularyRelationField(
        NRVocabularySchema, related_field=ExampleRecord.relations.subjects, many=True
    )
