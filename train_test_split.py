import os
import shutil
import random

def split_data(source_folder_1, source_folder_2, train_folder_1, val_folder_1, train_folder_2, val_folder_2, split_ratio):
    # Ensure the destination folders exist
    for folder in [train_folder_1, val_folder_1, train_folder_2, val_folder_2]:
        os.makedirs(folder, exist_ok=True)
    
    # Get list of image files in source_folder_1 and source_folder_2
    images_1 = sorted(os.listdir(source_folder_1))
    images_2 = sorted(os.listdir(source_folder_2))
    
    # Check if the number of images is the same in both folders
    if len(images_1) != len(images_2):
        print("Error: The number of images in the two folders is not the same.")
        return
    
    # Shuffle the indices to ensure randomization
    indices = list(range(len(images_1)))
    random.shuffle(indices)
    
    # Calculate the number of training and validation samples
    num_train = int(len(indices) * split_ratio)
    num_val = len(indices) - num_train
    
    # Assign images to training and validation sets while synchronizing the split
    for i in indices[:num_train]:
        img_name = images_1[i]
        shutil.copy(os.path.join(source_folder_1, img_name), train_folder_1)
        shutil.copy(os.path.join(source_folder_2, 'thermal_' + img_name), train_folder_2)
    for i in indices[num_train:]:
        img_name = images_1[i]
        shutil.copy(os.path.join(source_folder_1, img_name), val_folder_1)
        shutil.copy(os.path.join(source_folder_2, 'thermal_' + img_name), val_folder_2)

# Replace these paths with your actual paths
source_folder_1 = "path/video_rgb_test/data"
source_folder_2 = "path/video_thermal_test/data"
train_folder_1 = "path/video_rgb_test/train"
val_folder_1 = "path/video_rgb_test/val"
train_folder_2 = "path/video_thermal_test/train"
val_folder_2 = "path/video_thermal_test/val"
split_ratio = 0.8  # Ratio of training data to total data

# Call the function to split the data
split_data(source_folder_1, source_folder_2, train_folder_1, val_folder_1, train_folder_2, val_folder_2, split_ratio)
