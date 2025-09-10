# AI Agent

This is a small python project which is a toy version of [Claude Code](https://www.anthropic.com/claude-code).
This is a guided project on [Boot.dev](https://www.boot.dev).

:exclamation: **_This Agent can run arbitrary python code. It is for learning purposes only. Use at your own risk._**

## Learning Goals

1. Introduce multi-directory Python projects
2. Understand how modern AI tools work under the hood
3. Practice my Python and functional programming skills

## Prerequisites

- Python 3.7 or higher
- A Google Gemini API key

## Setup

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd ai-agent-main
   ```

2. **Create a virtual environment (recommended)**
   
   On macOS/Linux, you may encounter an "externally-managed-environment" error when installing packages. To avoid this, create a virtual environment:
   
   ```bash
   python3 -m venv ai-agent-env
   source ai-agent-env/bin/activate  # On macOS/Linux
   # or on Windows: ai-agent-env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   **Alternative installation methods if you get externally-managed-environment error:**
   
   - **Option 1: Use pipx** (install pipx first if you don't have it)
     ```bash
     brew install pipx  # On macOS
     pipx install --editable .
     ```
   
   - **Option 2: Use --break-system-packages flag** (not recommended)
     ```bash
     pip install -r requirements.txt --break-system-packages
     ```

4. **Set up your Gemini API key**
   
   Create a `.env` file in the root directory and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
   
   You can obtain a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## How to Run

The AI agent accepts natural language prompts and can perform various operations on the calculator project in the `calculator/` directory.

### Basic Usage

```bash
python main.py "your prompt here"
```

### With Verbose Output

For detailed logging and debugging information:

```bash
python main.py "your prompt here" --verbose
```

### Example Commands

Here are some example prompts you can try:

- **Code analysis**: `python main.py "Analyze the calculator code and tell me what it does"`
- **Bug fixing**: `python main.py "How do I fix the calculator?"`
- **Code modification**: `python main.py "Add a multiplication function to the calculator"`
- **File exploration**: `python main.py "What files are in the calculator directory?"`
- **Testing**: `python main.py "Run the tests for the calculator"`

## Available Functions

The AI agent has access to the following functions:

- **get_files_info**: List files and directories in the calculator project
- **get_file_content**: Read the contents of specific files
- **write_file**: Create or modify files
- **run_python_file**: Execute Python files and see their output

## Project Structure

```
ai-agent-main/
├── main.py              # Main entry point
├── call_function.py     # Function calling logic
├── prompts.py           # System prompts for the AI
├── requirements.txt     # Python dependencies
├── functions/           # Available functions for the AI agent
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
└── calculator/          # Target project for the AI agent
    ├── main.py
    ├── tests.py
    └── pkg/
        ├── calculator.py
        └── render.py
```

## Safety Note

This agent can execute arbitrary Python code and modify files. Always review the changes it suggests before accepting them, especially in production environments.

## Troubleshooting

### externally-managed-environment Error

If you get an "externally-managed-environment" error when installing packages:

1. **Best solution**: Use a virtual environment (see Setup step 2)
2. **Alternative**: Install with `--break-system-packages` flag (not recommended for system stability)
3. **For macOS users**: Consider using `pipx` or `conda` for package management

### API Key Issues

- Make sure your `.env` file is in the root directory
- Ensure your Gemini API key is valid and has the necessary permissions
- Check that the `.env` file format is correct: `GEMINI_API_KEY=your_key_here` (no quotes)

### Permission Errors

If you encounter permission errors when writing files:
- Make sure you have write permissions in the project directory
- On Unix systems, you may need to adjust file permissions: `chmod 755 .`
