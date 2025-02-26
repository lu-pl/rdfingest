![<img source="goku_rdf_slurp.png" width=10% height=10%>](https://raw.githubusercontent.com/lu-pl/rdfingest/main/goku_rdf_slurp.png)

# RDFIngest
![tests](https://github.com/lu-pl/rdfingest/actions/workflows/tests.yaml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/lu-pl/rdfingest/badge.svg?branch=main)](https://coveralls.io/github/lu-pl/rdfingest?branch=main)
[![PyPI version](https://badge.fury.io/py/rdfingest.svg)](https://badge.fury.io/py/rdfingest)
[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


RDFIngest - A tool for ingesting local and remote RDF data sources into a triplestore.

> WARNING: This project is in an early stage of development and should be used with caution.


This branch will implement a complete rewrite of the original RDFIngest prototype.

Planned changes:

- RDFIngest will adhere to the [W3C Graph Store Protocol](https://www.w3.org/TR/sparql12-graph-store-protocol/);
  i.e. ingest operations to named graphs will be implemented as HTTP PUT/POST requests, RDF data will be sent as HTTP payload body
  
- introduce a unified config that also supports environment variable resolution

- run ingest operations asynchronously and additionally provide an asyncio code interface 
