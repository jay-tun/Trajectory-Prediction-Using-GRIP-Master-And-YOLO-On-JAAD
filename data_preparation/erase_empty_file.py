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
directory_path = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder/data_set/"
delete_empty_files(directory_path)

