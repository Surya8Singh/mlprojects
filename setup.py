from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """Reads requirements from a file and returns a cleaned list."""
    with open(file_path) as f:
        requirements = f.readlines()
    # Remove whitespaces and trailing newlines
    requirements = [req.strip() for req in requirements]

    # Handle potential '-e .' marker for editable installs
    if '-e.' in requirements:
        requirements.remove('-e.')

    return requirements

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Surya',
    author_email='suryapratap.singh08@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
