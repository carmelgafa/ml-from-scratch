import matplotlib.pyplot as plt
import os

def process_image(image_path):
    '''load and convert image to grayscale'''

    image_path = os.path.join(os.path.dirname(__file__), image_path)
    image = plt.imread(image_path)

    # convert image to grayscale
    image = image.mean(axis=2)

    plt.imshow(image, cmap='gray')
    plt.show()



if __name__ == '__main__':
    image_path = 'bud.jpg'
    
    image = process_image(image_path)
    cv2.imshow('image', image)
    cv2.waitKey(0)