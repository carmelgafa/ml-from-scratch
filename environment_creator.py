import os

def create_environment(project_name:str, requirements:list)->None:
    # create file setup.py
    with open("setup.py", "w") as f:
        f.write("from setuptools import setup, find_packages\n")
        f.write("setup(name='"+project_name+"', version='1.0', packages=find_packages())")

    # create project folder
    os.mkdir(project_name)
    
    # create __init__.py in project folder
    with open(project_name+"/__init__.py", "w") as f:
        f.write("")
        
    # create requirements.txt
    with open("requirements.txt", "w") as f:
        for req in requirements:
            f.write(req+"\n")
        
    # create README.md
    with open("README.md", "w") as f:
        f.write(f"# {project_name}\n")

    # create virtual environment
    os.system("python -m venv venv")

    # create activate.bat
    with open("activate.bat", "w") as f:
        f.write("venv\\Scripts\\activate.bat\n")

    # create deactivate.bat
    with open("deactivate.bat", "w") as f:
        f.write("venv\\Scripts\\deactivate.bat\n")

    # run activate.bat
    os.system('''
              activate.bat & pip install -r requirements.txt & pip install -e .
              ''')

    # create gitignore file and add venv folder
    with open(".gitignore", "w") as f:
        f.write("venv\n")



if __name__ == '__main__':
    create_environment('ml_algorithms', ['numpy', 'pandas', 'mathplotlib'])