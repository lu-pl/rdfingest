"""Simple data for Registry Model tests."""

from importlib.resources import files


_model_tests_path = files("tests.tests_models.model_test_data")
ttl_file_path = _model_tests_path / "test.ttl"
trig_file_path = _model_tests_path / "test.trig"


pass_data = [
    {
        'source': [
            'https://some.triplestore/repositories/source.trig',
            ttl_file_path,
            'https://some.triplestore/repositories/source.rdf',
        ],
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': [
            'https://some.triplestore/repositories/source.trig',
            ttl_file_path,
            'https://some.triplestore/repositories/source.trig',
        ],
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': [
            'https://some.triplestore/repositories/source.trig',
            trig_file_path,
            'https://some.triplestore/repositories/source.trig',
        ],
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': ['https://some.triplestore/repositories/source.trig'],
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': 'https://some.triplestore/repositories/source.trig',
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': ['https://some.triplestore/repositories/source.trig'],
    },
    {
        'source': 'https://some.triplestore/repositories/source.trig',
    },
    {
        'source': ['https://some.triplestore/repositories/source.ttl'],
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': 'https://some.triplestore/repositories/source.ttl',
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': [
            'https://some.triplestore/repositories/source.trig',
            'https://some.triplestore/repositories/other.trig',
        ]
    },
    {
        'source': [
            'https://some.triplestore/repositories/source.trig',
            trig_file_path
        ]
    }
]

fail_data_invalid_registry = [
    {
        'source': 'https://some.triplestore/repositories/source.ttl',
    },
    {
        'source': ['https://some.triplestore/repositories/source.ttl']
    },
    {
        'source': [
            'https://some.triplestore/repositories/source.ttl',
            'https://some.triplestore/repositories/other.ttl'
        ]
    },
    {
        'source': [
            'https://some.triplestore/repositories/source.ttl',
            ttl_file_path
        ]
    }
]

fail_data_validation_error = [
    {
        'source': './does_not_exist.ttl',
        "graph_id": "https://somegraph.id/"
    },

    {
        'source': trig_file_path,
        "graph_id": "//somegraph.id/"
    },
    {
        "source": "somedata.ttl",
        "graph_id": "https://somegraph.id/"
    },
    {
        'SOURCE': ['https://some.triplestore/repositories/source.ttl'],
        'graph_id': "https://some.triplestore/repositories/somegraph",
    },
    {
        'source': 'https://some.triplestore/repositories/source.ttl',
        'graph_ids': "https://some.triplestore/repositories/somegraph",
    }
]
