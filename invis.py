import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

# Give camera time to warm up
time.sleep(2)

# Read one frame to get frame dimensions
ret, frame = cap.read()
if not ret:
    print("Camera not accessible")
    cap.release()
    exit()

frame = np.flip(frame, axis=1)
height, width = frame.shape[:2]

# Load background image from same folder
background = cv2.imread("background.jpeg")
if background is None:
    print("background.jpeg not found in the current folder")
    cap.release()
    exit()

# Resize and flip background to match webcam feed
background = cv2.resize(background, (width, height))
background = np.flip(background, axis=1)

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    img = np.flip(img, axis=1)

    # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # GREEN color range in HSV
    lower_green = np.array([25, 50, 30])
    upper_green = np.array([95, 255, 255])

    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Noise removal
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Invert mask
    mask_inv = cv2.bitwise_not(mask)

    # Extract foreground and background
    res1 = cv2.bitwise_and(img, img, mask=mask_inv)
    res2 = cv2.bitwise_and(background, background, mask=mask)

    # Combine both
    finalOutput = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Green Screen Effect", finalOutput)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
