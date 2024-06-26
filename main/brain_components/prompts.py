from langchain import hub

PROMPT_CODE_INTERPRETER = hub.pull("sibrash/open-interpreter-system")

PROMPT_INSTRUCTION = """You are an agent designed to write and implement html code to create html files for a website, keeping a beautiful and modern design in mind. Use a responsive design suitable for both mobile and desktop views.
        You have access to many tools to use to generate the files.
        If you get an error, debug your code and try again.
        Only use the output of your code as the final result.
        You might know the answer without tracing and reviewing the code, but you should still trace the review the code make sure.
        If it does not seem like you can write code, just return "I don't know" as the answer.
        """

REACT_AGENT_PROMPT = hub.pull("langchain-ai/react-agent-template")

REACT_AGENT_PROMPT_INPUT = {
    "input": """I need you to generate and save in the current working directory two HTML pages for a personal website, keeping a beautiful and modern design in mind. Use a responsive design suitable for both mobile and desktop views.

1. The first page, named "personal_life.html", should focus on the personal life of the person. It should include:
   - A large header with the person's name and a background image related to hobbies or personal life.
   - A navigation bar linking to the second page.
   - Sections for Biography, Hobbies, and a Photo Gallery.
   - Footer with social media links.

2. The second page, named "career.html", should detail the person's career. It should contain:
   - A professional header with the person's name and a background image of a corporate setting.
   - A navigation bar linking back to the first page.
   - Sections for Work Experience, Education, and Skills.
   - A contact form at the bottom for professional inquiries.
   - A footer similar to the first page but with a LinkedIn profile link.

Please ensure both pages use harmonious color schemes and are visually appealing. Include CSS for styling and make sure the HTML is ready to be viewed in a browser.
"""
}
print(REACT_AGENT_PROMPT.template)
