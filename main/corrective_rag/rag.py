print("test start")
from main.corrective_rag.graph.graph import app
def test():
    print("test rag")
    print(app.invoke(input={"question": "what is agent memory?"}))