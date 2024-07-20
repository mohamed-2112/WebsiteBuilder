from typing import Any, Dict
from langchain.schema import Document
from langchain_community.tools.tavily_search import TavilySearchResults
from main.corrective_rag.graph.state import GraphState

web_search_tool = TavilySearchResults(max_results=3)

def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]
    tavily_results = web_search_tool.invoke({"query": question})
    joined_tavily_results = "\n".join(
        [tavily_results["content"] for tavily_result in tavily_results]
    )
    web_result = Document(page_content=joined_tavily_results)
    if documents is not None:
        documents.append(web_result)
    else:
        documents = [web_result]
    return {"documents": documents, "question": question}