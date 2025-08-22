import os


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


def validate_can_access_directory(working_directory, directory_to_validate):
    """
    Validates whether a given path is a directory within the permitted working directory.

    Args:
        working_directory (str): The root directory within which the given path must reside.
        given_path (str): The path to validate.

    Returns:
        tuple:
            - bool: True if the given path is a valid directory within the working directory, False otherwise.
            - str: An error message if validation fails, or an empty string if validation succeeds.
            - str: The absolute path to the given path.
    """
    abs_path_to_directory, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, directory_to_validate
    )

    if not is_path_in_working_dir(working_directory, directory_to_validate):
        return (
            False,
            f'Error: Cannot list "{directory_to_validate}" as it is outside the permitted working directory',
            abs_path_to_directory,
        )
    if not os.path.isdir(abs_path_to_directory):
        print(abs_path_to_directory)
        return (
            False,
            f'Error: "{directory_to_validate}" is not a directory',
            abs_path_to_directory,
        )
    return (True, "", abs_path_to_directory)


def validate_can_read_file(working_directory, file_path):
    """
    Validates if a file exists within a specified working directory and is a regular file.

    Args:
        working_directory (str): The absolute or relative path to the working directory.
        file_name (str): The name of the file to validate.

    Returns:
        tuple: A tuple containing:
            - bool: True if the file is valid, False otherwise.
            - str: An error message if the file is invalid, or an empty string if valid.
            - str: The absolute path to the file.
    """
    abs_path_to_file, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, file_path
    )
    if not abs_path_to_file.startswith(abs_path_to_working_dir):
        return (
            False,
            f'Error: Cannot read "{abs_path_to_file}" as it is outside the permitted working directory',
            abs_path_to_file,
        )
    if not os.path.isfile(abs_path_to_file):
        return (
            False,
            f'Error: File not found or is not a regular file: "{abs_path_to_file}"',
            abs_path_to_file,
        )
    return (True, "", abs_path_to_file)


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
