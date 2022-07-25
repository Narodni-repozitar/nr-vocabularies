import nr_vocabularies.records.api
import oarepo_vocabularies.records.system_fields.pid_hierarchy_relation
from invenio_pidstore.providers.recordid_v2 import RecordIdProviderV2
from invenio_records.dumpers.relations import RelationDumperExt
from invenio_records.systemfields import ConstantField, RelationsField
from invenio_records_resources.records.api import Record as InvenioBaseRecord
from invenio_records_resources.records.systemfields import IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext

from example.records.dumper import ExampleDumper
from example.records.models import ExampleMetadata


class ExampleRecord(InvenioBaseRecord):
    model_cls = ExampleMetadata
    schema = ConstantField("$schema", "local://example-1.0.0.json")
    index = IndexField("example-example-1.0.0")

    pid = PIDField(
        create=True, provider=RecordIdProviderV2, context_cls=PIDFieldContext
    )

    dumper_extensions = [
        RelationDumperExt("relations"),
    ]
    dumper = ExampleDumper(extensions=dumper_extensions)

    relations = RelationsField(
        lang=oarepo_vocabularies.records.system_fields.pid_hierarchy_relation.PIDHierarchyRelation(
            "lang",
            keys=["id", "title"],
            pid_field=nr_vocabularies.records.api.NRVocabulary.pid.with_type_ctx(
                "hierarchy"
            ),
            cache_key="lang-relation",
        ),
        affiliations=oarepo_vocabularies.records.system_fields.pid_hierarchy_relation.PIDHierarchyListRelation(
            "affiliations",
            keys=["id", "title"],
            pid_field=nr_vocabularies.records.api.NRVocabulary.pid.with_type_ctx(
                "hierarchy"
            ),
            cache_key="affiliations-relation",
        ),
        subjects=oarepo_vocabularies.records.system_fields.pid_hierarchy_relation.PIDHierarchyListRelation(
            "subjects",
            keys=["id", "title"],
            pid_field=nr_vocabularies.records.api.NRVocabulary.pid.with_type_ctx(
                "hierarchy"
            ),
            cache_key="subjects-relation",
        ),
    )
