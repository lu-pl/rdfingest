"""Pytest entry point for testing RDFIngest._get_dataset_from_graph."""

import pytest

from rdflib import Dataset, Graph, BNode, URIRef

from rdfingest.ingest import RDFIngest, BNodeIDException
from rdfingest.parse_graph import ParseGraph


class TestGetDatasetFromGraph:
    """Test container for RDFIngest._get_dataset_from_graph"""

    @pytest.mark.parametrize(
        "graph",
        (
            Graph(),
            ParseGraph(),
            Graph(identifier=BNode()),
            ParseGraph(identifier=BNode())
        )
    )
    def test_fail_bnode_id(self, graph):
        """Check if passing a graph with a BNode ID fails."""
        with pytest.raises(BNodeIDException):
            RDFIngest._get_dataset_from_graph(graph)

    def test_inspect_result(self):
        """Check the result of _get_dataset_from_graph.

        Check if the result is a Dataset and if its context
        is the same graph processed by _get_dataset_from_graph.
        """
        graph_id = URIRef("https://some.graph/id/")
        graph = Graph(identifier=graph_id)

        dataset = RDFIngest._get_dataset_from_graph(graph)
        assert isinstance(dataset, Dataset)

        context = next(dataset.contexts())
        assert context is graph
