![<img src="lodkit.png" width=10% height=10%>](https://raw.githubusercontent.com/lu-pl/rdfingest/main/goku_rdf_slurp.png)

# RDFIngest

RDFIngest - A simple tool for ingesting local and remote RDF data sources into a triplestore.

## Requirements

* Python >= 3.11

## Installation

## Usage

RDFIngest reads two YAML files, a config file for obtaining triplestore credentials and a registry which defines the RDF sources to be ingested.

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

For contextless RDF resources all graphs are merged to a named graph identified by `graph_id`. Quad formats obviously do not require a `graph_id` field.  

If the source field references contextless *and* contextualized RDF sources, contextless sources are merged into a single named graph and added to the initial context graph.  


Note: RDFIngest also accepts local RDF data sources.

### CLI

### RDFIngest class
