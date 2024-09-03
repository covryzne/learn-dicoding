# Flower Classification using Convolutional Neural Networks (CNN)

## Project Overview

This project is focused on building a Convolutional Neural Network (CNN) model to classify images of flowers into 14 distinct categories. The dataset used contains over 13,000 images of flowers, ensuring a diverse and challenging set for the model to learn from. This project aims to achieve high accuracy on both training and validation datasets, following a set of predefined criteria to ensure a robust and well-generalized model.

## Dataset

### Dataset Description:

- The dataset contains 14 different categories of flowers:
  - Astilbe
  - Bellflower
  - Black-Eyed Susan
  - Calendula
  - California Poppy
  - Carnation
  - Common Daisy
  - Coreopsis
  - Dandelion
  - Iris
  - Rose
  - Sunflower
  - Tulip
  - Water Lily
- The total number of images in the dataset exceeds 13,000, ensuring the dataset meets the required minimum of 10000 images.
- The images are divided into a training set (80%) and a validation/test set (20%) to evaluate the model's performance effectively.

### Dataset Splitting:

- **Training Set:** 80% of the dataset is used for training the model.
- **Validation Set:** 20% of the dataset is used for validating the model's performance.

## Model Architecture

### Model Type:

- A Sequential model is used, which is the simplest way to build a neural network in TensorFlow/Keras.

### Layers:

- **Conv2D Layers:** Multiple convolutional layers are used to extract features from the images.
- **Pooling Layers:** MaxPooling layers are employed to reduce the spatial dimensions of the feature maps, which helps in reducing the computation and controlling overfitting.
- **Dropout Layer:** A dropout layer is added to prevent overfitting by randomly setting a fraction of input units to 0 at each update during training.
- **Dense Layer:** The final dense layer with a softmax activation function outputs the probabilities of each class.

### Activation Functions:

- ReLU is used as the activation function for hidden layers.
- Softmax is used in the output layer to produce probability distributions over the classes.

### Training Criteria:

- The model aims to achieve at least 95% accuracy on both the training and validation sets.

## Training & Evaluation

### Training Process:

- The model is trained using the Adam optimizer, with categorical cross-entropy as the loss function.
- EarlyStopping and ModelCheckpoint callbacks are utilized to monitor the training process and save the best model based on validation accuracy.

### Performance Metrics:

- The model's performance is evaluated based on accuracy and loss on both the training and validation sets.
- The goal is to achieve at least 95% accuracy on both datasets.

### Results:

- The model successfully reached the target accuracy, demonstrating its capability to generalize well on unseen data.

## Visualizations

### Accuracy and Loss Plots:

- During the training process, plots for accuracy and loss over epochs are generated to visualize the model's learning process.
- These plots help in understanding how well the model is fitting the data and whether there are any signs of overfitting or underfitting.

## Model Deployment

### Model Formats:

- The trained model is saved in multiple formats to ensure flexibility in deployment across different platforms:
  - **SavedModel:** The default format for TensorFlow models, suitable for server-side deployment.
  - **TF-Lite:** A lightweight format optimized for mobile and embedded devices.
  - **TFJS:** A format that allows the model to be run in a browser using TensorFlow.js, making it accessible for web applications.

## How to Use

### Inference:

- To perform inference, load the trained model and preprocess an image to be classified. The model will output the predicted class along with its probability.

### Example Code:

```python
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v3 import preprocess_input
import numpy as np

# Load the trained model
model = tf.keras.models.load_model('model.h5')

# Load and preprocess the image
img_path = 'path_to_your_image.jpg'
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Perform inference
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions, axis=1)
```
