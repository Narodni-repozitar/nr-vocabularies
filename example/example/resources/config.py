from invenio_records_resources.resources import (
    RecordResourceConfig as InvenioRecordResourceConfig,
)


class ExampleResourceConfig(InvenioRecordResourceConfig):
    """ExampleRecord resource config."""

    blueprint_name = "Example"
    url_prefix = "/example/"
