# Flower Classification using Convolutional Neural Networks (CNN)

## Project Overview

This project focuses on developing a Convolutional Neural Network (CNN) model for classifying images of flowers into 14 different categories. Utilizing over 24,000 high-resolution images, the dataset provides a diverse and challenging foundation for training a robust model. The model is built using Transfer Learning with MobileNetV3Large as the base architecture, followed by custom convolutional and dense layers to enhance feature extraction and classification capabilities. To ensure effective learning and generalization, the dataset is split into 70% for training, 15% for validation, and 15% for testing. The model is trained with appropriate callbacks like EarlyStopping and ModelCheckpoint to avoid overfitting and preserve the best performance. Additionally, the trained model is exported into multiple formats — SavedModel, TensorFlow Lite (TFLite), and TensorFlow.js (TFJS) — making it suitable for deployment on various platforms such as web browsers, mobile devices, and cloud-based systems. The project aims to achieve high accuracy across all data splits while ensuring model compatibility and portability for real-world applications.

## Dataset
`Link Dataset!` <br>
[![Google Drive Dataset](https://img.shields.io/badge/Download%20Dataset-Google%20Drive-blue?style=for-the-badge&logo=google-drive)](https://drive.google.com/file/d/1m9UBYCzLElZ8x_-b_jysE7A9y-jSq04u/view?usp=drive_link)

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

- The total number of images in the dataset exceeds 24.000, ensuring the dataset meets the required minimum of 10000 images.
- The images are divided into a training set (70%), validation set (15%), and test set (15%) to evaluate the model's performance effectively.

### Dataset Splitting:

The dataset is divided into three subsets to ensure optimal training and evaluation of the model:

- `Training Set (70%)`
  Used to train the model by allowing it to learn patterns from each image class.

- `Validation Set (15%)`
  Used to evaluate the model's performance during training and help prevent overfitting.

- `Test Set (15%)`
  Used to assess the final performance of the model after training, ensuring it can generalize well to unseen data.

## Model Architecture

### Model Type:

- A Sequential model is used, which is the simplest way to build a neural network in TensorFlow/Keras.

### Layers:

- **Conv2D Layers:** Multiple convolutional layers are used to extract features from the images.
- **Pooling Layers:** MaxPooling layers are employed to reduce the spatial dimensions of the feature maps, which helps in reducing the computation and controlling overfitting.
- **Dropout Layer:** A dropout layer is added to prevent overfitting by randomly setting a fraction of input units to 0 at each update during training.
- **Dense Layer:** The final dense layer with a softmax activation function outputs the probabilities of each class.
  
<p align="center">
  <img src="https://github.com/user-attachments/assets/ce51c235-58d3-4018-98e6-ca77edeac64d" width="600">
</p>

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

<img src="https://github.com/user-attachments/assets/fce6a862-7a82-4077-9c72-e01c2ac7128b" width="1000"> <br>

| Epoch | Accuracy | Loss   | Val Accuracy | Val Loss |
|-------|----------|--------|--------------|----------|
| 1     | 0.6352   | 1.3132 | 0.9267       | 0.2364   |
| 2     | 0.8983   | 0.3423 | 0.9578       | 0.1328   |
| 3     | 0.9225   | 0.2568 | 0.9642       | 0.1099   |
| 4     | 0.9465   | 0.1880 | 0.9805       | 0.0711   |
| 5     | 0.9601   | 0.1340 | 0.9768       | 0.0822   |
| 6     | 0.9657   | 0.1098 | 0.9854       | 0.0598   |
| 7     | 0.9722   | 0.0905 | 0.9799       | 0.0814   |
| 8     | 0.9746   | 0.0808 | 0.9803       | 0.0793   |
| 9     | 0.9746   | 0.0976 | 0.9719       | 0.1277   |
| 10    | 0.9756   | 0.0916 | 0.9901       | 0.0432   |
| 11    | 0.9806   | 0.0764 | 0.9873       | 0.0553   |
| 12    | 0.9774   | 0.0903 | 0.9869       | 0.0587   |
| 13    | 0.9846   | 0.0623 | 0.9854       | 0.0595   |
| 14    | 0.9868   | 0.0486 | 0.9874       | 0.0670   |
| 15    | 0.9866   | 0.0507 | 0.9908       | 0.0584   |

<br>
<img src="https://github.com/user-attachments/assets/6335546f-914c-4717-9754-36773552f2df">

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
# Load the TFLite model using tf.lite.Interpreter
interpreter = tf.lite.Interpreter(model_path='tflite/model.tflite')
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Path gambar yang di-upload
img_path = "/content/dataset_split/test/iris/164507281_f5c9796e11_c.jpg"  # Nama file yang di-upload

# Load dan preprocess gambar yang di-upload
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Set input tensor and invoke the interpreter
interpreter.set_tensor(input_details[0]['index'], img_array)
interpreter.invoke()

# Get the output tensor
predictions = interpreter.get_tensor(output_details[0]['index'])

# Get predicted class
predicted_class = np.argmax(predictions, axis=1)

predicted_label = class_names[predicted_class[0]]

# Display the image and prediction
plt.imshow(img)
plt.title(f'Predicted: {predicted_label}')
plt.axis('off')
plt.show()
```

### Prediction Result
<img src="https://github.com/user-attachments/assets/38d61f39-0eff-4039-8784-a89c8f114559" width="400">

