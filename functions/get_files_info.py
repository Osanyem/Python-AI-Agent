import os
from .common_functions import validate_directory


def get_files_info(working_directory, directory="."):
    is_valid_dir, validation_string, path_to_directory = validate_directory(
        working_directory, directory
    )
    if not is_valid_dir:
        return validation_string
    try:
        files_info = []
        for filename in os.listdir(path_to_directory):
            file_path = os.path.join(path_to_directory, filename)
            file_info = f"{filename}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
            files_info.append(file_info)
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
