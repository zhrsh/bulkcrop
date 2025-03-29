import os
from typing import Tuple, List

from PIL import Image

def main() -> None:
    """
    Main function.

    Args:
    None.

    Returns:
    None.
    """
    with Image.open("test.jpeg") as img:
        crop_box = shave_img(img, (50, 50, 50, 50))
        bulk_crop_img(crop_box)

def shave_img(
    img: Image.Image, crop_box: Tuple[int, int, int, int]
) -> Tuple[int, int, int, int]:
    """
    Calculate the new dimensions for cropping an image based on specified crop dimensions.

    This function takes an image and a tuple of crop dimensions, and returns a new tuple
    representing the left, top, right, and bottom coordinates for cropping the image.

    Args:
    img (Image object): the image from which dimensions will be calculated.
    crop_box (Tuple): a tuple of (left, upper, right, lower) coordinates for cropping.

    Returns:
    Tuple: A tuple containing the new crop dimensions:
        - left: The same as the input left.
        - top: The same as the input top.
        - right: The width of the image minus the input right.
        - bottom: The height of the image minus the input bottom.
    """
    width, height = img.size
    left, top, right, bottom = crop_box
    return left, top, width - right, height - bottom

def bulk_crop_img(
    # input_dir and output_dir are the cwd (".") by default
    crop_box: Tuple[int, int, int, int], input_dir: str=".", output_dir: str="." 
) -> None:
    """
    Crops images in the input directory and saves them to the output directory.

    Args:
    crop_box: a tuple of (left, upper, right, lower) coordinates for cropping.
    input_dir: directory containing input images (default is cwd).
    output_dir: directory where cropped images will be saved (default is cwd).
    """
    # create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # loop through all files in the input directory
    for filename in os.listdir(input_dir):
        # check for image file types
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            try:
                with Image.open(img_path) as img:
                    # crop & save img
                    cropped_img = img.crop(crop_box)
                    # save with the same extension
                    cropped_img.save(os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_cropped{os.path.splitext(filename)[1]}"))
            except Exception as e:
                print(f"error processing {filename}:\n{e}")

if __name__ == "__main__":
    main()
