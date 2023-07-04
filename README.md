# repository-analyser
A project to analyse GitHub repositories.

## Setup Instructions
- Clone the repository.
- Ensure you have ```Python3``` installed on your machine.
- Install ```PyGithub``` on your machine, run ```pip3 install PyGithub```.
- Update the ```access_token``` value in ```repo.py``` and ```org.py``` to your GitHub PAT.
- Update the ```organization_name``` value in ```repo.py``` and ```org.py``` to your GitHub organisation's name.
- Update the ```repo_name``` value in ```repo.py``` to your GitHub repo's name.

## Example Usage
- Run: ```python3 repo.py``` to analyse a specific repository.
- Run: ```python3 org.py``` to analyse a all repositories on your GitHub organisation.
