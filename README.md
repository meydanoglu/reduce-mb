# Story
This simple program uses Pillow, Python Image Library to reduce the size of images in a folder.
I wanted to make this simple program, because I occasionaly upload some snapshots from movies to Notion, and Notion only allows images that are not bigger than 5 MB. It turned out to be really annoying to
try to resize images one by one.
### Instructions on how to use this if you couldn't figured it out:
+ PIL must be installed. If you don't have Pillow installed, you can install it using:

  
  ```
  pip install Pillow
  ```

+ Please provide the input path containing the images, specify the output path where you'd like the compressed images to be saved, and indicate the target file size in megabytes to reduce the images. If an image is already smaller than the specified size, it will remain unaffected. However, note that the apparent reduction in size may occur due to the image-saving processes implemented by the Pillow library.
  
  ```python
  if __name__ == "__main__":
    input_folder = r"C:\Users\My Input Folder"
    output_folder = r"C:\Users\My Output Folder"
    max_size_mb = 5

    reducer(input_folder, output_folder, max_size_mb)
  ```
