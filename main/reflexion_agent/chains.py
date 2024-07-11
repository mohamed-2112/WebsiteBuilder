from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pathlib import Path
import datetime
from langchain_core.output_parsers.openai_tools import JsonOutputToolsParser, PydanticToolsParser
from langchain_core.messages import HumanMessage

env_path = Path('config') / '.env'
load_dotenv(dotenv_path=env_path)


actor_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are expert researcher.
            current time: {time}
            
            1. {first_instruction}
            2. Reflect and critique your answer. Be severe to maximize improvement.
            3. Recommend search queries to research information and improve your answer.
            """,
        ),
        MessagesPlaceholder(variable_name="messages"),
        ("system", "Answer the user's question above using the required format.")
    ]
).partial(
    time=lambda: datetime.datetime.now().isoformat(),
)






llm = ChatOpenAI()
generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm


