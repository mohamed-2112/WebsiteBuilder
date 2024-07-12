from langchain_core.tools import Tool
from main.brain_components.back_end_agents.tools_funcs import create_backend_files_wrapper

BACKEND_AGENT_TOOLS = [
    Tool(
        name="Python files Creator",
        func=create_backend_files_wrapper,
        description="""Tool to transform natural language to Python and create FastAPI Python code and create Python 
        files. Accepts a list composed of the code and a filename."""
    ),
]
