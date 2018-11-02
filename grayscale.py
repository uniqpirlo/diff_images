import cv2


img = cv2.imread('test.jpg')
width, height = cv2.GetSize(img)
print(width, height)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
width, height = cv2.GetSize(img)
print(width, height)
cv2.imwrite('test_gray.jpg', gray)
