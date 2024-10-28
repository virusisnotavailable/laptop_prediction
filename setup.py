from setuptools import find_packages ,setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    '''
    this function will return alll the dependent packages nedded to be installed 
    '''
    HYPHEN_E_DOT = '-e .'

    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        #now remove /n from list
        requirement = [req.replace('\n',"") for req in requirement]
        
        if HYPHEN_E_DOT in requirement:
            requirement.remove(HYPHEN_E_DOT)
    return requirement




setup(
    name = 'laptop_price_prediction',
    version = '0.0.1',
    author = 'Abhinav',
    email  = 'kah23604@gmail.com',
    packages = find_packages(), # folders that i want to make packages so anyone can install and use it directly 
    install_requirements = get_requirement('requirement.txt') # all the oher packages that my model is using to run it like dependecies 
    # for eg if we download pandas it also includes some part of numpy bcs it is dependent on it 
)
