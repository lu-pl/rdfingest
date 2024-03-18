"""Pytest entry point for testing Named Graph construction."""

import pytest

from rdflib import URIRef, BNode

from rdfingest.ingest import RDFIngest

from tests.tests_graph_constructors.graph_test_data import sources_expected_contexts_mapping


class TestConstructNamedGraph:
    """Test container for RDFIngest._construct_named_graph."""

    @pytest.mark.parametrize(
        ["sources", "expected"],
        sources_expected_contexts_mapping
    )
    def test_number_named_graphs(self, sources, expected):
        """Invoke RDFIngest._construct_named_graph on various sources
        and check the number of context graphs in the named graph.

        Note: For trig only content an additional empty graph is generated if graph_id is given.
        Should this be handled in RDFIngest or not?
        """
        expected += 1  # default graph
        sources = [str(source) for source in sources]

        named_graph = RDFIngest._construct_named_graph(
            sources, URIRef("https://testnamegraph.id")
        )

        contexts = list(named_graph.contexts())

        assert len(contexts) == expected


    @pytest.mark.parametrize(
        "sources",
        map(lambda x: x[0], sources_expected_contexts_mapping)
    )
    def test_no_bnodes(self, sources):
        """Check for BNodes as graph identifiers."""
        sources = [str(source) for source in sources]

        named_graph = RDFIngest._construct_named_graph(
            sources, URIRef("https://testnamegraph.id")
        )

        context_identifiers = [
            context.identifier  # type: ignore
            for context in named_graph.contexts()
        ]

        no_bnodes_p = not any(
            isinstance(identifier, BNode)
            for identifier in context_identifiers
        )

        assert no_bnodes_p
