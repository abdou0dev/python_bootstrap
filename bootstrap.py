import os, venv, subprocess, sys
from pathlib import Path

print("*************** BOOTSTRAP ****************")

def create_venv(path, packages=None):
	print(f"Creating environment at {path}")
	venv.create(path, with_pip=True)
	print("environment has been created.")
	if sys.platform == 'win32':
		env = os.path.join(path, 'Scripts', 'python.exe')
	else:
		env = os.path.join(path, 'bin', 'python3')

	if packages:
		try:
			print("Attempting to install packages...")
			subprocess.check_call([env, "-m", "pip", "install"] + packages)
			print("Installation complete.")
		except Exception as err:
			print("There was an error trying to install a package, maybe you misspelled it.")
			print(f"error: {err}")

while True:	
	project_name = input("Enter your project name: ")
	if not project_name:
		print("You must provide a name.")
	else:
		print("Creating directory...")
		project_path = Path(project_name)
		venv_path = Path(f"{project_path}/.venv")
		if project_path.exists():
			print("Project already exists.")
			sys.exit()
		venv_path.mkdir(parents=True)
		packages = input("Enter the packages you want to install seperated by a single space or leave empty: ")
			
		if packages:
			packages = packages.split(' ')
			print(packages)

		create_venv(venv_path, packages)
		break