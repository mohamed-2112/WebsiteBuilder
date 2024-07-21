from typing import Any, Dict
from main.corrective_rag.graph.chains.generation import generation_chain
from main.corrective_rag.graph.state import GraphState

def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATING---")
    question = state["question"]
    documents = state["documents"]
    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}
