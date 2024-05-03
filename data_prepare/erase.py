"""This script removes files which does not contain 
any content in them. It is written to clean the dataset 
which did not include anything and was causing error in 
processing data."""

import os

def delete_empty_files(directory):
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if the file is empty
        if os.path.isfile(filepath) and os.path.getsize(filepath) == 0:
            # Delete the empty file
            os.remove(filepath)
            print(f"Deleted empty file: {filepath}")

# Example usage:
directory_path = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/tess/train/"
delete_empty_files(directory_path)

