import os
from typing import Tuple

from PIL import Image

def main() -> None:
    """
    Main function.

    Args:
    None

    Returns:
    None.
    """
    with Image.open("test.jpeg") as img:
        crop_img(img, (50, 50, 50, 800), shave=True)

def shave_img(
    img: Image.Image, crop_dimensions: Tuple[int, int, int, int]
) -> Tuple[int, int, int, int]:
    """
    Calculate the new dimensions for cropping an image based on specified crop dimensions.

    This function takes an image and a tuple of crop dimensions, and returns a new tuple
    representing the left, top, right, and bottom coordinates for cropping the image.

    Args:
    img (Image object): the image from which dimensions will be calculated.
    crop_dimensions (Tuple): a tuple containing four integers (left, upper, right, lower)

    Returns:
    Tuple: A tuple containing the new crop dimensions:
        - left: The same as the input left.
        - top: The same as the input top.
        - right: The width of the image minus the input right.
        - bottom: The height of the image minus the input bottom.
    """
    width, height = img.size
    left, top, right, bottom = crop_dimensions
    return left, top, width - right, height - bottom

def crop_img(
    img: Image.Image, crop_dimensions: Tuple[int, int, int, int], shave: bool=False
) -> None:
    """
    Crops and saves an image.

    Args:
    img (Image object): the image to crop
    crop_dimensions (Tuple): the coordinates to crop (left, upper, right, lower)

    Returns:
    None
    """
    if shave:
        crop_dimensions = shave_img(img, crop_dimensions)
    img_crop = img.crop(crop_dimensions)
    img_crop.save('test2.png', 'PNG')

if __name__ == "__main__":
    main()
