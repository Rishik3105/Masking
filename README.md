🎭 Image Masking with OpenCV 🚀

🖼️ Overview

This Python script demonstrates the use of OpenCV for applying circular and rectangular masking to an image. Masking is a crucial technique in image processing where specific portions of an image are highlighted or isolated for further analysis.

With this code, you can:

Apply circular masking to center-focus on an area.

Apply rectangular masking to emphasize a specific region.

🛠️ Features

🔘 Circular Masking: Highlights a circular area around the center of the image.

⬛ Rectangular Masking: Creates a rectangular focus on the center of the image.

💡 Dynamic Shape Options: Choose the type of masking dynamically via user input.

📜 Usage Instructions

Prerequisites

Ensure you have Python and the required libraries installed:

pip install opencv-python numpy

Running the Script

Clone or copy the script to your local system.

Save your image in the appropriate directory.

Execute the script:

python masking_script.py

Follow the prompts:

Enter your choice: 1 for circular masking, 2 for rectangular masking.

Provide the path to your image file.

View the output as separate masked images.

🧑‍💻 Code Walkthrough

🔍 Core Functionalities

Image Input: Reads the image using cv.imread().

Blank Mask Creation: Generates a blank mask with the same dimensions as the input image:

blank = np.zeros(img.shape[:2], dtype='uint8')

Mask Application:

Circular Mask:

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img, img, mask=circle)

Rectangular Mask:

rectangle = cv.rectangle(blank, (x_start, y_start), (x_end, y_end), 255, -1)

masked = cv.bitwise_and(img, img, mask=rectangle)

🛠️ Technical Details

Bitwise Operations: Masks are applied using cv.bitwise_and() for pixel-wise operations.

Dynamic Dimensions: Mask positions are calculated dynamically using image dimensions.

Visualization: cv.imshow() is used to display the original and masked images.

🎨 Demo

Original Image

Circular Masking

Rectangular Masking

🔗 Resources

📖 OpenCV Documentation

🎥 OpenCV Tutorials on YouTube

🛡️ License
This script is open-source under the MIT License. Feel free to fork and enhance it!







