# Flower Classification using Convolutional Neural Networks (CNN)

## Project Overview

This project is focused on building a Convolutional Neural Network (CNN) model to classify images of flowers into 14 distinct categories. The dataset used contains over 13,000 images of flowers, ensuring a diverse and challenging set for the model to learn from. This project aims to achieve high accuracy on both training and validation datasets, following a set of predefined criteria to ensure a robust and well-generalized model.

## Dataset

### Dataset Description:

- The dataset contains 14 different categories of flowers:

| Categories Flowers     | Categories Flowers     |
|------------------------|------------------------|
| Astilbe                | Bellflower             |
| Black-Eyed Susan       | Calendula              |
| California Poppy       | Carnation              |
| Common Daisy           | Coreopsis              |
| Dandelion              | Iris                   |
| Rose                   | Sunflower              |
| Tulip                  | Water Lily             |

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
  
Model: **Sequential**
| Layer (type)                 | Output Shape   | Param #   |
|------------------------------|----------------|-----------|
| MobilenetV3large (Functional) | (None, 7, 7, 960) | 2,996,352 |
| conv2d (Conv2D)              | (None, 7, 7, 64)  | 553,024   |
| max_pooling2d (MaxPooling2D) | (None, 3, 3, 64)  | 0         |
| conv2d_1 (Conv2D)            | (None, 3, 3, 128) | 73,856    |
| max_pooling2d_1 (MaxPooling2D)| (None, 1, 1, 128) | 0         |
| flatten (Flatten)            | (None, 128)      | 0         |
| dropout (Dropout)            | (None, 128)      | 0         |
| dense (Dense)                | (None, 14)       | 1,806     |

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

<img src="https://github.com/shendyeff/learn-dicoding/blob/c5763b49534610b28748a60f3c24519ad7c383cf/Submission/Assets/Flower%20Image%20Classification/loss%20acc.png" width="1000">

| Epoch | Loss    | Accuracy | Val Loss | Val Accuracy |
|-------|---------|----------|----------|--------------|
| 0     | 0.905522| 0.736210 | 0.277265 | 0.918622     |
| 1     | 0.327626| 0.903977 | 0.165723 | 0.945748     |
| 2     | 0.206954| 0.938061 | 0.128094 | 0.961877     |
| 3     | 0.146846| 0.954279 | 0.105651 | 0.969941     |
| 4     | 0.109960| 0.968298 | 0.158723 | 0.958578     |
| 5     | 0.110463| 0.966648 | 0.123099 | 0.976173     |
| 6     | 0.099199| 0.972329 | 0.125565 | 0.974707     |
| 7     | 0.101633| 0.971413 | 0.092807 | 0.979106     |
| 8     | 0.052077| 0.984790 | 0.109990 | 0.979472     |
| 9     | 0.086612| 0.977369 | 0.128743 | 0.974340     |
| 10    | 0.070326| 0.979751 | 0.113604 | 0.982405     |
| 11    | 0.047733| 0.987539 | 0.127281 | 0.981305     |
| 12    | 0.057384| 0.985890 | 0.150161 | 0.976173     |

<img src="https://github.com/shendyeff/learn-dicoding/blob/c5763b49534610b28748a60f3c24519ad7c383cf/Submission/Assets/Flower%20Image%20Classification/accuracy%20epoch.png">

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
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(model_path="/content/tflite/model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Prepare the image
img_path = '6105173_d0b6a55d9e_c.jpg'
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array.astype('float32')

# Set the tensor to the image
interpreter.set_tensor(input_details[0]['index'], img_array)

# Run inference
interpreter.invoke()

# Get the output
output_data = interpreter.get_tensor(output_details[0]['index'])
predicted_class = np.argmax(output_data, axis=1)

print(f'Predicted class: {class_names[predicted_class[0]]}')

# Display the image and the prediction
plt.imshow(img)
plt.title(f'Predicted: {class_names[predicted_class[0]]}')
plt.axis('off')
plt.show()
```
### Prediction
<img src="https://github.com/shendyeff/learn-dicoding/blob/85f2947b2f1fff9393f58b07d681ea57d3e6db3b/Submission/Assets/Flower%20Image%20Classification/pred-rose.png" width="400">


