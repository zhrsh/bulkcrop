import os
import argparse
from typing import Tuple, List
from PIL import Image

NAME = "bulkcrop"

def main() -> None:
    """
    Main function.

    Args:
    None.

    Returns:
    None.
    """
    args = run_argparse()
    bulk_crop_img(args.cropbox, args.files, shave=args.shave)

def run_argparse() -> argparse.ArgumentParser.parse_args:
    """
    Parse the user's command line arguments. Runs at the beginning of the program.

    Args: none
    Returns: parser.parse_args() (parsed arguments. an argparse obj)
    """

    parser = argparse.ArgumentParser(
        description='A simple script to bulk crop images. This script is under the MIT License. Copyright (c) 2025 Zahra A. S.',
        epilog='For more information, see documentation at github.com/zhrsh/bulkcrop',
        prog=NAME
    )

    parser.add_argument(
        '-f', '--files', type=str,
        nargs='+', required=True,
        help='list of image files to crop (e.g., use "*.png" for all png images in cwd)'
    )

    parser.add_argument(
        '-b', '--cropbox', type=int,
        nargs=4, metavar=("LEFT", "UPPER", "RIGHT", "LOWER"),
        required=True,
        help='coordinates for the cropbox as a list of integers (e.g., --box 5 5 5 5)'
    )

    parser.add_argument(
        '-s', '--shave',
        action='store_true',
        help='use the cropbox as lengths to "shave" each side of the image instead. use only for images of the same size.'
    )

    # return parsed args
    return parser.parse_args()

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
    crop_box: Tuple[int, int, int, int],
    file_list: List[str],
    input_dir: str=".",
    output_dir: str=".",
    shave: bool=False
) -> None:
    """
    Crops specified images and saves them to the output directory.

    Args:
    crop_box: a tuple of (left, upper, right, lower) coordinates for cropping.
    file_list: list of image file names to be processed.
    input_dir: directory containing input images (default is cwd).
    output_dir: directory where cropped images will be saved (default is cwd).
    """
    # create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # loop through the provided list of file names
    for filename in file_list:
        # check for image file types
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_dir, filename)
            try:
                with Image.open(img_path) as img:
                    if shave:
                        crop_box = shave_img(img, crop_box)
                    # crop & save img
                    cropped_img = img.crop(crop_box)
                    # save with the same extension
                    cropped_img.save(os.path.join(
                        output_dir,
                        f"{os.path.splitext(filename)[0]}_crop{os.path.splitext(filename)[1]}"
                    ))
            except Exception as e:
                print(f"error: unable to process {filename}:\n{e}")
        else:
            print(f"error: {filename} is not an image.")

if __name__ == "__main__":
    main()
