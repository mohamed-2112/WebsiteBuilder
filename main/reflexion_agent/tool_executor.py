from typing import List

from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, ToolMessage, HumanMessage, AIMessage

from main.reflexion_agent.shemas import AnswerQuestion, Reflection

load_dotenv()

def execute_tools(state: List[BaseMessage]) -> List[ToolMessage]:
    tool_invocation: AIMessage = state[-1]
    pass


human_message = HumanMessage(
    content="Write about AI-Powered SOC / autonomous soc problem domain,"
            "list startups that do that and raised capital."
)

answer = AnswerQuestion(
    answer="",
    reflection=Reflection(missing="", superfluous=""),
    search_queries=[
        "AI-powered SOC startups funding",
        "AI SOC problem domain specifics",
        "Technologies used by AI-powered SOC startups",
    ],
    id="call_aldkstghj2askdfjaloi"
)

# raw_res = execute_tools(
#     state=[
#         human_message,
#         AIMessage(
#             content="",
#             tool_calls[
#                 {
#                     "name": AnswerQuestion.__name__,
#                     "args": answer.dict(),
#                     "id": "call_aldkstghj2askdfjaloi",
#                 }
#             ],
#         ),
#     ]
# )