# Submission 1: Nama Proyek Anda

Nama: `Shendi Teuku Maulana Efendi`

Username dicoding: `shendyeff`

|                         | Deskripsi                                                                       |
| ----------------------- | ------------------------------------------------------------------------------- |
| Dataset                 | [Spam Email Dataset](https://www.kaggle.com/datasets/mfaisalqureshi/spam-email) |
| Masalah                 | Deskripsi masalah yang di angkat                                                |
| Solusi machine learning | Deskripsi solusi machine learning yang akan dibuat                              |
| Metode pengolahan       | Deskripsi metode pengolahan data yang digunakan                                 |
| Arsitektur model        | Deskripsi arsitektur model yang diguanakan                                      |
| Metrik evaluasi         | Deksripsi metrik yang digunakan untuk mengevaluasi performa model               |
| Performa model          | Deksripsi performa model yang dibuat                                            |

## **Spam Email Machine Learning Pipeline**

## **Deskripsi Proyek**

Seiring dengan meningkatnya penggunaan pesan teks sebagai sarana komunikasi, spam menjadi salah satu masalah yang cukup mengganggu. Pesan spam sering kali berupa iklan, penipuan, atau konten yang tidak diinginkan oleh penerima. Oleh karena itu, diperlukan sistem otomatis yang dapat mengidentifikasi dan memisahkan pesan spam dari pesan yang sah secara akurat.

Proyek ini bertujuan untuk membangun Spam Email Machine Learning Pipeline menggunakan framework TensorFlow Extended (TFX). Pipeline ini akan mengotomatiskan seluruh proses pengolahan data, pelatihan model, validasi, hingga deployment model klasifikasi spam berbasis Neural Network.

## **Dataset**

Proyek ini menggunakan SMS Spam Collection Dataset, yang berisi kumpulan pesan SMS dengan label spam atau ham (bukan spam). Dataset ini akan melalui berbagai tahapan pemrosesan agar dapat digunakan untuk membangun model klasifikasi berbasis machine learning.

## **Tujuan Proyek**

- Mengembangkan pipeline machine learning yang dapat mengklasifikasikan pesan spam dan ham secara otomatis.
- Memanfaatkan TensorFlow Extended (TFX) untuk membuat pipeline yang modular, reproducible, dan scalable.
- Menggunakan teknik Natural Language Processing (NLP) untuk mengolah teks sebelum diklasifikasikan oleh model
- Menganalisis performa model menggunakan berbagai metrik evaluasi seperti AUC, Binary Accuracy, False Positive, dan False Negative.

## **Arsitektur Pipeline**

Pipeline ini terdiri dari beberapa tahap utama:

1. Data Ingestion: Mengimpor dataset ke dalam pipeline.

2. Data Validation:

   - Menghasilkan statistik ringkasan dari dataset.
   - Membuat skema data untuk mendeteksi anomali.
   - Mengidentifikasi inkonsistensi dalam data.

3. Data Preprocessing:

   - Membersihkan teks dan menormalkan format.
   - Mengubah label menjadi format numerik.
   - Melakukan tokenisasi dan vektorisasi teks.

4. Model Development:

- Mendesain dan melatih model klasifikasi berbasis Neural Network.

- Menggunakan embedding dan teknik NLP untuk meningkatkan akurasi model.<>

  5.Model Analysis & Validation:

Mengevaluasi model dengan TFX Evaluator.

Memastikan model memiliki performa yang stabil sebelum deployment.

Model Deployment:

Menggunakan TFX Pusher untuk mendistribusikan model ke lingkungan produksi.

Memastikan model dapat digunakan untuk inferensi secara real-time.

Metode Pengolahan Data

Konversi huruf kecil menggunakan tf.strings.lower untuk konsistensi.

Penghapusan tanda baca menggunakan metode lower_and_strip_punctuation dari TextVectorization.

Transformasi label ke format numerik (ham = 0, spam = 1) menggunakan tf.cast.

Arsitektur Model

Model yang digunakan memiliki beberapa lapisan utama:

TextVectorization: Mengubah teks menjadi token numerik.

Embedding Layer: Mengonversi token menjadi representasi vektor.

GlobalAveragePooling1D: Mereduksi dimensi vektor embedding.

Dense Layer dengan ReLU: Menangkap pola kompleks dari teks.

Output Layer dengan Sigmoid: Menghasilkan probabilitas klasifikasi spam atau ham.

Model dikompilasi menggunakan optimizer Adam dan dievaluasi dengan binary accuracy.

Metrik Evaluasi

Area Under Curve (AUC): Menilai performa model dalam membedakan spam dan ham.

Binary Accuracy: Mengukur seberapa banyak prediksi yang benar.

False Positive & False Negative: Mengukur kesalahan prediksi spam dan ham.

True Positive & True Negative: Menghitung jumlah prediksi yang benar untuk kedua kelas.

Performa Model

Model yang dikembangkan menunjukkan performa yang sangat baik dengan hasil berikut:

AUC: 0.96755

Binary Accuracy: 0.98225

False Negatives: 16

False Positives: 4

True Negatives: 977

True Positives: 130

Loss: 0.10437

Hasil ini menunjukkan bahwa model memiliki akurasi dan kemampuan prediksi yang tinggi dalam membedakan antara pesan spam dan non-spam. Dengan pipeline ini, pengguna dapat dengan mudah mengintegrasikan model ke dalam sistem produksi untuk mendeteksi spam secara otomatis.
