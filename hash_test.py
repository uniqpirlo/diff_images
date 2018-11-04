from PIL import Image
import imagehash


def images_diff(img1, img2):
    image1 = Image.open(img1)
    image1 = image1.resize((int(image1.width / 2), int(image1.height / 2)))
    h1 = imagehash.dhash(image1)
    print(h1)

    image2 = Image.open(img2)
    image2 = image2.resize((int(image2.width / 2), int(image2.height / 2)))
    h2 = imagehash.dhash(image2)
    print(h2)
    print('{}, {}:{}'.format(img1, img2, h1 - h2))


if __name__ == '__main__':
    (images_diff("test.jpg", "test_gray.jpg"))
    (images_diff("test1.jpg", "test1_gray.jpg"))
    (images_diff("test.jpg", "test1.jpg"))
    (images_diff("test_gray.jpg", "test1_gray.jpg"))
    print('\n')

    (images_diff("test.jpg", "test2.jpg"))
    (images_diff("test_gray.jpg", "test2.jpg"))
    (images_diff("test1.jpg", "test2.jpg"))
    (images_diff("test1_gray.jpg", "test2.jpg"))
    print('\n')

    images_diff("test_black.bmp", "test1_black.bmp")
    images_diff("test.jpg", "test_p.png")
