# **Project Pengembangan dan Pengoperasian Sistem Machine Learning: Studi Kasus Prediksi Berita Palsu**
`Nama: Shendi Teuku Maulana Efendi`  
`Username Dicoding: shendyeff`  

| | Deskripsi |
| ----------- | ----------- |
| 📂 **Dataset** | Dataset yang digunakan adalah **[Fake News Dataset](https://www.kaggle.com/datasets/hassanamin/textdb3)**, yang berisi berita dengan label apakah berita tersebut asli (`is_fake=0`) atau palsu (`is_fake=1`). Dataset memiliki beberapa fitur utama:<br> - **title** → Judul berita <br> - **text** → Isi lengkap berita <br> - **is_fake** → Label target (1 = berita palsu, 0 = berita asli) <br> Dataset ini telah di-preprocess agar lebih seimbang. |
| ❓ **Masalah** | Tantangan utama dalam proyek ini adalah **mendeteksi berita palsu secara otomatis**. Dengan penyebaran informasi yang luas di era digital, hoaks menjadi ancaman serius. Oleh karena itu, dibutuhkan **model machine learning** yang mampu membedakan antara berita asli dan berita palsu secara efektif. |
| 💡 **Solusi Machine Learning** | Model klasifikasi berbasis deep learning yang akan:<br> ✅ **Menganalisis teks berita** <br> ✅ **Melakukan ekstraksi fitur** dengan teknik `TextVectorization` dan `Embedding` <br> ✅ **Memprediksi apakah berita asli atau palsu** <br> ✅ **Di-deploy dalam sistem berbasis API** agar bisa digunakan secara real-time |
| ⚙️ **Metode Pengolahan** | Model dibangun menggunakan **TFX (TensorFlow Extended)** untuk membentuk **ML pipeline end-to-end**. <br> 🔹 **ExampleGen** → Membaca dataset dan membagi data (80% train, 20% val) <br> 🔹 **StatisticsGen** → Menganalisis distribusi data <br> 🔹 **SchemaGen** → Membuat skema fitur dataset <br> 🔹 **ExampleValidator** → Mengecek anomali dalam data <br> 🔹 **Transform** → Melakukan tokenisasi teks dan normalisasi data <br> 🔹 **Trainer** → Melatih model deep learning <br> 🔹 **Evaluator** → Mengevaluasi performa model <br> 🔹 **InfraValidator & Pusher** → Menguji model sebelum di-deploy |
| 🏗️ **Arsitektur Model** | Model menggunakan **arsitektur deep learning berbasis Neural Network**, dengan struktur sebagai berikut:<br> 1️⃣ **TextVectorization** → Konversi teks ke representasi numerik <br> 2️⃣ **Embedding Layer (16 dimensi)** → Representasi kata dalam ruang vektor <br> 3️⃣ **GlobalAveragePooling1D** → Merangkum informasi dari embedding <br> 4️⃣ **Dense Layer (64 neurons, ReLU activation)** <br> 5️⃣ **Dense Layer (32 neurons, ReLU activation)** <br> 6️⃣ **Output Layer (1 neuron, Sigmoid activation)** untuk memprediksi probabilitas berita palsu |
| 📊 **Metrik Evaluasi** | Model dievaluasi menggunakan metrik berikut:<br> - **Accuracy** → Seberapa sering model memberikan prediksi yang benar <br> - **Precision** → Seberapa banyak berita yang diklasifikasikan sebagai palsu benar-benar palsu <br> - **Recall** → Kemampuan model menangkap berita palsu <br> - **F1 Score** → Rata-rata harmonik dari precision & recall <br> - **AUC (Area Under Curve)** → Seberapa baik model membedakan antara berita asli dan palsu |
| 🚀 **Performa Model** | Hasil evaluasi pada dataset validasi menunjukkan:<br> - **Accuracy = 86.2% ✅** <br> - **Precision = 86.3% ✅** <br> - **Recall = 85.3% ✅** <br> - **F1 Score = 85.8% ✅** <br> Model sudah cukup baik dalam mendeteksi berita palsu, tetapi masih bisa dioptimalkan lebih lanjut dengan hyperparameter tuning. |
| ☁️ **Opsi Deployment** | Model di-deploy menggunakan **Railway** sebagai platform cloud. Railway memungkinkan kita menjalankan model sebagai **API** yang dapat menerima request prediksi dari user. |
| 🌐 **Web App** | Model dapat diakses melalui API berikut:<br> 🔗 **[Fake News Classification API](https://mlops-fake-news-production.up.railway.app/v1/models/fake-news-model/metadata)** <br> API ini bisa digunakan untuk melakukan **prediksi berita palsu** dengan mengirimkan request berisi teks berita. |
| 📈 **Monitoring** | Monitoring dilakukan menggunakan **Prometheus & Grafana** untuk melihat performa model setelah deployment.<br> - **Prometheus Metrics** → [🔗 Endpoint Prometheus](https://mlops-fake-news-production.up.railway.app/monitoring/prometheus/metrics) <br> - **Local Prometheus UI** → [`http://localhost:9090/`](http://localhost:9090/) <br> - **Status Prometheus** → [`http://localhost:9090/targets`](http://localhost:9090/targets) <br> - **Grafana** digunakan untuk visualisasi metrik |

# 🏃 How to Run - Fake News Detection ML Pipeline

## 📌 Prerequisites
Sebelum menjalankan proyek ini, pastikan lu udah install dependencies yang dibutuhkan:

### 1️⃣ **Install Python & Virtual Environment**
```bash
# Install Python versi terbaru (kalau belum)
sudo apt install python3 python3-venv python3-pip  # Linux
brew install python3                               # macOS
winget install Python.Python                      # Windows

# Buat virtual environment
python3 -m venv env

# Aktivasi virtual environment
source env/bin/activate  # Mac/Linux
env\Scripts\activate     # Windows
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🚀 Run ML Pipeline via Jupyter Notebook
Pipeline ini bisa dijalankan langsung lewat Jupyter Notebook (.ipynb). Pastikan environment udah ke-load dengan benar.

### 1️⃣ Jalankan Jupyter Notebook
```bash
jupyter notebook
```

Setelah Jupyter terbuka, buka file run_pipeline.ipynb dan jalankan semua cell secara berurutan.

### 🔄 Alternatif: Run Pipeline via Python Script
Kalau mau running tanpa notebook, bisa langsung pakai script Python.

### 1️⃣ Jalankan pipeline
```bash
python run_pipeline.py
```

## 🌐 API Model - Fake News Classification
Setelah training pipeline selesai, model akan otomatis di-deploy menggunakan Railway sebagai API.

## 🔗 API Endpoint:
```bash
https://mlops-fake-news-production.up.railway.app/v1/models/fake-news-model
```

## 🔍 Contoh Request Prediksi (via Jupyter Notebook)
```jupyter
import requests
import pandas as pd

balanced_df = pd.read_csv('.\data\\fake_or_real_news_balanced.csv')
random_row = balanced_df.sample(1).iloc[0]

data = {"instances": [{"text_xf": random_row['text']}]}
url = "https://mlops-fake-news-production.up.railway.app/v1/models/fake-news-model:predict"
response = requests.post(url, json=data)

prediction = response.json()

print(f"Text: {random_row['text']}")
print(f"Prediksi: {'Fake' if prediction['predictions'][0][0] < 0.5 else 'Real'}")
```
![Screenshot (123)](https://github.com/user-attachments/assets/01647267-b3cd-47fc-b8a8-ca60b06b4194)

## 📈 Monitoring dengan Prometheus & Grafana
Setelah model di-deploy, kita bisa memantau performanya menggunakan Prometheus dan Grafana.

### 1️⃣ Jalankan Prometheus (via Docker)
```bash
docker build -t fake-news-monitoring ./monitoring/
docker run -p 9090:9090 fake-news-monitoring
```

### 2️⃣ Cek Status Prometheus
- Prometheus Metrics → 🔗 [Endpoint Prometheus](https://mlops-fake-news-production.up.railway.app/monitoring/prometheus/metrics)
- Local Prometheus UI → [http://localhost:9090/](http://localhost:9090/)
- Status Prometheus → [http://localhost:9090/targets](http://localhost:9090/targets)

### 3️⃣ Grafana Dashboard 
![Grafana - Dashboard - All_Panel](https://github.com/user-attachments/assets/1aaf61b5-08d0-4eaf-8115-0adf33ca8b68)

