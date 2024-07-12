from main.brain_components.back_end_agents.tools import BACKEND_AGENT_TOOLS
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from main.brain_components.prompts import REACT_AGENT_PROMPT, REACT_AGENT_PROMPT_FASTAPI_INPUT, \
    PROMPT_INSTRUCTION_FASTAPI
from main.brain_components.agents_interface import Agents


class BackendAgent(Agents):
    def __init__(self):
        super().__init__()
        self.tools = BACKEND_AGENT_TOOLS

    @classmethod
    def back_end_agent_wrapper(cls, prompt):
        """
        This method is a wrapper method to invoke the backend agent which need a prompt to instruct it to
        generate a FastAPI Python code which can be saved in the working directory
        :param prompt: prompt for the back end agent (instruction on what it will generate)
        :return: dict[str, Any] it will return the status on weather it successfully created the file or not
        """
        backend_instance = cls()
        back_end_agent_executor = backend_instance.agent_init(backend_instance.tools)
        return back_end_agent_executor.invoke(input=prompt)
