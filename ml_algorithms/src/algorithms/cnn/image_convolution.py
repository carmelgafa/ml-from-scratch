
#pylint: disable = E0401
import os
import cv2
import matplotlib.pyplot as plt

def process_image(image_path):
    '''load and convert image to grayscale'''

    image_path = os.path.join(os.path.dirname(__file__), image_path)
    image = plt.imread(image_path)

    # convert image to grayscale
    image = image.mean(axis=2)

    plt.imshow(image, cmap='gray')
    plt.show()
    return image



if __name__ == '__main__':
    bud_path = 'bud.jpg'

    bud_image = process_image(bud_path)
    cv2.imshow('image', bud_image)
    cv2.waitKey(0)
