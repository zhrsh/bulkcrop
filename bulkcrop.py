from PIL import Image
import os

with Image.open("test.jpeg") as img:
    width, height = img.size
    (left, upper, right, lower) = (50, 50, (width - 50), (height - 500))

    # here the image "img" is cropped and assigned to new variable img_crop
    img_crop = img.crop((left, upper, right, lower))
    img_crop.save('test2.png', 'PNG')
