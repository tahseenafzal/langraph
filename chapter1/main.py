from langgraph.graph import StateGraph, START, END
from classes import State
from nodes import node_1


graph_builder = StateGraph(state_schema=State)

graph_builder.add_node("node_one", node_1)

graph_builder.add_edge(START, "node_one")
graph_builder.add_edge("node_one", END)

graph = graph_builder.compile()

res = graph.invoke({"prompt": "Hi"})

print(res)