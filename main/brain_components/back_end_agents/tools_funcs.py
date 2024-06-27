import ast


def create_backend_files(code: str, filename: str = "default_filename.html"):
    """This function creates Python files for the backend side of the website with the FastAPI code given Python code
    and saves them with the provided filename."""
    with open(filename, 'w') as file:
        file.write(code)
    return f"Python file created: {filename}"


def create_backend_files_wrapper(args):
    """Wrapper function to handle tool calls with multiple arguments. and the tool func is a function that creates
    Python files for the backend side of the website with the FastAPI code given Python code and saves them with the
    provided filename."""
    print(type(args))
    args = ast.literal_eval(args)
    # html, filename = args  # Expect args to be a list with two elements
    print(type(args))
    html = args[0]
    filename = args[1]
    print("this is the filename")
    print(filename)
    return create_backend_files(html, filename)
