''' image manipulation '''
#pylint: disable = E0401
import os
import matplotlib.pyplot as plt


def load_image_to_rgb(image_path):
    '''load and convert image to RGB'''

    image = plt.imread(image_path)

    b, g, r = image[:, :, 0], image[:, :, 1], image[:, :, 2] # For RGB image

    return b, g, r

def load_image_to_grayscale(image_path):
    '''load and convert image to grayscale'''

    image = plt.imread(image_path)

    # convert image to grayscale
    image = image.mean(axis=2)

    return image

if __name__ == '__main__':
    BUD_FILENAME = 'bud.jpg'
    bud_path = os.path.join(os.path.dirname(__file__), BUD_FILENAME)


    bud_image_grayscale = load_image_to_grayscale(bud_path)
    plt.imshow(bud_image_grayscale, cmap='gray')
    plt.show()


    bud_image_r, bud_image_g, bud_image_b = load_image_to_rgb(bud_path)
    plt.imshow(bud_image_r, cmap='Reds')
    plt.show()
    plt.imshow(bud_image_g, cmap='Greens')
    plt.show()
    plt.imshow(bud_image_b, cmap='Blues')
    plt.show()
        