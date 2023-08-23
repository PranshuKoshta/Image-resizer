import cv2
source = "selmoBhai.jpeg"
destination = 'BhaiRoteRoteChoteHoGye.jpeg'
scale_percent = 50

src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
cv2.imshow("bhaiRoMat", src)

#calculate the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)

# resize image
output = cv2.resize(src, (new_width, new_height))

cv2.imwrite('BhaiRoteRoteChoteHoGye.jpeg',output)