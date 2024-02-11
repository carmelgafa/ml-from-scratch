'''
script to create project folder structure, virtual 
environment and loads required libraries
'''
import os

def create_environment(project_name:str, requirements:list)->None:
    '''
    creates a new virtual environment with project folder structure
    '''

    # create file setup.py
    with open(file="setup.py", mode="w", encoding="utf-8") as f:
        f.write("from setuptools import setup, find_packages\n")
        f.write("setup(name='"+project_name+"', version='1.0', packages=find_packages())")

    # create project folder
    os.mkdir(project_name)
    os.mkdir(project_name+"/.build")
    os.mkdir(project_name+"/.config")
    os.mkdir(project_name+"/dep")
    os.mkdir(project_name+"/doc")
    os.mkdir(project_name+"/res")
    os.mkdir(project_name+"/samples")
    os.mkdir(project_name+"/src")
    os.mkdir(project_name+"/test")
    os.mkdir(project_name+"/tools")

    # create __init__.py in project folder
    with open(file=project_name+"/__init__.py", mode="w", encoding="utf-8") as f:
        f.write("")

    # create requirements.txt
    with open("requirements.txt", mode="w", encoding="utf-8") as f:
        for req in requirements:
            f.write(req+"\n")

    # create README.md
    with open("README.md", mode="w", encoding="utf-8") as f:
        f.write(f"# {project_name}\n")

    # create virtual environment
    os.system("python -m venv venv")

    # create activate.bat
    with open("activate.bat", mode="w", encoding="utf-8") as f:
        f.write("venv\\Scripts\\activate.bat\n")

    # create deactivate.bat
    with open("deactivate.bat", mode="w", encoding="utf-8") as f:
        f.write("venv\\Scripts\\deactivate.bat\n")

    # run activate.bat
    os.system('''
              activate.bat & pip install -r requirements.txt & pip install -e .
              ''')

    # create gitignore file and add venv folder
    with open(".gitignore", mode="w", encoding="utf-8") as f:
        f.write("venv\n")


if __name__ == '__main__':
    create_environment('ml_algorithms', ['numpy', 'pandas', 'matplotlib'])
    