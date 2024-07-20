from dotenv import load_dotenv

load_dotenv("D:\PycharmProjects\WebsiteBuilder\config\.env")

from main.corrective_rag.graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from main.corrective_rag.ingestion import retriever
from pprint import pprint
from main.corrective_rag.graph.chains.generation import generation_chain


def test_retrieval_grader_answer_yes() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retrieval_grader.invoke({"question": question, "document": doc_txt})
    assert res.binary_score == "yes"


def test_retrieval_grader_answer_no() -> None:
    question = "how to make pizaa"
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retrieval_grader.invoke({"question": question, "document": doc_txt})
    assert res.binary_score == "no"

def test_generation_chain() -> None:
    question = "agent memory"
    docs = retriever.invoke(question)
    generation = generation_chain.invoke({"context": docs, "question": question})
    pprint(generation)