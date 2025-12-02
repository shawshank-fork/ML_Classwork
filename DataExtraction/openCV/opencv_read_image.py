import cv2

img = cv2.imread("img.jpg")

if img is None:
    print("Image not found")
else:
    print("Image successfully loaded.")
    print(f"Shape: {img.shape}")  # (height, width, channels)
