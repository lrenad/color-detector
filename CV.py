import cv2
import numpy as np

def nothing(x):
    pass

# Capture video from the default camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open video device")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cy, cx]
    h_value = pixel_center[0]
    s_value = pixel_center[1]
    v_value = pixel_center[2]

    color = "Not defined"
    text_color = (0, 0, 0)  # Default text color (black)

    if s_value < 20:
        if v_value < 40:
            color = "Black"
        elif v_value > 200:
            color = "White"
        else:
            color = "Grey"
            text_color = (100, 100, 100)  # Grey text color
    else:
        if h_value < 6 or h_value >= 170:
            color = "Red"
            text_color = (0, 0, 255)  # Red text color
        elif h_value < 22:
            color = "Orange"
            text_color = (0, 165, 255)  # Orange text color
        elif h_value < 32:
            color = "Yellow"
            text_color = (0, 255, 255)  # Yellow text color
        elif h_value < 81:
            color = "Green"
            text_color = (0, 255, 0)  # Green text color
        elif h_value < 132:
            color = "Blue"
            text_color = (255, 0, 0)  # Blue text color
        elif h_value < 170:
            color = "Violet"
            text_color = (255, 0, 255)  # Violet text color
        elif h_value >= 140 and h_value < 170:
            color = "Pink"
            text_color = (255, 192, 203)  # Pink text color

    # Get the size of the text
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(color, font, 1.5, 2)[0]

    # Calculate the position for the text to be centered
    text_x = (width - text_size[0]) // 2
    text_y = text_size[1] + 20  # Position at the top with a small margin

    # Draw a filled rectangle as the background for the text
    rectangle_bgr = (255, 255, 255)
    cv2.rectangle(frame, 
                  (text_x - 10, text_y - text_size[1] - 10), 
                  (text_x + text_size[0] + 10, text_y + 10), 
                  rectangle_bgr, 
                  cv2.FILLED)

    # Put the text on the frame
    cv2.putText(frame, color, (text_x, text_y), font, 1.5, text_color, 2)

    # Draw a circle at the center
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    # Display the resulting frame
    cv2.imshow("Frame", frame)

    # Wait for 1 ms and check if the Esc key (key code 27) is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




