"""Very simple Typer CLI for RDFIngest."""

from pathlib import Path
from typing import Annotated

import typer

from loguru import logger

from rdfingest.cli_help import config_help, registry_help
from rdfingest.rdfingest import RDFIngest


def main(
        config: Annotated[
            Path | str,
            typer.Option(help=config_help)
        ] = "./config.yaml",
        registry: Annotated[
            Path | str,
            typer.Option(help=registry_help)
        ] = "./registry.yaml"
):
    """RDFIngest CLI."""
    logger.info("Initializing RDFIngest.")
    rdfingest = RDFIngest(config=config, registry=registry)

    logger.info(f"Running update requests against '{rdfingest.config.service.endpoint}'.")
    print("Dummy run")
    # rdfingest.run_ingest()


if __name__ == "__main__":
    typer.run(main)
