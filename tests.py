# from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file


def test():
    print("=== Testing function calls with natural language prompts ===\n")

    # Test prompts that would trigger get_file_content
    print("Prompt: 'read the contents of main.py'")
    result = get_file_content("main.py")
    print(f"get_file_content({{'file_path': 'main.py'}})")
    print(f"Result: \n{result}\n")

    print("Prompt: 'show me what's in config.json'")
    result = get_file_content("config.json")
    print(f"get_file_content({{'file_path': 'config.json'}})")
    print(f"Result: \n{result}\n")

    # Test prompts that would trigger write_file
    print("Prompt: 'write hello world to greeting.txt'")
    result = write_file("greeting.txt", "Hello, World!")
    print(f"write_file({{'file_path': 'greeting.txt', 'content': 'Hello, World!'}})")
    print(f"Result: \n{result}\n")

    print("Prompt: 'create a file called notes.md with some sample content'")
    result = write_file("notes.md", "# My Notes\n\nThis is a sample markdown file.")
    print(
        f"write_file({{'file_path': 'notes.md', 'content': '# My Notes\\n\\nThis is a sample markdown file.'}})"
    )
    print(f"Result: \n{result}\n")

    # Test prompts that would trigger run_python_file
    print("Prompt: 'run main.py'")
    result = run_python_file("calculator", "main.py")
    print(f"run_python_file({{'directory': 'calculator', 'file_path': 'main.py'}})")
    print(f"Result: \n{result}\n")

    print("Prompt: 'execute test.py with input data'")
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(
        f"run_python_file({{'directory': 'calculator', 'file_path': 'main.py', 'input_lines': ['3 + 5']}})"
    )
    print(f"Result: \n{result}\n")

    print("Prompt: 'run the script tests.py'")
    result = run_python_file("calculator", "tests.py")
    print(f"run_python_file({{'directory': 'calculator', 'file_path': 'tests.py'}})")
    print(f"Result: \n{result}\n")

    # Test prompts that would trigger get_files_info (commented out since import is commented)
    print("Prompt: 'list the contents of the src directory'")
    print("get_files_info({'directory': 'src'})")
    print("(Function not imported/available)\n")

    print("Prompt: 'show me all files in the current folder'")
    print("get_files_info({'directory': '.'})")
    print("(Function not imported/available)\n")


if __name__ == "__main__":
    test()
