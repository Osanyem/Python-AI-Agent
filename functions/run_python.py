import os
import subprocess
from functions.shared import (
    is_path_in_working_dir,
    get_full_and_absolute_paths,
)


def run_python_file(working_directory, file_path, args=[]):
    abs_path_to_file, abs_path_to_working_dir = get_full_and_absolute_paths(
        working_directory, file_path
    )
    if not is_path_in_working_dir(working_directory, file_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_path_to_file):
        return f'Error: File "{file_path}" not found.'
    if not abs_path_to_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        completed_process = subprocess.run(
            ["python", abs_path_to_file] + args,
            timeout=30,
            capture_output=True,
            text=True,
            cwd=abs_path_to_working_dir,
        )
        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()
        output = []

        if stdout:
            output.append(f"STDOUT: {stdout}")
        if stderr:
            output.append(f"STDERR: {stderr}")
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")
        if not output:
            return "No output produced."
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"
