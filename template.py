import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format='[%(asctime)s]: %(message)s:')

file_list = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py"
]

for filepath in file_list:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)
    
    if file_dir!="":
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        logging.info(f"Creating directory; {file_dir} for the file: {file_name}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")