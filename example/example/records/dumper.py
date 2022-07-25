from invenio_records.dumpers import ElasticsearchDumper as InvenioElasticsearchDumper


class ExampleDumper(InvenioElasticsearchDumper):
    """ExampleRecord elasticsearch dumper."""
