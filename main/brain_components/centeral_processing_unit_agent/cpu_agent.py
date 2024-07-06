from main.brain_components.centeral_processing_unit_agent.tools import CPU_AGENT_TOOLS
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from main.brain_components.prompts import REACT_AGENT_PROMPT, REACT_AGENT_PROMPT_CPU_INPUT, \
    PROMPT_INSTRUCTION_CPU
from main.brain_components.agents_interface import Agents


class CPUAgent(Agents):
    def __init__(self):
        super().__init__()
        self.tools = CPU_AGENT_TOOLS

    def agent_trials(self):
        agent_executor = self.agent_init(CPU_AGENT_TOOLS)
        res = agent_executor.invoke(input=REACT_AGENT_PROMPT_CPU_INPUT)
        print(res)
