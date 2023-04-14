import cv2

img = cv2.imread('blue.jpg')
img = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(gray_blur, 30, 50)
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
min_area = 3
max_area = 70
filtered_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > min_area and area < max_area:
        filtered_contours.append(contour)
cv2.drawContours(img, filtered_contours, -1, (0, 0, 255), 2)
cv2.imshow('Contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
