import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    
    abs_working_dir = os.path.abspath(working_directory)
    
    full_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
    if os.path.commonpath([abs_working_dir, full_path]) != abs_working_dir:
        return f'Error: Cannot run "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_path):
        return f'Error: File "{file_path}" does not exist in working directory "{working_directory}".'
    if os.path.isdir(full_path):
        return f'Error: "{file_path}" is a directory, not a file.'
    if not file_path.endswith('.py'):
        return f'Error: File "{file_path}" is not a Python (.py) file.'
    
    try:
        command = ["python", full_path]
        if args:
            command.extend(args)
            print(f"It came here with args: {args}")
        
        result = subprocess.run(command, capture_output=True, text=True, cwd=abs_working_dir, timeout=30)
        output = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        return "\n".join(output)      

    except Exception as e:
        return f'Error executing file "{file_path}": {str(e)}'
    
schema_run_file_content = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file relative to the working directory and captures its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="File path to execute, relative to the working directory",
            ),
        },
    ),
)