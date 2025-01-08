import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained model
model_path = os.path.join("/Users/user/Desktop/digital_recognition_model", "digit_recognition_model.h5")
model = load_model(model_path)

# Function to preprocess the uploaded image
def preprocess_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    # Resize the image to 28x28 pixels
    resized = image.resize((28, 28))
    # Convert the image to a NumPy array and normalize pixel values
    array = np.array(resized) / 255.0
    # Reshape the array to match the model input shape
    reshaped = array.reshape(1, 28, 28, 1)
    return reshaped

# Main function for image upload and prediction
def main():
    print("Welcome to the Handwritten Digit Recognizer!")
    image_path = input("Please provide the path to your image file (e.g., /path/to/image.png): ")

    # Validate the provided path
    if not os.path.exists(image_path):
        print("Error: File not found. Please check the file path.")
        return

    if not os.path.isfile(image_path):
        print("Error: The provided path is not a file. Please provide a valid image file.")
        return

    try:
        # Preprocess the image
        input_image = preprocess_image(image_path)

        # Predict the digit
        prediction = model.predict(input_image)
        predicted_digit = np.argmax(prediction)

        print(f"The model predicts this digit as: {predicted_digit}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
