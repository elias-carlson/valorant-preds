import cv2
import os

directory = 'frames/'
mask = cv2.imread('../mask.png', 0)

frame = 1
files = os.listdir(directory)

img_dimensions = cv2.imread(directory + files[0]).shape
mask = cv2.resize(mask, (img_dimensions[1], img_dimensions[0]))
cv2.imwrite('mask.png', mask)

for file in files:
    img = cv2.imread(directory + file)
    
    res = cv2.bitwise_and(img, img, mask = mask)
    cv2.imwrite(directory + file, res)
    print('Processing frame ' + str(frame))
    frame += 1