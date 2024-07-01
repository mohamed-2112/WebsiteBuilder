from main.brain_components.centeral_processing_unit_agent.tools import CPU_AGENT
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from main.brain_components.prompts import REACT_AGENT_PROMPT, REACT_AGENT_PROMPT_FASTAPI_INPUT, \
    PROMPT_INSTRUCTION_FASTAPI


class CPUAgent:
    def __init__(self):
        self.tools = CPU_AGENT

    def agent_init(self):
        llm = ChatOpenAI(temperature=0.9, model="gpt-4-turbo")
        prompt = REACT_AGENT_PROMPT.partial(instructions=PROMPT_INSTRUCTION_FASTAPI)
        print(prompt)
        fastapi_agent = create_react_agent(prompt=prompt, llm=llm, tools=self.tools)
        fastapi_agent_executor = AgentExecutor(agent=fastapi_agent, tools=self.tools, verbose=True)
        return fastapi_agent_executor

    def agent_trials(self):
        agent_executor = self.agent_init()
        res = agent_executor.invoke(input=REACT_AGENT_PROMPT_FASTAPI_INPUT)
        print(res)
