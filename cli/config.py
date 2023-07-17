import os
import json
import glob
import subprocess
import datetime
import pytz

class Config:
    
    #
    # Colored output
    #
    
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    
    #
    # List of repositories to analyze
    #

    repos = [
        "lp-home",
        "lp-home-web"
    ]

    #
    # Functions
    #

    # Clone the repository and change directory
    def clone_repo(repo_name):
        try:
            os.system(f"git clone https://github.com/HT2-Labs/{repo_name}.git")
            os.chdir(repo_name)
        except:
            print(f'Failed to clone the repository {repo_name}.')
            print('Exiting program.')
            exit()

    # Change directory back to root and delete the cloned repository
    def return_to_root(repo_name):
        try:
            os.chdir("..")
            os.system(f"rm -rf {repo_name}")
        except:
            print(f'Failed to return root and delete {repo_name}.')
            print('Exiting program.')
            exit()

    # Check the repository for 'package-lock.json' or 'yarn.lock'
    def get_package_manager(repo_name):
        try:
            # Check if 'package-lock.json' and 'yarn.lock' exist in the repository
            packageLockJsonExists = os.path.isfile('package-lock.json')
            yarnLockExists = os.path.isfile('yarn.lock')

            if packageLockJsonExists and yarnLockExists:
                return 'Yes (NPM and Yarn)' 
            elif packageLockJsonExists:
                return 'Yes (NPM)'
            elif yarnLockExists:
                return 'Yes (Yarn)'
            else:
                return 'No'
        except:
            print(f'Failed to check for a package manager for {repo_name}.')
            print('Exiting program.')
            exit()

    # Check the repository for Semantic Release
    def get_semantic_release(repo_name):
        try:
            packageJsonExists = os.path.isfile('package.json')

            if packageJsonExists:
                with open('package.json', 'r') as f:
                    data = json.load(f)

                semanticRelease = 'devDependencies' in data and 'semantic-release' in data['devDependencies']
            else:
                semanticRelease = False

            # If semanticRelease is True, return 'Yes'. Otherwise, return 'No'
            if semanticRelease:
                return 'Yes'
            else:
                return 'No'
        except:
            print(f'Failed to check for Semantic Release for {repo_name}.')
            print('Exiting program.')
            exit()

    # Check the repository for GitHub Actions files
    def get_gha(repo_name):
        try:
            ymlFiles = glob.glob('.github/workflows/*.yml')
            yamlFiles = glob.glob('.github/workflows/*.yaml')

            files = ymlFiles + yamlFiles

            one_year_ago = datetime.datetime.now(pytz.utc) - datetime.timedelta(days=365)

            for file in files:
                result = subprocess.run(['git', 'log', '-1', '--format=%cd', file], capture_output=True, text=True)
                file_date = datetime.datetime.strptime(result.stdout.strip(), '%a %b %d %H:%M:%S %Y %z').replace(tzinfo=pytz.utc)

                if file_date > one_year_ago:
                    return 'Yes'
            return 'No'  # If no recent files are found

        except:
            print(f'Failed to check for GitHub Actions files for {repo_name}.')
            print('Exiting program.')
            exit()
            
    # Check the repository for Integration Suite (GHA)
    def get_gha_integration(repo_name):
        try:
            ymlFiles = glob.glob('.github/workflows/*.yml')
            yamlFiles = glob.glob('.github/workflows/*.yaml')
            allFiles = ymlFiles + yamlFiles
            keywords = ["test", "build", "integration"]

            for file in allFiles:
                with open(file, 'r') as f:
                    if any(keyword in line for line in f for keyword in keywords):
                        return "Yes"
            return "No"
        except:
            print(f'Failed to check for Integration Suite (GHA) for {repo_name}.')
            print('Exiting program.')
            exit()

    # Check the repository for Concurrency Rule (GHA)
    def get_gha_concurrency(repo_name):
        try:
            ymlFiles = glob.glob('.github/workflows/*.yml')
            yamlFiles = glob.glob('.github/workflows/*.yaml')
            allFiles = ymlFiles + yamlFiles

            for file in allFiles:
                with open(file, 'r') as f:
                    if 'concurrency' in f.read():
                        return "Yes"
            return "No"
        except:
            print(f'Failed to check for Concurrency Rule (GHA) for {repo_name}.')
            print('Exiting program.')
            exit()

    # Check the repository for Mend (GHA)
    def get_mend_gha(repo_name):
        try:
            ymlFiles = glob.glob('.github/workflows/*.yml')
            yamlFiles = glob.glob('.github/workflows/*.yaml')
            allFiles = ymlFiles + yamlFiles

            for file in allFiles:
                with open(file, 'r') as f:
                    if 'mend' in f.read():
                        return "Yes"
            return "No"
        except:
            print(f'Failed to check for Mend (GHA) for {repo_name}.')
            print('Exiting program.')
            exit()

    # Check the repository for Dependency Management
    def get_dependency_management(repo_name):
        try:
            process = subprocess.run(["gh", "pr", "list"], capture_output=True, text=True)
            output = process.stdout
            if "renovate" and "dependabot" in output:
                return "Renovate and Dependabot"
            elif "renovate" in output :
                return "Renovate"    
            elif "dependabot" in output:
                return "Dependabot"
            return "No"
        except:
            print(f'Failed to check for Dependency Management for {repo_name}.')
            print('Exiting program.')
            exit()
