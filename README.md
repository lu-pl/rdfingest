![<img src="lodkit.png" width=10% height=10%>](https://raw.githubusercontent.com/lu-pl/rdfingest/main/goku_rdf_slurp.png)

# RDFIngest
![tests](https://github.com/lu-pl/rdfingest/actions/workflows/tests.yaml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/lu-pl/rdfingest/badge.svg?branch=main)](https://coveralls.io/github/lu-pl/rdfingest?branch=main)
[![license: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)


RDFIngest - A simple tool for ingesting local and remote RDF data sources into a triplestore.

## Requirements

* Python >= 3.11

## Installation

## Usage

RDFIngest reads two YAML files: 
- a config file for obtaining triplestore credentials and 
- a registry which defines the RDF sources to be ingested.

#### Example config:
```yaml
service:
  endpoint: "https://sometriplestore.endpoint"
  user: "admin"
  password: "supersecretpassword123"
```

#### Example registry:
```yaml
graphs:
  
  # ttl
  - source: https://raw.githubusercontent.com/lu-pl/clscorgi/main/clscorgi/output/rem/rem.ttl
    graph_id: https://somenamedgraph.id

  # multiple ttl to a single named graph
  - source: [
    https://raw.githubusercontent.com/lu-pl/clscorgi/main/clscorgi/output/eltec/eltec_cze.ttl,
    https://raw.githubusercontent.com/lu-pl/clscorgi/main/clscorgi/output/eltec/eltec_deu.ttl
    ]
    graph_id: https://somenamedgraph.id
    
  # trig; no graph_id required
  - source: <trig source>
  
  # trig + ttl
  - source: [
    <trig source>,
    https://raw.githubusercontent.com/lu-pl/clscorgi/main/clscorgi/output/eltec/eltec_cze.ttl,
    https://raw.githubusercontent.com/lu-pl/clscorgi/main/clscorgi/output/eltec/eltec_deu.ttl
    ]
    graph_id: https://somenamedgraph.id
```

For contextless RDF resources all graphs are merged into a named graph identified by `graph_id`.  

[RDF Datasets](https://www.w3.org/TR/rdf11-concepts/#section-dataset)/Quad formats obviously do not require a `graph_id` field.  
Multiple datasets are merged into a single dataset containing all named graphs of all datasets.  

If the source field references both contextless *and* contextualized RDF sources, contextless sources are merged into a single named graph and added to the dataset.  

The tool accepts both local and remote RDF data sources.

### CLI

### RDFIngest class

Point an `RDFIngest` instance to a config file and a registry and invoke `run_ingest`.

```python
rdfingest = RDFIngest(registry="./registry.yaml", config="./config.yaml")
rdfingest.run_ingest()
```
