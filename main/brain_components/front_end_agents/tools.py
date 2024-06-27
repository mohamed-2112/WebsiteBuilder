from langchain_core.tools import Tool
from .tools_funcs import create_html_files_wrapper

USER_INTERFACE_AGENT_TOOLS = [
    Tool(
        name="HTML files Creator",
        func=create_html_files_wrapper,
        description="""Tool to transform natural language to HTML and create HTML files. Accepts a list and only a list composed of the HTML content and a 
        filename."""
    ),
]
