# **Documentation Image Classification DICODING**
Create a neural network program using TensorFlow that is able to recognize hand shapes that form scissors, stones, or paper.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Approach](#2-approach)
3. [Data Collection](#3-data-collection)
4. [Import Libraries](#4-import-libraries)
5. [Load Dataset](#5-load-dataset)
6. [Extract Dataset](#6-extract-dataset)
7. [ImageDataGenerator with Augmentation and Validation Split](#7-imagedatagenerator-with-augmentation-and-validation-split)
8. [Check Number of Samples in Train and Validation Data](#8-check-number-of-samples-in-train-and-validation-data)
9. [Build Sequential Model using CNN](#9-build-sequential-model-using-cnn)
10. [Compile the Model](#10-compile-the-model)
11. [Implement Callback](#11-implement-callback)
12. [Train the Model](#12-train-the-model)
13. [Visualize Accuracy and Loss](#13-visualize-accuracy-and-loss)
14. [Evaluate the Model](#14-evaluate-the-model)
15. [Predict Image](#15-predict-image)
16. [Results](#16-results)

## 1. Introduction
Proyek ini bertujuan untuk mengembangkan model neural network menggunakan TensorFlow yang mampu mengenali bentuk tangan yang membentuk gunting, batu, atau kertas.

Dengan menggunakan dataset `rockpaperscissors`, proyek ini akan melatih model Convolutional Neural Network (CNN) untuk mengklasifikasikan gambar tangan ke dalam tiga kategori: gunting, batu, dan kertas. Proses ini mencakup beberapa langkah utama, mulai dari pengaturan lingkungan dan data augmentation, hingga pelatihan model dan evaluasi performa.

Proyek ini tidak hanya menunjukkan kemampuan TensorFlow dalam menangani tugas klasifikasi gambar, tetapi juga memberikan wawasan tentang teknik augmentasi data, penggunaan callback untuk menghindari overfitting, dan visualisasi kinerja model selama pelatihan.

## 2. Approach
Dalam proyek ini, kami menggunakan pendekatan berbasis Convolutional Neural Network (CNN) untuk mengklasifikasikan gambar tangan. CNN adalah jenis deep learning yang sangat efektif untuk tugas-tugas yang melibatkan data gambar karena kemampuannya dalam menangkap fitur spasial dan hierarki fitur dari gambar.

Langkah-langkah utama yang diikuti dalam proyek ini meliputi:
- Collection and preprocess data
- Augmentasi data untuk meningkatkan keberagaman dataset
- Pembangunan model CNN dengan beberapa lapisan konvolusi dan pooling
- Penggunaan teknik callback untuk mencegah overfitting
- Pelatihan dan evaluasi model
- Visualisasi kinerja model
- Prediksi pada gambar baru

## 3. Data Collection
Dataset yang digunakan dalam proyek ini adalah `rockpaperscissors`, yang berisi gambar tangan yang menunjukkan bentuk gunting, batu, dan kertas. Dataset ini bisa diakses pada [Kaggle](https://www.kaggle.com/drgfreeman/rockpaperscissors) atau disediakan oleh [Dicoding](https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip).

Langkah-langkah pengumpulan data meliputi:
- Mengunduh dataset `rockpaperscissors.zip` dari [Kaggle](https://www.kaggle.com/drgfreeman/rockpaperscissors) atau [Dicoding](https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip)
- Mengekstrak file zip untuk mendapatkan gambar dalam format yang dapat digunakan

## 4. Import Libraries
```python
import tensorflow as tf
import zipfile, os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline
```

## 5. Load dataset
```python
!wget --no-check-certificate \
  https://github.com/dicodingacademy/assets/releases/download/release/rockpaperscissors.zip \
  -O /tmp/rockpaperscissors.zip
```

## 6. Extract dataset
```python
local_zip = '/tmp/rockpaperscissors.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp')
zip_ref.close()

base_dir = '/tmp/rockpaperscissors/rps-cv-images'
```

## 7. ImageDataGenerator with Augmentation and Validation Split
```python
train_datagen = ImageDataGenerator(
     rescale = 1./255,
     rotation_range = 50,
     width_shift_range = 0.2,
     height_shift_range = 0.2,
     zoom_range = 0.2,
     horizontal_flip = True,
     shear_range = 0.2,
     fill_mode = 'nearest',
     validation_split = 0.4  # 40% validation split
 )

validation_datagen = ImageDataGenerator(
    rescale = 1.0/255,
    validation_split = 0.4
)

train_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'categorical',
    subset = 'training'
)

validation_generator = validation_datagen.flow_from_directory(
    base_dir,
    target_size = (150,150),
    batch_size = 32,
    class_mode = 'categorical',
    subset = 'validation'
)
```

## 8. Check Number of Samples in Train and Validation Data
```python
print(f"Number of training samples: {train_generator.samples}")
print(f"Number of validation samples: {validation_generator.samples}")
```
Dari ukuran pembagian data validasi 40% dari total dataset, ditemukan: Data training memiliki 1314 sampel gambar dengan 3 class, dan Data validasi memiliki 874 sampel gambar dengan 3 class. Setelah data kita telah siap, kita bisa membangun arsitektur sebuah CNN.

## 9. Build Sequential Model using CNN
```python
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(3, activation='softmax')
])
```
cek summary pada model sequential yang telah dibuat
```python
model.summary()
```

## 10. Compile the model
```python
model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)
```
Dikarenakan membagi 3 class maka loss function yang digunakan adalah `categorical_crossentropy`

## 11. Implement Callback
Menggunakan `EarlyStopping` callback dari TensorFlow untuk menghentikan pelatihan lebih awal jika performa pada data validasi tidak membaik setelah beberapa epoch, mencegah overfitting.
```python
callback = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
```

## 12. Train the Model
Melatih model dengan data pelatihan dan validasi, menggunakan callback untuk menghentikan pelatihan jika diperlukan.
```python
history = model.fit(
    train_data,
    steps_per_epoch=train_data.samples // 32,
    validation_data=val_data,
    validation_steps=val_data.samples // 32,
    epochs=25,
    callbacks=[callback]
)
```

## 13. Visualize Accuracy and Loss
Membuat plot untuk melihat perubahan akurasi dan loss pada data pelatihan dan validasi selama pelatihan.
```python
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(len(acc))

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
```

## 14. Evaluate the Model
Evaluasi model pada data validasi untuk mengukur performa akhir model.
```python
results = model.evaluate(val_data)
print(f"Validation Loss: {results[0]}")
print(f"Validation Accuracy: {results[1]}")
```

## 15. Predict Image
Menggunakan model untuk memprediksi gambar baru dan menentukan kelasnya.
```python
img = image.load_img('path_to_image', target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array /= 255.

prediction = model.predict(img_array)
class_names = ['paper', 'rock', 'scissors']
print(f"Predicted class: {class_names[np.argmax(prediction)]}")
```

## 16. Results
Model yang telah dilatih mampu mengenali bentuk tangan dengan akurasi yang baik. Evaluasi model menunjukkan hasil yang baik pada data validasi, dan contoh prediksi menunjukkan kemampuan model untuk mengklasifikasikan gambar baru dengan benar.
