# AI-Agent

An AI-powered coding assistant that can interact with your file system to perform various development tasks. This agent uses Google's Gemini API to understand user requests and execute appropriate file operations.

## Features

- **File System Interaction**: List files and directories with size information
- **File Content Reading**: Read and display contents of files (with size limits)
- **Code Execution**: Run Python files with optional arguments
- **File Writing**: Create or overwrite files with new content
- **AI-Powered**: Uses Google's Gemini API for intelligent task processing

## Project Structure

```
AI-Agent/
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── calculator/
│   ├── pkg/
│   ├── main.py
│   ├── script.py
│   ├── tests.py
│   ├── lorem.txt
│   └── test.txt
├── main.py
├── config.py
├── tests.py
├── pyproject.toml
└── .env
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/itsaahsan/AI-Agent.git
   cd AI-Agent
   ```

2. Install dependencies using uv (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install google-genai python-dotenv
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your Google Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

Run the AI agent with a prompt:
```bash
python main.py "List all files in the calculator directory"
```

For verbose output:
```bash
python main.py "Run the calculator tests" --verbose
```

## How It Works

The AI agent uses Google's Gemini API to understand user requests and map them to appropriate file operations:

1. **File Listing**: `get_files_info()` - Lists files in a directory with size information
2. **File Reading**: `get_file_content()` - Reads and returns the content of a specified file (limited to 10KB by default)
3. **Code Execution**: `run_python_file()` - Executes Python files with optional arguments
4. **File Writing**: `write_file()` - Creates or overwrites files with new content

## Example Prompts

- "List all files in the calculator directory"
- "Read the content of main.py"
- "Run the tests.py file"
- "Create a new file called example.txt with the content 'Hello, World!'"

## Configuration

- The agent is configured to work within a specified working directory (currently set to `./calculator`) for security reasons. You can modify this in the `main.py` file.
- File reading is limited to 10KB by default (configurable in `config.py`)

## Dependencies

- Python 3.12+
- google-genai 1.12.1
- python-dotenv 1.1.0

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License.