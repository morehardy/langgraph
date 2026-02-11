import pytest
from langgraph.graph import StateGraph, START
from langgraph.pregel import Pregel
from langgraph._internal._config import ensure_config, merge_configs

def test_invoke_with_invalid_config_type_raises_type_error():
    builder = StateGraph(dict)
    builder.add_node("node", lambda s: s)
    builder.add_edge(START, "node")
    graph = builder.compile()

    with pytest.raises(TypeError, match="Expected config to be a mapping"):
        graph.invoke({}, config="invalid")

    with pytest.raises(TypeError, match="Expected config to be a mapping"):
        list(graph.stream({}, config="invalid_string"))

def test_merge_configs_validation():
    
    with pytest.raises(TypeError, match="Expected config to be a mapping"):
        ensure_config({"valid": "dict"}, "invalid_string")

    with pytest.raises(TypeError, match="Expected config to be a mapping"):
        merge_configs({"a": 1}, "invalid_string")