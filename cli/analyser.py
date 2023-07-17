from config import Config as c

for repo in c.repos:
    # Analyse the repository
    try:
        # Clone the repo
        c.clone_repo(repo)

        # Check for a Package Manager
        packageManager = c.get_package_manager(repo)

        # Clone for Semantic Release
        semanticRelease = c.get_semantic_release(repo)

        # Clone for GitHub Actions
        githubActions = c.get_gha(repo)
        
        # Return to the root directory and delete the repo
        c.return_to_root(repo)
    except:
        print(f'Failed to analyse {repo}.')
        print('Exiting program.')
        exit()

    # Print the repository information to the console
    try:
        print('--------------------------------')
        print(f'Repository: {repo}')
        print(f'Package Manager: {packageManager}')
        print(f'Semantic Release: {semanticRelease}')
        print(f'GitHub Actions: {githubActions}')
        print('--------------------------------')
    except:
        print(f'Failed to print to the console for {repo}.')
        print('Exiting program.')
        exit()