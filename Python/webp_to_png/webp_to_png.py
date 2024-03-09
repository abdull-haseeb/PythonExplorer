from PIL import Image
import os

def convert_webp_to_png(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all .webp files in the input folder
    webp_files = [f for f in os.listdir(input_folder) if f.endswith('.webp')]

    for webp_file in webp_files:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, webp_file)
        output_file = os.path.splitext(webp_file)[0] + '.png'
        output_path = os.path.join(output_folder, output_file)

        # Open the .webp file and convert it to .png
        with Image.open(input_path) as img:
            img.save(output_path, 'PNG')

        print(f"Converted {webp_file} to {output_file}")

# Specify the input and output folders

input_folder = 'InputFiles'
output_folder = 'Output_folder'

convert_webp_to_png(input_folder, output_folder)
