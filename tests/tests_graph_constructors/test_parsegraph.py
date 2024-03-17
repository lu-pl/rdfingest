"""Pytest entry point for ParseGraph tests."""

from unittest.mock import patch
from _pytest import monkeypatch

import pytest

from rdflib import Graph
from rdflib.plugin import PluginException
from rdfingest.parse_graph import ParseGraph

from tests.tests_graph_constructors.graph_test_data import ecrm_owl, ecrm_rdf


remote_sources = [
    "https://raw.githubusercontent.com/erlangen-crm/ecrm/master/ecrm_091125.owl",
    "https://raw.githubusercontent.com/lu-pl/clscorgi/main/clscorgi/output/eltec/eltec_eng.ttl"
]


@pytest.mark.remote
@pytest.mark.parametrize("source", remote_sources)
def test_parsegraph_remote_sources(source):
    """Check if parsing remotes with content type 'text/plain' passes with ParseGraph.

    Warning: This tests actually requests a remote source!
    """
    graph = ParseGraph()
    graph.parse(source=source)
    assert graph


@pytest.mark.remote
@pytest.mark.parametrize("source", remote_sources)
def test_graph_remote_sources(source):
    """Check if parsing remotes with content type 'text/plain' fails with Graph.

    Warning: This tests actually requests a remote source!

    This test is connected to 'test_parsegraph_remote_sources';
    Given the same remote sources,
    test_parsegraph_remote_sources should pass,
    while test_graph_remote_sources should fail.
    """
    with pytest.raises(PluginException):
        graph = Graph()
        graph.parse(source=source)


@pytest.mark.parametrize("source", [ecrm_owl, ecrm_rdf])
def test_parsegraph_fake_remote(source):
    """Check if parsing remotes with content type 'text/plain' passes with ParseGraph.

    Remote calls are mocked by passing format='text/plain'.
    """
    graph = ParseGraph().parse(source=source, format="text/plain")
    assert graph


@pytest.mark.parametrize("source", [ecrm_owl, ecrm_rdf])
def test_graph_fake_remote(source):
    """Check if parsing remotes with content type 'text/plain' fails with Graph.

    Remote calls are mocked by passing format='text/plain'.
    """
    with pytest.raises(PluginException):
        graph = Graph().parse(source=source, format="text/plain")
        assert graph
