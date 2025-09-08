import os
from config import MAX_FILE_SIZE
from google.genai import types


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_abs = os.path.abspath(working_directory)
        
        if not full_path.startswith(working_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content) > MAX_FILE_SIZE:
            content = content[:MAX_FILE_SIZE] + f'[...File "{file_path}" truncated at {MAX_FILE_SIZE} characters]'
        
        return content
    
    except Exception as e:
        return f"Error: {str(e)}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads and returns the contents of a file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)