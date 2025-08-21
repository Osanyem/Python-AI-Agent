import os


def validate_directory(working_directory, directory):
    path_to_directory = os.path.abspath(os.path.join(working_directory, directory))
    abs_path = os.path.abspath(working_directory)
    if not path_to_directory.startswith(abs_path):
        return (
            False,
            f'Error: Cannot list "{directory}" as it is outside the permitted working directory',
            path_to_directory,
        )
    if not os.path.isdir(path_to_directory):
        print(path_to_directory)
        return (False, f'Error: "{directory}" is not a directory', path_to_directory)
    return (True, "", path_to_directory)


def validate_file(working_directory, file_path):
    path_to_file = os.path.abspath(os.path.join(working_directory, file_path))
    abs_path = os.path.abspath(working_directory)
    if not path_to_file.startswith(abs_path):
        return (
            False,
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory',
            path_to_file,
        )
    if not os.path.isfile(path_to_file):
        return (
            False,
            f'Error: File not found or is not a regular file: "{file_path}"',
            path_to_file,
        )
    return (True, "", path_to_file)
