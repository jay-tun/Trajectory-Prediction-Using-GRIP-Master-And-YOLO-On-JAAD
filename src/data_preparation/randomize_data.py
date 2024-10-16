import random
import shutil
import os

data_folder = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder_new/"
output_folder = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder_new/selected_data/"

# List all .txt files
data_files = [f for f in os.listdir(data_folder) if f.endswith('.txt')]

# Randomly select 53 files
selected_files = random.sample(data_files, 54)

# Ensure the output directory exists
os.makedirs(output_folder, exist_ok=True)

# Move selected files to the output directory
for file in selected_files:
    shutil.move(os.path.join(data_folder, file), os.path.join(output_folder, file))

print(f"Selected {len(selected_files)} files out of {len(data_files)} and moved them to {output_folder}.")

