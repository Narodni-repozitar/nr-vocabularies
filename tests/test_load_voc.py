from nr_vocabularies.records.api import NRVocabulary
from oarepo_vocabularies.datastreams.catalogue import YAMLVocabularyCatalogue
from oarepo_vocabularies.datastreams.excel import ExcelReader
import os
CATALOGUE_FILE = os.path.join(os.path.dirname(__file__), '../data/catalogue.yaml')

def test_load_vocabularies(app,nrvoc_service, identity):
    ret = YAMLVocabularyCatalogue().create_or_update_vocabularies(CATALOGUE_FILE, identity)
    NRVocabulary.index.refresh()
    assert ret == {
        'access-rights': {'errored': [], 'filtered': 0, 'success': 4},
        'contributor-types': {'errored': [], 'filtered': 0, 'success': 34},
        'countries': {'errored': [], 'filtered': 0, 'success': 249},
        'funders': {'errored': [], 'filtered': 0, 'success': 75},
        'institutions': {'errored': [], 'filtered': 0, 'success': 1781},
        'item-relation-types': {'errored': [], 'filtered': 0, 'success': 34},
        'languages': {'errored': [], 'filtered': 0, 'success': 184},
        'licenses': {'errored': [], 'filtered': 0, 'success': 36},
        'related-resource-types': {'errored': [], 'filtered': 0, 'success': 48},
        'resource-types': {'errored': [], 'filtered': 0, 'success': 37},
        'subject-categories': {'errored': [], 'filtered': 0, 'success': 255}
    }

    ret = YAMLVocabularyCatalogue().create_or_update_vocabularies(CATALOGUE_FILE, identity, update=True)
    NRVocabulary.index.refresh()
    assert ret == {
        'access-rights': {'errored': [], 'filtered': 0, 'success': 4},
        'contributor-types': {'errored': [], 'filtered': 0, 'success': 34},
        'countries': {'errored': [], 'filtered': 0, 'success': 249},
        'funders': {'errored': [], 'filtered': 0, 'success': 75},
        'institutions': {'errored': [], 'filtered': 0, 'success': 1781},
        'item-relation-types': {'errored': [], 'filtered': 0, 'success': 34},
        'languages': {'errored': [], 'filtered': 0, 'success': 184},
        'licenses': {'errored': [], 'filtered': 0, 'success': 36},
        'related-resource-types': {'errored': [], 'filtered': 0, 'success': 48},
        'resource-types': {'errored': [], 'filtered': 0, 'success': 37},
        'subject-categories': {'errored': [], 'filtered': 0, 'success': 255}
    }
