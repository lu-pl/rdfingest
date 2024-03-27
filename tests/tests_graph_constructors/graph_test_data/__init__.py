from importlib.resources import files


_data_path = files("tests.tests_graph_constructors.graph_test_data")

trig1 = _data_path / "trig_test_1.trig"
trig2 = _data_path / "trig_test_2.trig"

ttl1 = _data_path / "ttl_test_1.ttl"
ttl2 = _data_path / "ttl_test_2.ttl"

ecrm_owl = _data_path / "ecrm.owl"
ecrm_rdf = _data_path / "ecrm.rdf"

sources_expected_contexts_mapping = [
    ([ttl1], 1),
    ([ttl2], 1),
    ([trig1], 3),
    ([trig2], 3),
    ([ttl1, ttl2], 2),
    ([trig1, trig2], 6),
    ([trig1, ttl1], 4),
    ([ttl2, trig2], 4),
    ([ttl1, trig1, ttl2], 5),
    ([ttl1, ttl2, trig1, trig2], 8),
]
