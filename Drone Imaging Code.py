import cv2
import numpy as np

# Define the image paths
image_paths = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "10.png", "11.png"]

# Define the colors for burnt and green grass
burnt_color = (0, 0, 255)  # red
green_color = (0, 255, 0)  # green

# Define the priority for blue and red houses
blue_priority = 2
red_priority = 1

# Initialize the lists to store the results
n_houses = []
priority_houses = []
rescue_ratios = []
image_by_rescue_ratio = []

# Loop through each image
for image_path in image_paths:
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of colors for burnt and green grass
    burnt_range = np.array([[0, 100, 100], [10, 255, 255]])
    green_range = np.array([[40, 100, 100], [80, 255, 255]])

    # Threshold the image to get the burnt and green grass
    burnt_mask = cv2.inRange(hsv_image, burnt_range[0], burnt_range[1])
    green_mask = cv2.inRange(hsv_image, green_range[0], green_range[1])

    # Create an output image with burnt and green grass highlighted
    output_image = image.copy()
    output_image[burnt_mask > 0] = burnt_color
    output_image[green_mask > 0] = green_color

    # Save the output image
    cv2.imwrite(f"output_{image_path}", output_image)

    # Find the contours of the houses
    contours, _ = cv2.findContours(burnt_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Initialize the counts for burnt and green houses
    burnt_houses = 0
    green_houses = 0
    burnt_priority = 0
    green_priority = 0

    # Loop through each contour
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # Check if the contour is a house
        if area > 100:
            # Check if the house is blue or red
            x, y, w, h = cv2.boundingRect(contour)
            roi = image[y:y+h, x:x+w]
            hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            blue_mask = cv2.inRange(hsv_roi, np.array([100, 100, 100]), np.array([130, 255, 255]))
            red_mask = cv2.inRange(hsv_roi, np.array([0, 100, 100]), np.array([10, 255, 255]))

            # Update the counts and priorities
            if np.count_nonzero(blue_mask) > np.count_nonzero(red_mask):
                burnt_houses += 1
                burnt_priority += blue_priority
            else:
                burnt_houses += 1
                burnt_priority += red_priority

    for contour in contours_green:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)

        # Check if the contour is a house
        if area > 100:
                        # Check if the house is blue or red
            x, y, w, h = cv2.boundingRect(contour)
            roi = image[y:y+h, x:x+w]
            hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            blue_mask = cv2.inRange(hsv_roi, np.array([100, 100, 100]), np.array([130, 255, 255]))
            red_mask = cv2.inRange(hsv_roi, np.array([0, 100, 100]), np.array([10, 255, 255]))

            # Update the counts and priorities
            if np.count_nonzero(blue_mask) > np.count_nonzero(red_mask):
                green_houses += 1
                green_priority += blue_priority
            else:
                green_houses += 1
                green_priority += red_priority

    # Calculate the rescue ratio
    if green_priority != 0:
        rescue_ratio = burnt_priority / green_priority
    else:
        rescue_ratio = 0

    # Append the results to the lists
    n_houses.append([burnt_houses, green_houses])
    priority_houses.append([burnt_priority, green_priority])
    rescue_ratios.append(rescue_ratio)
    image_by_rescue_ratio.append(image_path)

# Sort the images by rescue ratio
sorted_pairs = sorted(zip(rescue_ratios, image_by_rescue_ratio), reverse=True)
image_by_rescue_ratio = [pair[1] for pair in sorted_pairs]

# Print the results
print("Number of houses:")
for i, (burnt, green) in enumerate(n_houses):
    print(f"Image {i+1}: Burnt={burnt}, Green={green}")

print("\nPriority of houses:")
for i, (burnt, green) in enumerate(priority_houses):
    print(f"Image {i+1}: Burnt={burnt}, Green={green}")

print("\nRescue ratios:")
for i, ratio in enumerate(rescue_ratios):
    print(f"Image {i+1}: {ratio}")

print("\nImages sorted by rescue ratio:")
for image in image_by_rescue_ratio:
    print(image)
