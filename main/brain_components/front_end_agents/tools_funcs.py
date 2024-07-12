import ast


def create_html_files(html: str, filename: str = "default_filename.html"):
    """This function creates HTML files from the given HTML code and saves them with the provided filename."""
    with open(filename, 'w') as file:
        file.write(html)
    return f"HTML file created: {filename}"


def create_html_files_wrapper(args):
    """Wrapper function to handle tool calls with multiple arguments."""
    print(type(args))
    args = ast.literal_eval(args)
    # html, filename = args  # Expect args to be a list with two elements
    print(type(args))
    html = args[0]
    filename = args[1]
    print("this is the filename")
    print(filename)
    return create_html_files(html, filename)
