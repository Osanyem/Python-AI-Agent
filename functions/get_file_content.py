import os
from config import CHAR_LIMIT
from .shared_functions import (
    get_full_and_absolute_paths,
    is_path_in_working_dir,
)


def get_file_content(working_directory, file_path):

    abs_path_to_file, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, file_path
    )

    if not is_path_in_working_dir(working_directory, file_path):
        return f'Error: Cannot read "{abs_path_to_file}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path_to_file):
        return f'Error: File not found or is not a regular file: "{abs_path_to_file}"'

    try:
        with open(abs_path_to_file, "r") as file:
            file_text = file.read()

            if len(file_text) > CHAR_LIMIT:
                file_text = (
                    file_text[:CHAR_LIMIT]
                    + f'[...File "{file_path}" truncated at 10000 characters]'
                )
            return file_text
    except FileNotFoundError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
