from main.brain_components.front_end_agents.tools import USER_INTERFACE_AGENT_TOOLS
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from main.brain_components.prompts import REACT_AGENT_PROMPT, REACT_AGENT_PROMPT_INPUT, PROMPT_INSTRUCTION


class UIAgent:
    def __init__(self):
        self.tools = USER_INTERFACE_AGENT_TOOLS

    def agent_init(self):
        llm = ChatOpenAI(temperature=0.9, model="gpt-4-turbo")
        prompt = REACT_AGENT_PROMPT.partial(instructions=PROMPT_INSTRUCTION)
        print(prompt)
        html_agent = create_react_agent(prompt=prompt, llm=llm, tools=self.tools)
        html_agent_executor = AgentExecutor(agent=html_agent, tools=self.tools, verbose=True)
        return html_agent_executor

    def agent_trials(self):
        agent_executor = self.agent_init()
        res = agent_executor.invoke(input=REACT_AGENT_PROMPT_INPUT)
        print(res)

    @classmethod
    def front_end_agent_wrapper(cls, prompt):
        """
        This method is a wrapper method to invoke the frontend agent which need a prompt to instruct it to
        generate an html Python code which can be saved in the working directory
        :param prompt: prompt for the front end agent (instruction on what it will generate)
        :return: dict[str, Any] it will return the status on weather it successfully created the file or not
        """
        front_end_instance = cls()
        front_end_agent_executor = front_end_instance.agent_init()
        return front_end_agent_executor.invoke(input=prompt)
