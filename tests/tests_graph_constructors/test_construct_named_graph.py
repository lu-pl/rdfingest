"""Pytest entry point for testing Named Graph construction."""

import pytest

from rdflib import URIRef, BNode

from rdfingest.ingest import RDFIngest

from tests.tests_graph_constructors.graph_test_data import sources_expected_contexts_mapping


class TestParseEntrySources:
    """Test container for RDFIngest._parse_entry_sources."""

    @pytest.mark.parametrize(
        ["sources", "expected"],
        sources_expected_contexts_mapping
    )
    def test_parse_entry_sources_count_graphs(self, sources, expected):
        """Run RDFIngest._parse_entry_sources and count the generated context graphs."""
        graphs = RDFIngest._parse_entry_sources(
            source=sources,
            graph_id="https://test.graph/test/"
        )

        len_graphs = len(list(graphs))
        assert len_graphs == expected


    @pytest.mark.parametrize(
        "sources",
        map(lambda x: x[0], sources_expected_contexts_mapping)
    )
    def test_parse_entry_sources_no_bnodes(self, sources):
        """Run RDFIngest._parse_entry_sources and check if there are any BNodes."""
        graphs = RDFIngest._parse_entry_sources(
            source=sources,
            graph_id="https://test.graph/test/"
        )

        bnode_identifiers = any(
            isinstance(g.identifier, BNode)
            for g in graphs
        )

        assert not bnode_identifiers
