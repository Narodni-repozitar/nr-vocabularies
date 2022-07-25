import invenio_vocabularies.services.schema as vocabularies_schema
import marshmallow as ma
import marshmallow.fields as ma_fields
import marshmallow.validate as ma_valid
from invenio_records_resources.services.records.schema import (
    BaseRecordSchema as InvenioBaseRecordSchema,
)
from invenio_vocabularies.services.schema import BaseVocabularySchema
from marshmallow import ValidationError
from marshmallow import validates as ma_validates


class RelatedURISchema(
    ma.Schema,
):
    """RelatedURISchema schema."""

    COAR = ma_fields.String()

    CrossrefFunderID = ma_fields.String()

    ROR = ma_fields.String()

    URL = ma_fields.String()


class NonPreferredLabels(
    ma.Schema,
):
    """NonPreferredLabels schema."""

    cs = ma_fields.List(ma_fields.String())

    en = ma_fields.List(ma_fields.String())


class NRVocabularySchema(
    BaseVocabularySchema,
):
    """NRVocabularySchema schema."""

    relatedURI = ma_fields.Nested(RelatedURISchema)

    marcCode = ma_fields.String()

    dataCiteCode = ma_fields.String()

    alpha3Code = ma_fields.String()

    alpha3CodeENG = ma_fields.String()

    alpha3CodeNative = ma_fields.String()

    acronym = ma_fields.String()

    RID = ma_fields.String()

    ICO = ma_fields.String()

    coarType = ma_fields.String()

    dataCiteType = ma_fields.String()

    nameType = ma_fields.String()

    nonpreferredLabels = ma_fields.Nested(NonPreferredLabels)

    pair = ma_fields.String()

    hint = vocabularies_schema.i18n_strings

    type = ma_fields.Str(required=True, attribute="type.id")

    contexts = ma_fields.List(ma_fields.String())

    tags = ma_fields.List(ma_fields.String())
