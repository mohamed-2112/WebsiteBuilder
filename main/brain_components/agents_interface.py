from abc import ABC, abstractmethod
from main.brain_components.front_end_agents.tools import USER_INTERFACE_AGENT_TOOLS
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from main.brain_components.prompts import REACT_AGENT_PROMPT, PROMPT_INSTRUCTION
from main.utils.utils import override


class Agents(ABC):
    def __init__(self):
        pass

    def agent_init(self, tools):
        llm = ChatOpenAI(temperature=0.9, model="gpt-4-turbo")
        prompt = REACT_AGENT_PROMPT.partial(instructions=PROMPT_INSTRUCTION)
        html_agent = create_react_agent(prompt=prompt, llm=llm, tools=tools)
        html_agent_executor = AgentExecutor(agent=html_agent, tools=tools, verbose=True)
        return html_agent_executor

    @classmethod
    def agent_wrapper(cls, prompt):
        pass
