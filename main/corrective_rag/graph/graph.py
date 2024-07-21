from dotenv import load_dotenv

load_dotenv("D:\PycharmProjects\WebsiteBuilder\config\.env")

from langgraph.graph import END, StateGraph

from main.corrective_rag.graph.consts import RETRIEVE, GENERATE, WEBSEARCH, GRADE_DOCUMENTS
from main.corrective_rag.graph.nodes import generate, retrieve, grade_documents, web_search
from main.corrective_rag.graph.state import GraphState


def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")
    if state["web_search"]:
        print("--- DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE")
        return WEBSEARCH
    else:
        print("--DECISION: GENERATE---")
        return GENERATE

workflow = StateGraph(GraphState)
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS,
    decide_to_generate,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE:GENERATE,
    },
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)
app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph_test.png")