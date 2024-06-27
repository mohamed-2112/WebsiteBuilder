from langchain import hub

PROMPT_CODE_INTERPRETER = hub.pull("sibrash/open-interpreter-system")

PROMPT_INSTRUCTION = """You are an agent designed to write and implement html code to create html files for a website, keeping a beautiful and modern design in mind. Use a responsive design suitable for both mobile and desktop views.
        You have access to a tool to use to just create the html files but you will need to provide the html code.
        If you get an error, debug your code and try again.
        Only use the output of your code as the final result.
        You might know the answer without tracing and reviewing the code, but you should still trace the review the code make sure.
        If it does not seem like you can write code, just return "I don't know" as the answer.
        """

REACT_AGENT_PROMPT = hub.pull("langchain-ai/react-agent-template")

REACT_AGENT_PROMPT_INPUT = {
    "input": """I need you to generate and save in the current working directory HTML code for a personal website, keeping a beautiful and modern design in mind. Use a responsive design suitable for both mobile and desktop views.

1. The first page, should focus on the personal life of the person. It should include:
   - A large header with the person's name and a background image related to hobbies or personal life.
   - A navigation bar
   - Sections for Biography, Hobbies, and a Photo Gallery.
   - Footer with social media links.

Please ensure the page use harmonious color schemes and are visually appealing. Include CSS for styling and make sure the HTML is ready to be viewed in a browser.
"""
}

PROMPT_INSTRUCTION_FASTAPI = """You are an AI agent designed to write Python code for FastAPI applications. Generate 
the code necessary to create an API with FastAPI. You have access to a tool to use to just create the Python files 
but you will need to provide the code. Ensure the code is syntactically correct and ready to run. If you find an 
error, review your code and try again. You might know the answer without tracing and reviewing the code, 
but you should still trace the review the code make sure. If it does not seem like you can write code, just return "I 
don't know" as the answer."""

REACT_AGENT_PROMPT_FASTAPI_input = {
    "input": "Generate FastAPI code for a simple application that has one route '/hello' which returns 'Hello, "
             "World!' when accessed."
}

