# Handwritten Digit Recognition Project

![Digit Recognition Process](images/model.png)

This project implements a Convolutional Neural Network (CNN) to recognize handwritten digits using the MNIST dataset. It also provides a simple interface for users to upload an image or capture one via webcam (optional, if permissions allow) to identify handwritten digits.

---

## Recognition Process Overview
The digit recognition process involves the following steps:
1. **Image Input**: Original image of a handwritten digit (e.g., `125x125` resolution).
2. **Normalization**: Preprocessing and resizing the image to a standard size (`20x20` or `28x28` depending on the model).
3. **Feature Extraction**: Extracting pixel features for model processing.
4. **Model Prediction**: CNN-based model predicts the digit.
5. **Result Output**: The recognized digit is displayed.

---

## Features
- **Train**: A CNN is trained using the MNIST dataset.
- **Model Saving**: The trained model is saved for future predictions.
- **Predict**: Identify handwritten digits from uploaded images or webcam captures.
- **Interactive User Interface**: Upload images and get predictions in real-time.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries**: 
  - TensorFlow/Keras
  - OpenCV
  - PIL (Pillow)
- **Tools**:
  - Virtual Environment for dependency management
  - Git for version control

---

## Directory Structure
```
├── digit_recognition_webcam.py   # Main script for predictions
├── digit_recognition_model.h5    # Trained model
├── images/                       # Folder containing images for the README
│   └── model.png                 # Process diagram
├── requirements.txt              # Dependencies
└── README.md                     # Project documentation
```

---

## Installation and Setup
1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/handwritten-digit-recognition.git
   cd handwritten-digit-recognition
   ```

2. Set up a virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python digit_recognition_webcam.py
   ```

---

## Usage
1. **Train the Model (Optional)**: 
   Train the model using the MNIST dataset and save it as `digit_recognition_model.h5`.

2. **Predict**:
   - Upload an image of a handwritten digit.
   - The application preprocesses the image and predicts the digit using the trained model.

---

## Example Results
| Prediction Example | Training Accuracy |
|--------------------|-------------------|
| ![Example Image](images/example_prediction.png) | ![Training Graph](images/example_accuracy.png) |

---

## Contribution
Feel free to contribute to this project by:
1. Submitting bug fixes.
2. Suggesting enhancements or new features.
3. Optimizing the CNN architecture.

---

## License
This project is licensed under the MIT License
