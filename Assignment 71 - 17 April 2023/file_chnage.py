import os

def rename_ipynb_files(root_folder, old_name, new_name):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith('.ipynb') and old_name in filename:
                old_filepath = os.path.join(dirpath, filename)
                new_filename = filename.replace(old_name, new_name)
                new_filepath = os.path.join(dirpath, new_filename)
                os.rename(old_filepath, new_filepath)
                print(f'Renamed: {old_filepath} -> {new_filepath}')

# Set the root folder and the old and new names
root_folder = r'C:\Users\balkr\PWSkills-Assignments-main'
old_name = 'Utkarsh'
new_name = 'Balkrishna_Tiwari'

rename_ipynb_files(root_folder, old_name, new_name)
