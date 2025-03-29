import os
from typing import Tuple

from PIL import Image

def main():
    with Image.open("test.jpeg") as img:
        crop_img(img, (50, 50, 50, 800), shave=True)

def shave_img(img: Image.Image, crop_dimensions: Tuple[int, int, int, int]) -> Tuple[int, int, int, int]:
    width, height = img.size
    left, top, right, bottom = crop_dimensions
    return left, top, width - right, height - bottom

def crop_img(img: Image.Image, crop_dimensions: Tuple[int, int, int, int], shave: bool) -> None:
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
