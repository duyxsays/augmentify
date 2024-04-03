# %% 
# import libraries
import aug_methods as am 
import os

# %%
# place each category of sample in the samples directory
data_dir = os.path.join(os.getcwd(), 'samples')
# %% 
# check if all the categories are printed
categories = am.list_data_folders(data_dir)

# %%
# select a category
index = 0 # <- select a directory/category 
selected_category = categories[index] 

print('\nChosen category: ' + selected_category)

category_dir = os.path.join(data_dir, selected_category)

# %%
# read sample directories
inverted = 'new-directory-for-inverted'
shifted = 'new-directory-for-shifted'
stretched = 'new-directory-for-stretched'

# reference to the destination folder
augmented_root = 'output-folder-for-augmented-data'
destination = os.path.join(augmented_root, selected_category)

# %%
# run the augmentation methods
am.polarity_invert_samples(category_dir, inverted, selected_category, "1", "1")              # 1. Invert the samples
am.pitch_shift_samples(inverted, shifted, selected_category, "1", "1")                       # 2. Pitch shift the samples
am.time_stretch_samples(shifted, stretched, selected_category, "1", "1")                     # 3. Time stretch the samples
am.move_data(augmented_root, destination, stretched, selected_category, "1", "1")            # 4. Move the augmented samples to the destination folder

# %%
# reduce the samples to one second
am.reduce_samples(augmented_root)                                                           # 6. Reduce the samples to one second

# %%
# create a time histogram
am.analyse_duration(augmented_root)                                                         # 7. Create a time histogram of the original and augmented samples

# %%
# run the entire augmentation process
category_count = 0
total_categories = len(categories)
print('Augmenting data...')
for category in categories:
    category_count += 1
    category_dir = os.path.join(root, category)
    destination = os.path.join(augmented_root, category)

    am.polarity_invert_samples(category_dir, inverted, category, str(category_count), str(total_categories))    # 1. Invert the samples
    am.pitch_shift_samples(inverted, shifted,  category, str(category_count), str(total_categories))            # 2. Pitch shift the samples
    am.time_stretch_samples(shifted, stretched, category, str(category_count), str(total_categories))           # 3. Time stretch the samples
    am.move_data(augmented_root, destination, stretched, category, str(category_count), str(total_categories))  # 4. Move the augmented samples to the destination folder
    

am.reduce_samples(augmented_root)                                                                               # 5. Reduce the samples to one second

# %%
