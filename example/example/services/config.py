from invenio_records_resources.services import RecordLink
from invenio_records_resources.services import (
    RecordServiceConfig as InvenioRecordServiceConfig,
)
from invenio_records_resources.services import pagination_links
from invenio_records_resources.services.records.components import (
    DataComponent,
    RelationsComponent,
)

from example.records.api import ExampleRecord
from example.services.permissions import ExamplePermissionPolicy
from example.services.schema import ExampleSchema
from example.services.search import ExampleSearchOptions


class ExampleServiceConfig(InvenioRecordServiceConfig):
    """ExampleRecord service config."""

    permission_policy_cls = ExamplePermissionPolicy
    schema = ExampleSchema
    search = ExampleSearchOptions
    record_cls = ExampleRecord

    components = [
        *InvenioRecordServiceConfig.components,
        DataComponent,
        RelationsComponent,
    ]

    model = "example"

    @property
    def links_item(self):
        return {
            "self": RecordLink("/example/{id}"),
        }

    links_search = pagination_links("/example/{?args*}")
