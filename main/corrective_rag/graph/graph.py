from dotenv import load_dotenv

load_dotenv("D:\PycharmProjects\WebsiteBuilder\config\.env")

from langgraph.graph import END, StateGraph

from main.corrective_rag.graph.consts import RETRIEVE, GENERATE, WEBSEARCH, GRADE_DOCUMENTS
from main.corrective_rag.graph.nodes import generate, retrieve, grade_documents, web_search
from main.corrective_rag.graph.state import GraphState
from main.corrective_rag.graph.chains.answer_grader import answer_grader
from main.corrective_rag.graph.chains.hallucination_grader import hallucination_grader


def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")
    if state["web_search"]:
        print("--- DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE")
        return WEBSEARCH
    else:
        print("--DECISION: GENERATE---")
        return GENERATE


def grade_generation_in_documents_and_questions(state: GraphState) -> str:
    print("---GRADING DOCUMENTS---")
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]
    score = hallucination_grader.invoke(
        {"documents": documents, "generation": generation}
    )
    if hallucination_grade := score.binary_score:
        print("---DECISION: GENERATION IS GROUNDED IN DOCUMENTS---")
        print("---GRADE GENERATION VS QUESTION---")
        score = answer_grader.invoke({"question": question, "generation": generation})
        if answer_grade := score.binary_score:
            print("---DECISION: GENERATION ADDRESSES QUESTION---")
            return "useful"
        else:
            print("---DECISION: GENERATION DOES NOT ADDRESS THE QUESTION---")
            return "not useful"

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
workflow.add_conditional_edges(
    GENERATE,
    grade_generation_in_documents_and_questions,
    {
        "not supported": GENERATE,
        "useful": END,
        "not useful": WEBSEARCH,
    }
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)
app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph_test.png")