import os
import json
import glob

class Config:
    #
    # List of repositories to migrate
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
        os.system(f"git clone https://github.com/HT2-Labs/{repo_name}.git")
        os.chdir(repo_name)

    # Change directory back to root and delete the cloned repository
    def return_to_root(repo_name):
        os.chdir("..")
        os.system(f"rm -rf {repo_name}")

    # Check the repository for 'package-lock.json' or 'yarn.lock'
    def get_package_manager(repo_name):
        try:
            # Check if 'package-lock.json' and 'yarn.lock' exists in the repository
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

            if packageJsonExists == True:
                with open('package.json', 'r') as f:
                    data = json.load(f)

                semanticRelease = 'devDependencies' in data and 'semantic-release' in data['devDependencies']
            else:
                semanticRelease = False

            # If semanticRelease is True, return 'Yes'. Otherwise, return 'No'
            if semanticRelease == True:
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

            if ymlFiles or yamlFiles:
                return 'Yes'
            else:
                return 'No'
        except:
            print(f'Failed to check for GitHub Actions files for {repo_name}.')
            print('Exiting program.')
            exit()
