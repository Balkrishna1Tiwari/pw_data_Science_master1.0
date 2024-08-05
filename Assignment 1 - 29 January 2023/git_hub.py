import os
import subprocess

def push_folders_to_github(root_folder, github_repo_url):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Skip the `.git` directory and any other hidden directories
        if '.git' in dirpath:
            continue

        # Ensure we're not at the root folder level
        if dirpath == root_folder:
            continue

        os.chdir(dirpath)

        # Initialize a new git repository
        subprocess.run(['git', 'init'], check=True)
        
        # Configure Git buffer size
        subprocess.run(['git', 'config', '--global', 'http.postBuffer', '524288000'], check=True)
        
        # Add all files to the staging area
        subprocess.run(['git', 'add', '.'], check=True)

        # Check if there are changes to commit
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if result.stdout:
            # Commit the changes
            subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)
            
            # Check if remote 'origin' exists
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], capture_output=True, text=True)
            if result.returncode != 0:
                # Remote 'origin' does not exist, add it
                subprocess.run(['git', 'remote', 'add', 'origin', github_repo_url], check=True)
            else:
                # Remote 'origin' exists, update the URL if needed
                subprocess.run(['git', 'remote', 'set-url', 'origin', github_repo_url], check=True)
            
            # Fetch the remote branches
            try:
                subprocess.run(['git', 'fetch', 'origin'], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error fetching from origin in folder {dirpath}: {e}')
                continue  # Skip pushing if fetching fails

            # Push the changes to the remote repository
            try:
                # Use 'main' or 'master' based on the repository's default branch
                subprocess.run(['git', 'push', '-u', 'origin', 'main'], check=True)
            except subprocess.CalledProcessError as e:
                print(f'Error pushing folder {dirpath}: {e}')
        else:
            print(f'No changes to commit in folder {dirpath}')

        print(f'Processed folder {dirpath}')

# Set the root folder and GitHub repository URL
root_folder = r'C:\Users\balkr\PWSkills-Assignments-main'
github_repo_url = 'https://github.com/yourusername/your-repository.git'

push_folders_to_github(root_folder, github_repo_url)
