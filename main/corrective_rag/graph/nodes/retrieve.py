from typing import Any, Dict
from main.corrective_rag.graph.state import GraphState
from main.corrective_rag.ingestion import retriever


def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]
    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}
