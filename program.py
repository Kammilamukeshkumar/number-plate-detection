import cv2
import numpy as np
import easyocr
from matplotlib import pyplot as plt

# Load the image
image_path = "/anpt7.jpg"
img = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area and get the largest contour
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Initialize the EasyOCR reader
reader = easyocr.Reader(["en"])

# Loop over the contours
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w / h > 4:  # Filter out non-rectangular contours
        continue
    roi = img[y:y + h, x:x + w]
    # Perform OCR on the region of interest (ROI)
    result = reader.readtext(roi, detail=0)
    if result:
        # Draw a rectangle around the detected number plate
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Display the detected number plate text
        cv2.putText(img, result[0], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# Display the image with the detected number plates and bordered lines
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Number Plate Detection with Bordered Lines")
plt.show()
