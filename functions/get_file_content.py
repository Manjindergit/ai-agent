import os

def get_file_content(working_directory, file_path):
    
     try:
        abs_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(abs_working_dir, file_path))
        
        if os.path.commonpath([abs_working_dir, target_path]) != abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" is a directory, not a file'
        
        MAX_CHARS = 10000

        with open(file_path, "r") as f: 
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            
    except Exception as e:
        return f'Error accessing directory "{directory}": {str(e)}'