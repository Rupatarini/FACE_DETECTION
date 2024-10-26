# Import necessary libraries
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

# Function to capture an image from the webcam
def take_photo(filename='captured_image.jpg'):
    # Ask the user to enter a key to capture the image
    input_key = input("Press 'c' when you are ready to capture the image: ")

    if input_key.lower() == 'c':  # Check if the entered key is 'c'
        js = Javascript('''
            async function takePhoto() {
                const video = document.createElement('video');
                const stream = await navigator.mediaDevices.getUserMedia({video: true});

                document.body.appendChild(video);
                video.srcObject = stream;
                await video.play();

                // Create a canvas to capture the image
                const canvas = document.createElement('canvas');
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                canvas.getContext('2d').drawImage(video, 0, 0);

                // Stop the video stream
                stream.getTracks().forEach(track => track.stop());
                video.remove();

                // Convert the canvas image to base64 and return
                return canvas.toDataURL('image/jpeg', 0.8);
            }
            takePhoto();
        ''')

        # Display the JavaScript to the user
        display(js)

        # Get the captured image data
        data = eval_js('takePhoto()')

        # Decode the base64 image and convert it into an OpenCV format image
        binary = b64decode(data.split(',')[1])
        image = np.array(Image.open(BytesIO(binary)))

        # Save the image using OpenCV
        cv2.imwrite(filename, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        print(f"Image saved as {filename}")
    else:
        print("Image capture canceled. You can run the code again when you're ready.")

# Call the function to capture an image
take_photo('captured_image.jpg')

