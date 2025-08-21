import os


def get_files_info(working_directory, directory="."):
    path_to_directory = os.path.abspath(os.path.join(working_directory, directory))
    abs_path = os.path.abspath(working_directory)
    if not path_to_directory.startswith(abs_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(path_to_directory):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(path_to_directory):
            file_path = os.path.join(path_to_directory, filename)
            file_info = f"{filename}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}"
            files_info.append(file_info)
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
