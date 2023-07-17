from config import Config as c

for repo in c.repos:
    # Analyse the repository
    try:
        # Clone the repo
        c.clone_repo(repo)

        # Check for a Package Manager
        packageManager = c.get_package_manager(repo)

        # Check for Semantic Release
        semanticRelease = c.get_semantic_release(repo)

        # Check for GitHub Actions
        githubActions = c.get_gha(repo)
        
        # Check for Dependency Management
        dependencyManagement = c.get_dependency_management(repo)
        
        # Check for Integration Suite (GHA)
        integrationSuite = c.get_gha_integration(repo)
        
        # Check for Concurrency Rule (GHA)
        concurrencyRule = c.get_gha_concurrency(repo)
        
        # Check for Mend (GHA)
        mend = c.get_mend_gha(repo)

        # Return to the root directory and delete the repo
        c.return_to_root(repo)
    except:
        print(f'Failed to analyse {repo}.')
        print('Exiting program.')
        exit()

    # Print the repository information to the console
    try:
        print(f'{c.CYAN}--------------------------------{c.RESET}')
        print(f'Repository: {c.YELLOW}{repo}{c.RESET}')
        print(f'Package Manager: {c.RED if packageManager == "No" else c.GREEN}{packageManager}{c.RESET}')
        print(f'Semantic Release: {c.GREEN if semanticRelease == "Yes" else c.RED}{semanticRelease}{c.RESET}')
        print(f'GitHub Actions: {c.GREEN if githubActions == "Yes" else c.RED}{githubActions}{c.RESET}')
        print(f'Dependency Management: {c.RED if dependencyManagement == "No" else c.GREEN}{dependencyManagement}{c.RESET}')
        print(f'Integration Suite (GHA): {c.GREEN if integrationSuite == "Yes" else c.RED}{integrationSuite}{c.RESET}')
        print(f'Concurrency Rule (GHA): {c.GREEN if concurrencyRule == "Yes" else c.RED}{concurrencyRule}{c.RESET}')
        print(f'Mend (GHA): {c.GREEN if mend == "Yes" else c.RED}{mend}{c.RESET}')
        print(f'{c.CYAN}--------------------------------{c.RESET}')
    except:
        print(f'{c.RED}Failed to print to the console for {repo}.')
        print(f'{c.RED}Exiting program.')
        exit()
