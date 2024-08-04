from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    :param file_path:
    :return:
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name="mlprojects",
    version='0.0.1',
    author='teja',
    author_email='teja24507@gail.com',
    packages=find_packages(),
    insatll_requires =get_requirements('requirements.txt')
)