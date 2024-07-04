from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requiremets
    '''
    requiremetns = []
    with open(file_path) as file_obj:
        requiremetns = file_obj.readlines()
        requiremetns = [req.replace("\n","") for req in requiremetns]
        if HYPHEN_E_DOT in requiremetns:
            requiremetns.remove(HYPHEN_E_DOT)


setup(
    name="student performance indicator",
    version="0.0.1",
    author="Yassine",
    author_email="yassine@gmail.com",
    packages= find_packages(),
    install_requires= get_requirements("requirements.txt")
)