from github import Github

# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your GitHub personal access token
access_token = 'GITHUB_PAT'

# Create a GitHub API object using the access token
g = Github(access_token)

# Replace 'YOUR_ORGANIZATION_NAME' with your GitHub organization name
organization_name = 'HT2-Labs'

# Function to check for dependency management tools
def check_dependency_management(repo):
    package_lock_exists = "package-lock.json" in [f.name for f in repo.get_contents("")]
    yarn_lock_exists = "yarn.lock" in [f.name for f in repo.get_contents("")]

    if package_lock_exists:
        return "NPM"
    elif yarn_lock_exists:
        return "Yarn"
    else:
        return "No"

# Function to check for Renovate/Dependabot
def check_renovate_dependabot(repo):
    get_pull_requests = repo.get_pulls(state="all")
    renovate_found = False
    dependabot_found = False

    for pr in get_pull_requests:
        if pr.user.login.lower() == "renovate[bot]":
            renovate_found = True

        if pr.user.login.lower() == "dependabot[bot]":
            dependabot_found = True

    if renovate_found and dependabot_found:
        return "Renovate/Dependabot"
    elif renovate_found:
        return "Renovate"
    elif dependabot_found:
        return "Dependabot"
    else:
        return "No"

# Function to check for GitHub Actions (GHA)
def check_gha(repo):
    workflows = repo.get_workflows()
    return "Yes" if workflows.totalCount > 0 else "No"

# Function to check for Integration Suite (GHA)
def check_integration_suite(repo):
    workflows = repo.get_workflows()
    for workflow in workflows:
        if "integration" in workflow.name.lower():
            return "Yes"
    return "No"

# Function to check for Concurrency Rule (GHA)
def check_concurrency_rule(repo):
    workflows = repo.get_workflows()

    for workflow in workflows:
        if "integration" in workflow.name.lower():
            workflow_file = workflow.raw_data['path']
            workflow_content = repo.get_contents(workflow_file).decoded_content.decode()

            if "concurrency:" in workflow_content:
                return "Yes"

    return "No"

# Function to check for Mend (GHA)
def check_mend(repo):
    workflows = repo.get_workflows()
    for workflow in workflows:
        if "mend" in workflow.name.lower():
            return "Yes"
    return "No"

# Retrieve the organization
org = g.get_organization(organization_name)

# Loop through all repositories in the organization
for repo in org.get_repos():
    print("Repository Name:", repo.name)
    print("Repository URL:", repo.html_url)

    # Check dependency management
    dependency_management = check_dependency_management(repo)
    print("Dependency Management:", dependency_management)

    # Check Renovate/Dependabot
    renovate_dependabot = check_renovate_dependabot(repo)
    print("Renovate/Dependabot:", renovate_dependabot)

    # Check GitHub Actions (GHA)
    gha = check_gha(repo)
    print("GitHub Actions (GHA):", gha)

    # Check Integration Suite (GHA)
    integration_suite = check_integration_suite(repo)
    print("Integration Suite (GHA):", integration_suite)

    # Check Concurrency Rule (GHA)
    concurrency_rule = check_concurrency_rule(repo)
    print("Concurrency Rule (GHA):", concurrency_rule)

    # Check Mend (GHA)
    mend = check_mend(repo)
    print("Mend (GHA):", mend)

    print("---")
