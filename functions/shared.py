import os
from google.genai import types


def get_full_and_absolute_paths(working_directory, given_path):
    """
    Computes the absolute paths of a given path and the working directory.

    Args:
        working_directory (str): The base directory to resolve the paths from.
        given_path (str): The relative or absolute path to be resolved.

    Returns:
        tuple: A tuple containing:
            - abs_path_to_given_path (str): The absolute path to the given path.
            - abs_path_to_working_dir (str): The absolute path to the working directory.
    """
    abs_path_to_given_path = os.path.abspath(
        os.path.join(working_directory, given_path)
    )
    abs_path_to_working_dir = os.path.abspath(working_directory)
    return (abs_path_to_given_path, abs_path_to_working_dir)


def is_path_in_working_dir(working_directory, given_path):
    """
    Checks if a given path is within the specified working directory.

    Args:
        working_directory (str): The absolute path to the working directory.
        given_path (str): The path to check, which can be relative or absolute.

    Returns:
        bool: True if the given path is within the working directory, False otherwise.

    Example:
        >>> path_in_working_dir("/home/user/projects", "subdir/file.txt")
        True  # The given path resolves to a location inside the working directory.
        >>> path_in_working_dir("/home/user/projects", "../outside/file.txt")
        False  # The given path resolves to a location outside the working directory.
    """
    abs_path_to_given_path, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, given_path
    )
    return abs_path_to_given_path.startswith(abs_path_to_working_dir)


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file and returns the output, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional command line arguments to pass to the Python file.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
