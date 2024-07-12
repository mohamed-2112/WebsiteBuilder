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

REACT_AGENT_PROMPT_FASTAPI_INPUT = {
    "input": "Generate FastAPI code for a simple application that has one route '/hello' which returns 'Hello, "
             "World!' when accessed."
             "and DON'T NAME THE FILE main.py"
}

PROMPT_INSTRUCTION_CPU = """You are an AI agent designed to act as the brain of the software that can generate 
Websites applications. You have access to several tools to use to create the website and those tools are agents that 
can do different tasks. but you will need to choose what agent you will envoke and in what sequence or order. and you 
can invoke or use a tool multiple times until you reach your goal and if something goes wrong review the result and 
try again. You might know the answer without using the tools, but you should still use the specialized tools. If it 
does not seem like you can do it, just return "I don't know" as the answer."""


REACT_AGENT_PROMPT_CPU_INPUT = {
    "input": "Generate a very simple application that basically have one web page and that is all "
             " the application can just have one route '/' which returns 'welcome to the first application,"
             "and DON'T NAME ANY FILE BY main "
}



"""
I should add something like 

"""
test_prompt = """
{instructions}

TOOLS:
------

You have access to the following tools:

{tools}

To use a tool, please use the following format:

```
Thought: Do I need to use a tool? Yes
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
```

When you have a response to say to the Human, or if you do not need to use a tool, you MUST use the format:

```
Thought: Do I need to use a tool? No
Final Answer: [your response here]
```

Begin!

Previous conversation history:
{chat_history}

New input: {input}
{agent_scratchpad}

"""
