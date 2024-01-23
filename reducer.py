from PIL import Image
import os

def reducer(input_folder, output_folder, max_size_mb):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        # os.path.join will construct file paths for input and output images.
        # The one for the input_folder makes sure that we have example.png inside the input folder,
        # whereas the one for the output makes sure that the modified example.png will be created inside the output folder.
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        # Check if the file is an image, and not another folder or anything.
        # I wanted to make sure that this program won't mess with the folder I am using as the output folder,
        # which is inside the input_folder.
        if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            # Open the image. Thanks to the with function, we don't need to manually close it.
            with Image.open(input_path) as img:
                # Set an initial quality value, 100. So, if our image is less than 4.9 mb, the program will not touch it.
                current_quality = 100

                # Calculate the target size in bytes. The os.path.getsize() function returns to size in bytes, so this is necessary.
                target_size_bytes = int(max_size_mb * 1024 ** 2)

                img.save(output_path, quality=current_quality)
                # Critic part: Check if the image meets the size requirement
                while os.path.getsize(output_path) > target_size_bytes and current_quality > 0:
                    # Reduce the image quality
                    current_quality = current_quality - 5
                    
                    # Save the image with the determined quality setting
                    img.save(output_path, format= 'JPEG', quality=current_quality)

if __name__ == "__main__":
    input_folder = r"C:\Users"
    output_folder = r"C:\Users"
    max_size_mb = 4.8

    reducer(input_folder, output_folder, max_size_mb)
