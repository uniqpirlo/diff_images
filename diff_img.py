import cv2
from matplotlib import pyplot as plt

# small = cv2.imread('subset.png', 0)
small = cv2.imread('subset.png')
small = cv2.cvtColor(small, cv2.COLOR_RGB2GRAY)
big = cv2.imread('test.jpg', 0)
big2 = big.copy()
w, h = small.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']


for meth in methods:
    big = big2.copy()
    method = eval(meth)
    res = cv2.matchTemplate(big, small, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(big, top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res, cmap='gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(big, cmap='gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    # plt.suptitle(meth)

    plt.show()
