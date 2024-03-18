"""RDFIngest.

Automatically ingest local and/or remote RDF data sources indicated in a YAML registry into a triplestore.
"""

from inspect import stack
from pathlib import Path

import requests

from loguru import logger
from rdflib import Dataset, URIRef

from rdfingest.parse_graph import ParseGraph

from rdfingest.yaml_loaders import config_loader, registry_loader
from rdfingest.models import RegistryModel, ConfigModel


class RDFIngest:
    """RDFIngest class.

    This class provides functionality for automatically ingesting local/remote RDF data sources
    indicated in a YAML registry into a triplestore.

    :param registry: Indicites a local YAML file which registers local/remote RDF data sources.
    This YAML file gets validated against rdfingest.models.RegistryModel.

    :param config: Indicates a local YAML file which holds credentials for a triplestore.
    This YAML file gets validated against rdfingest.models.ConfigModel.
    """
    def __init__(
            self,
            registry: str | Path = "./registry.yaml",
            config: str | Path = "./config.yaml"
    ) -> None:
        """RDFIngester initializer."""
        self.registry: RegistryModel = registry_loader(registry)
        self.config: ConfigModel = config_loader(config)

    @staticmethod
    def _construct_named_graph(
            source: list[str],
            graph_id: str | None = None
    ) -> Dataset:
        """Construct a named graph from a list of sources."""
        _get_extension = lambda x: str(x).rpartition(".")[-1]
        _graph_id = URIRef(str(graph_id)) if graph_id is not None else graph_id

        dataset = Dataset()
        graph = ParseGraph(identifier=_graph_id)

        for _source in source:
            if _get_extension(_source) in ["trig", "trix"]:
                dataset.parse(source=_source)
            else:
                graph.parse(source=_source)

        if graph and _graph_id is None:
            logger.info(
                "Parameter 'graph_id' not specified. "
                "Named graph identifier will be a blank node."
            )

        dataset.graph(graph)
        return dataset

    def _run_named_graph_update_request(self, named_graph: Dataset) -> requests.Response:
        """Execute a POST request for a named graph against the config store.

        Note: This is used as a side-effects only callable.
        """
        auth: tuple[str, str] = self.config.service.user, self.config.service.password

        response = requests.post(
            self.config.service.endpoint,
            headers={"Content-Type": "application/x-trig"},
            data=named_graph.serialize(format="trig"),
            auth=auth
        )
        return response

    def run_ingest(self) -> None:
        """Run RDF source ingest against a triplestore.

        The method constructs named graphs based on Registry entries
        and executes a POST request against the config store.
        """
        for entry in self.registry.graphs:
            logger.info(f"Constructing named graph for {entry.source}.")
            named_graph = self._construct_named_graph(**dict(entry))

            logger.info("Updating.")
            self._run_named_graph_update_request(named_graph)
