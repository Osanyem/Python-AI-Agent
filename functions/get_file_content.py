import os
from config import CHAR_LIMIT
from .common_functions import validate_directory, validate_file


def get_file_content(working_directory, file_path):
    is_valid, validation_string, path_to_file = validate_file(
        working_directory, file_path
    )
    if not is_valid:
        return validation_string

    try:
        with open(path_to_file, "r") as file:
            file_text = file.read()

            if len(file_text) > CHAR_LIMIT:
                file_text = (
                    file_text[:CHAR_LIMIT]
                    + f'[...File "{file_path}" truncated at 10000 characters]'
                )
            return file_text
    except FileNotFoundError as e:
        return f"Error: The specified file was not found. {e}"
    except Exception as e:
        return f"Error: An error occurred: {e}"
