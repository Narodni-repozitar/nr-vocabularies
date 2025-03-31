import logging
import tempfile

from invenio_vocabularies.records.api import Vocabulary
from oarepo_runtime.datastreams.fixtures import dump_fixtures, load_fixtures
from oarepo_runtime.datastreams.types import StatsKeepingDataStreamCallback


def test_complex_import_export(app, db, cache, search_clear, vocab_cf, caplog):
    caplog.set_level(logging.ERROR)
    load_callback = StatsKeepingDataStreamCallback()
    load_fixtures(batch_size=100, callback=load_callback)
    
    # Log the number of failed entries
    logging.error(f"Failed entries count: {load_callback.failed_entries_count}")
    
    if load_callback.failed_entries_count > 0:
        for record in caplog.records:
            print(record.message)
    
    assert load_callback.failed_entries_count == 0
    assert load_callback.filtered_entries_count == 0
    assert load_callback.ok_entries_count == 1627
    Vocabulary.index.refresh()

    with tempfile.TemporaryDirectory() as d:
        dump_callback = StatsKeepingDataStreamCallback()
        dump_fixtures(d, callback=dump_callback)
        assert dump_callback.failed_entries_count == 0
        assert dump_callback.filtered_entries_count == 0
        assert dump_callback.ok_entries_count == load_callback.ok_entries_count
