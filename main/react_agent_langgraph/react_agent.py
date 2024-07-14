from langchain_core.agents import AgentFinish
from langgraph.graph import END, StateGraph
from main.react_agent_langgraph.nodes import execute_tools, run_agent_reasoning_engine
from main.react_agent_langgraph.state import AgentState

AGENT_REASON = "agent_reason"
ACT = "act"


def should_continue(state: AgentState) -> str:
    if isinstance(state["agent_outcome"], AgentFinish):
        return END
    else:
        return ACT


def test():
    flow = StateGraph(AgentState)
    flow.add_node(AGENT_REASON, run_agent_reasoning_engine)
    flow.set_entry_point(AGENT_REASON)
    flow.add_node(ACT, execute_tools)
    flow.add_conditional_edges(AGENT_REASON, should_continue)
    flow.add_edge(ACT, AGENT_REASON)
    app = flow.compile()
    app.get_graph().draw_mermaid_png(output_file_path="graph.png")
    res = app.invoke(
        input={"input": "What is the weather in sf? Write it and then triple it, so you need to provide the original number and the tripled number", }
    )
    print(res["agent_outcome"].return_values["output"])
    print(res)
