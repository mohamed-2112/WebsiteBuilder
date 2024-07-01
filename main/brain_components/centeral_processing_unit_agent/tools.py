from langchain_core.tools import Tool
from main.brain_components.back_end_agents.back_end_agent import BackendAgent
from main.brain_components.front_end_agents.user_interface_agent import UIAgent


CPU_AGENT = [
    Tool(
        name="BackEnd Agent",
        func=BackendAgent.back_end_agent_wrapper,
        description="""Useful when you need to transform natural language to FastAPI code with Python and then save the file
        returning the status of weather the file has been created or not.
        DOES NOT ACCEPT CODE AS INPUT."""
    ),
    Tool(
        name="FrontEnd Agent",
        func=UIAgent.front_end_agent_wrapper,
        description="""Useful when you need to transform natural language to html code then save the file
        returning the status of weather the file has been created or not.
        DOES NOT ACCEPT CODE AS INPUT."""
    ),
]
