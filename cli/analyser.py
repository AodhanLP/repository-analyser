import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font
from config import Config as c

# Check if the Excel file exists
try:
    workbook = openpyxl.load_workbook('LP Github repos.xlsx')
    # Do your amendments to the existing workbook
except FileNotFoundError:
    # If the file doesn't exist, create a new workbook
    workbook = Workbook()

# Select the 'LP Github repos' sheet or create it if it doesn't exist
sheet_name = 'LP Github repos'
if sheet_name in workbook.sheetnames:
    sheet = workbook[sheet_name]
else:
    sheet = workbook.create_sheet(sheet_name)

# Define the headers in the first row of the sheet
headers = [
    'Repository Name',
    'Package Manager',
    'Dependency Management',
    'Semantic Release',
    'GHA',
    'Integration Suite (GHA)',
    'Concurrency Rule (GHA)',
    'Mend (GHA)'
]

# Write the headers to the sheet
for col_num, header in enumerate(headers, start=1):
    cell = sheet.cell(row=1, column=col_num)
    cell.value = header
    cell.font = Font(bold=True)

# Analyze each repository
for repo in c.repos:
    try:
        # Analyze the repository
        c.clone_repo(repo)
        package_manager = c.get_package_manager(repo)
        dependency_management = c.get_dependency_management(repo)
        semantic_release = c.get_semantic_release(repo)
        gha = c.get_gha(repo)
        integration_suite = c.get_gha_integration(repo)
        concurrency_rule = c.get_gha_concurrency(repo)
        mend_gha = c.get_mend_gha(repo)
        c.return_to_root(repo)

        # Write the data to the sheet
        row = len(sheet['A']) + 1
        sheet.cell(row=row, column=1, value=repo)
        sheet.cell(row=row, column=2, value=package_manager)
        sheet.cell(row=row, column=3, value=dependency_management)
        sheet.cell(row=row, column=4, value=semantic_release)
        sheet.cell(row=row, column=5, value=gha)
        sheet.cell(row=row, column=6, value=integration_suite)
        sheet.cell(row=row, column=7, value=concurrency_rule)
        sheet.cell(row=row, column=8, value=mend_gha)
    except:
        print(f'Failed to analyze {repo}.')
        print('Exiting program.')
        exit()

    # Print the repository information to the console with colors
    print(f'{c.CYAN}--------------------------------{c.RESET}')
    print(f'Repository: {c.YELLOW}{repo}{c.RESET}')
    print(f'Package Manager: {c.RED if package_manager == "No" else c.GREEN}{package_manager}{c.RESET}')
    print(f'Semantic Release: {c.GREEN if semantic_release == "Yes" else c.RED}{semantic_release}{c.RESET}')
    print(f'GitHub Actions: {c.GREEN if gha == "Yes" else c.RED}{gha}{c.RESET}')
    print(f'Dependency Management: {c.RED if dependency_management == "No" else c.GREEN}{dependency_management}{c.RESET}')
    print(f'Integration Suite (GHA): {c.GREEN if integration_suite == "Yes" else c.RED}{integration_suite}{c.RESET}')
    print(f'Concurrency Rule (GHA): {c.GREEN if concurrency_rule == "Yes" else c.RED}{concurrency_rule}{c.RESET}')
    print(f'Mend (GHA): {c.GREEN if mend_gha == "Yes" else c.RED}{mend_gha}{c.RESET}')
    print(f'{c.CYAN}--------------------------------{c.RESET}')

# Save the modified workbook
workbook.save('LP Github repos.xlsx')
