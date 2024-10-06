import os
import shutil

# Define paths
base_dir = "C:/Users/tplay/OneDrive/Documents/School/Classes/SeniorFall/CST-435/SearchEngines-Github/Neural Network - Project 3"  # Change this to the path where PlantCLEF2020TrainingData is located
plantclef_dir = os.path.join(base_dir, "PlantCLEF2020TrainingData")
combined_dir = os.path.join(base_dir, "PlantCLEF_Combined")

# Create the combined directory if it doesn't exist
if not os.path.exists(combined_dir):
    os.makedirs(combined_dir)

# Get a list of all species present in each of the three folders
species_folders = set()
for main_folder in ['herbarium', 'herbarium_photo_associations', 'photo']:
    main_path = os.path.join(plantclef_dir, main_folder)
    if os.path.exists(main_path):
        species_folders.update(os.listdir(main_path))

# Create combined subdirectories for each species and populate them
for species in species_folders:
    species_combined_path = os.path.join(combined_dir, species)
    if not os.path.exists(species_combined_path):
        os.makedirs(species_combined_path)

    # Copy images from each source folder if the species folder exists
    for source_folder in ['herbarium', 'herbarium_photo_associations', 'photo']:
        source_path = os.path.join(plantclef_dir, source_folder, species)
        if os.path.exists(source_path):
            for img_file in os.listdir(source_path):
                source_img_path = os.path.join(source_path, img_file)
                destination_img_path = os.path.join(species_combined_path, f"{source_folder}_{img_file}")
                shutil.copy2(source_img_path, destination_img_path)

print("Dataset organized successfully.")
