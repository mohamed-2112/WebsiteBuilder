from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph
from main.reflection_agent.chains import generate_chain, reflect_chain
REFLECT = "reflect"
GENERATE = "generate"


def generation_node(state: Sequence[BaseMessage]):
    return generate_chain.invoke({"messages": state})


def reflection_node(state: Sequence[BaseMessage]):
    res = reflect_chain.invoke({"messages": state})
    return [HumanMessage(content=res.content)]


def should_continue(state: List[BaseMessage]):
    if len(state) > 6:
        return END
    return REFLECT


def test_run():
    builder = MessageGraph()
    builder.add_node(GENERATE, generation_node)
    builder.add_node(REFLECT, reflection_node)
    builder.set_entry_point(GENERATE)
    builder.add_conditional_edges(GENERATE, should_continue)
    builder.add_edge(REFLECT, GENERATE)

    graph = builder.compile()
    print(graph.get_graph().draw_mermaid())

    inputs = HumanMessage(content="""Make this tweet better:
    @langChainAI
    - newly tool Calling feature is seriously uderrated.
    After a long wait, it's here- making the implementation of agents across different models with function calling much easier.
    Make a video covering their newest blog post.
    """)

    response = graph.invoke(inputs)

