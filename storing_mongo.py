import os
from pymongo import MongoClient
import gridfs
from PIL import Image

# Directories for cat and dog images
dog_dir = "./data/PetImages/Dog"
cat_dir = "./data/PetImages/Cat"

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['pet_images_db']
fs = gridfs.GridFS(db)

# Function to save image to MongoDB


def save_image_to_db(directory, label):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):  # Ensure it's a file
            try:
                # Open and verify the image
                img = Image.open(file_path)
                img.verify()

                # Save image to GridFS
                with open(file_path, 'rb') as file_data:
                    fs.put(file_data, filename=filename, label=label)
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

# Save cat and dog images


save_image_to_db(cat_dir, 'cat')
save_image_to_db(dog_dir, 'dog')

print("Images saved to MongoDB successfully!")
