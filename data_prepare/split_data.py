from sklearn.model_selection import train_test_split
import os
import shutil


data_folder = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder/"

video_clips = os.listdir(data_folder)

train_clips, test_clips = train_test_split(video_clips, test_size=0.30)

train_folder = "/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder/prediction_train/"
test_folder = '/home/jnomad/Documents/Semester 6/Thesis/GRIP-master/data_folder/prediction_test/'


#create the train and test folders if they don't already exist
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

#move training clips to the train folder
for clip in train_clips:
	shutil.move(os.path.join(data_folder, clip), os.path.join(train_folder, clip))

#move testing clips to the test folder
for clip in test_clips:
	shutil.move(os.path.join(data_folder, clip), os.path.join(test_folder, clip))

print("{} - training clips and {} - testing clips.".format(len(train_clips), len(test_clips)))

