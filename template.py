import os
from pathlib import Path
import logging
my_project='ml_project'
list_of_file=[f"src/{my_project}/__init__.py",
              f"src/{my_project}/components/__init__.py",
              f"src/{my_project}/components/data_ingestion.py",
              f"src/{my_project}/components/data_tranformation.py",
              f"src/{my_project}/components/model_tranier.py",
              f"src/{my_project}/components/model_monitering.py",
              f"src/{my_project}/pipeline/__init__.py",
              f"src/{my_project}/pipeline/training_pipeline.py",
              f"src/{my_project}/pipeline/predication.py",
              f"src/{my_project}/logger.py",
              f"src/{my_project}/exception.py"
              ]
for filepath in list_of_file:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file{filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath))==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating empty file {filepath}")
    else:
        logging.info(f"{filename} is already exists")
    