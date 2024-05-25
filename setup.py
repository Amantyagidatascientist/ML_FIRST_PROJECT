from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->list[str]:
    'this function will return the list of requirement'
    Hypen_e_dot='-e .'
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n'," ") for req in requirements]
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements


setup(
    name='ml_first_project',
    version='0.0.1',
    author='Aman Tyagi',
    author_email='tyagiaman3558@gmail.com',
    install_requires=get_requirements('requirements.txt')
)