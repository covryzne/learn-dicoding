# 🎮 Sentiment Analysis Ulasan Mobile Legends: Bang Bang di Google Play Store

## 📌 Deskripsi Proyek

Proyek ini bertujuan untuk **menganalisis sentimen** ulasan pengguna **Mobile Legends: Bang Bang** yang dikumpulkan dari **Google Play Store**.  
Dengan menerapkan **Natural Language Processing (NLP)** dan **Machine Learning**, ulasan akan dikategorikan menjadi:

- **Positif** 😊
- **Netral** 😐
- **Negatif** 😡

Analisis ini dapat memberikan wawasan tentang **pengalaman pengguna**, **keluhan yang sering muncul**, serta **persepsi komunitas** terhadap game ini.

---

## ✅ Kriteria yang Dipenuhi

✔ **Scraping Data Secara Mandiri**

- Data dikumpulkan menggunakan **Google Play Scraper**.
- Minimal **3.000 sampel ulasan**, target **10.000+ ulasan**.

✔ **Preprocessing Data & Pelabelan Sentimen**

- **Cleaning teks**: hapus emoji, angka, simbol, dll.
- **Tokenization, stemming, dan stopword removal**.
- **Pelabelan sentimen** dengan **lexicon-based atau semi-supervised learning**.

✔ **Ekstraksi Fitur & Model Training**

- **TF-IDF** untuk Machine Learning.
- **Word2Vec / FastText** untuk Deep Learning.
- **3 model berbeda** dicoba:
  1. **SVM + TF-IDF**
  2. **Random Forest + Word2Vec**
  3. **LSTM + FastText**

✔ **Evaluasi Model**

- Target **akurasi ≥ 85%** pada **testing set**.
- Optimasi model **Deep Learning** untuk **akurasi > 92%**.

---

## 🛠 Metodologi Proyek

### 1️⃣ Scraping Data

Mengambil ulasan Mobile Legends dari **Google Play Store** dengan **Google Play Scraper**.

### 2️⃣ Preprocessing Data

- **Pembersihan teks** dari emoji, angka, simbol, dan kata tidak relevan.
- **Tokenization, stemming, dan stopword removal**.
- **Pelabelan sentimen** dengan **lexicon-based atau semi-supervised learning**.

### 3️⃣ Ekstraksi Fitur

- **TF-IDF** → Machine Learning (SVM, RF).
- **Word2Vec / FastText** → Deep Learning (LSTM).

### 4️⃣ Training & Evaluasi Model

- **SVM + TF-IDF (80/20 split)**
- **Random Forest + Word2Vec (80/20 split)**
- **LSTM + FastText (70/30 split)**

Evaluasi model dengan **accuracy, precision, recall, F1-score**.

### 5️⃣ Inference & Deployment

- Model diuji dengan data baru untuk **prediksi sentimen**.
- Output akhir: **positif, netral, atau negatif**.

---

## 🎯 Hasil yang Diharapkan

✅ **Dataset ulasan Mobile Legends** yang sudah diproses & dilabeli.  
✅ **Model Machine Learning / Deep Learning** dengan **akurasi ≥ 85%**.  
✅ **Grafik & word cloud** untuk visualisasi distribusi sentimen.  
✅ **File `.ipynb` atau `.py` untuk inference & testing model sentimen**.

---

## 🚀 Cara Menjalankan Proyek

### 📌 Prasyarat

Pastikan sudah menginstal **Python 3.x** dan pustaka berikut:

```bash
pip install google-play-scraper numpy pandas scikit-learn tensorflow nltk wordcloud matplotlib seaborn joblib
```
