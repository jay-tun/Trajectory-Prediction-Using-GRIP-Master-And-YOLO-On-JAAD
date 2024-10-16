from sklearn.model_selection import train_test_split
import os
import shutil

data_folder = '/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder/'
# List only .txt files
data_files = [f for f in os.listdir(data_folder) if f.endswith('.txt')]

# Split data into training and testing sets
train_files, test_files = train_test_split(data_files, test_size=1/56, random_state=42)

train_folder = os.path.join(data_folder, "prediction_train")
test_folder = os.path.join(data_folder, "prediction_test")

# Create the train and test folders if they don't already exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Move training files to the train folder
for file in train_files:
    shutil.move(os.path.join(data_folder, file), os.path.join(train_folder, file))

# Move testing files to the test folder
for file in test_files:
    shutil.move(os.path.join(data_folder, file), os.path.join(test_folder, file))

print(f"{len(train_files)} training files and {len(test_files)} testing files moved successfully.")

