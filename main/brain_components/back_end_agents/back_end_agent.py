from main.brain_components.back_end_agents.tools import BACKEND_AGENT_TOOLS
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from main.brain_components.prompts import REACT_AGENT_PROMPT, REACT_AGENT_PROMPT_FASTAPI_INPUT, PROMPT_INSTRUCTION_FASTAPI


class BackendAgent:
    def __init__(self):
        self.tools = BACKEND_AGENT_TOOLS

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

    @classmethod
    def back_end_agent_wrapper(cls, prompt):
        """
        This method is a wrapper method to invoke the backend agent which need a prompt to instruct it to
        generate a FastAPI Python code which can be saved in the working directory
        :param prompt: prompt for the back end agent (instruction on what it will generate)
        :return: dict[str, Any] it will return the status on weather it successfully created the file or not
        """
        backend_instance = cls()
        back_end_agent_executor = backend_instance.agent_init()
        return  back_end_agent_executor.invoke(input=prompt)
