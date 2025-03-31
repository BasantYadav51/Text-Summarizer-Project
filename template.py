import os  
from pathlib import Path  
import logging 


logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s') 
project_name = "textSummarization"  # Defining project name

# List of files to be created
list_of_files = [
    ".github/workflows/.gitkeep",  # Keeping empty directories in version control
    f"src/{project_name}/__init__.py",  # Fixed incorrect `init` filename (_init_ -> __init__)
    f"src/{project_name}/component/__init__.py",  # Fixed incorrect `init` filename
    f"src/{project_name}/utils/__init__.py",  # Fixed incorrect `init` filename
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",  # Fixed typo in filename (cofiguration -> configuration)
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constant/__init__.py",  # Fixed typo in folder name (constent -> constant)
    "config/config.yaml",
    "params.yaml",  # Fixed typo in filename (parmas -> params)
    "app.py",
    "main.py",
    "Dockerfile",  # Fixed typo in filename (Docker.file -> Dockerfile)
    "requirements.txt",  # Fixed typo in filename (requirment.txt -> requirements.txt)
    "setup.py",
    "research.ipynb",
]

# Creating files and directories
for file_path in list_of_files:
    filepath = Path(file_path)  # Corrected variable name
    filedir, filename = os.path.split(filepath)  # Fixed syntax errors

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # Fixed function call syntax
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Creating an empty file
        logging.info(f"Creating empty file: {filepath}")  # Fixed f-string formatting
    else:
        logging.info(f"{filename} already exists")
