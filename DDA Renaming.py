import os
import shutil

# Set the path to the folder containing the client folders
#FUTURE DAMON READ THIS
# Do not copy and paste directly, we need forward slashes in python for this to work.
parent_folder = "C:/Users/damon.melton/Documents/Display Ads"

# Iterate through the client folders
for client_folder in os.listdir(parent_folder):
    for file_name in os.listdir(os.path.join(parent_folder, client_folder)):
        old_path = os.path.join(parent_folder, client_folder, file_name)
        new_file_name = client_folder + "_" + file_name
        new_path = os.path.join(parent_folder, client_folder, new_file_name)
        shutil.move(old_path, new_path)