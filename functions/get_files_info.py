import os
from .shared import (
    get_full_and_absolute_paths,
    is_path_in_working_dir,
)


def get_files_info(working_directory, directory="."):

    abs_path_to_directory, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, directory
    )

    if not is_path_in_working_dir(working_directory, directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_path_to_directory):
        print(abs_path_to_directory)
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(abs_path_to_working_dir):
            file_path = os.path.join(abs_path_to_working_dir, filename)
            file_info = f"{filename}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
            files_info.append(file_info)
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
