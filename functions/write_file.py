import os
from functions.shared import (
    is_path_in_working_dir,
    get_full_and_absolute_paths,
)


def write_file(working_directory, file_path, content):
    abs_path_to_file, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, file_path
    )
    if not is_path_in_working_dir(working_directory, file_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(abs_path_to_file, "w") as file:
            file.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error now here: {e}"
