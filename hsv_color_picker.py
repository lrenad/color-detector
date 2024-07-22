import cv2
import numpy as np

def nothing(x):
    pass

# Create a window
cv2.namedWindow("frame")

# Create trackbars for color change
cv2.createTrackbar("H", "frame", 0, 179, nothing)
cv2.createTrackbar("S", "frame", 255, 255, nothing)
cv2.createTrackbar("V", "frame", 255, 255, nothing)

# Create a blank HSV image
img_hsv = np.zeros((250, 500, 3), np.uint8)

while True:
    # Get current positions of the trackbars
    h = cv2.getTrackbarPos("H", "frame")
    s = cv2.getTrackbarPos("S", "frame")
    v = cv2.getTrackbarPos("V", "frame")
    
    # Update the HSV image with the current trackbar values
    img_hsv[:] = (h, s, v)
    
    # Convert the HSV image to BGR for display
    img_bgr = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
    
    # Display the image
    cv2.imshow("frame", img_bgr)
    
    # Break the loop if the Escape key is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# Destroy all OpenCV windows
cv2.destroyAllWindows()

