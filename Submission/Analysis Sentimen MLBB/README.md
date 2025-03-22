# 🎮 Sentiment Analysis: Mobile Legends User Reviews 🔥

## 📌 Deskripsi Proyek

Mobile Legends: Bang Bang adalah salah satu game **MOBA (Multiplayer Online Battle Arena)** paling populer di dunia, tetapi ulasan pengguna di **Google Play Store** mencerminkan berbagai pengalaman yang berbeda—dari **pujian setinggi langit** hingga **keluhan penuh emosi**.  

Proyek ini bertujuan untuk **menganalisis sentimen pengguna** berdasarkan ulasan mereka menggunakan teknik **Natural Language Processing (NLP) & Machine Learning serta Deep Learning**. Dengan memahami pola sentimen pengguna, kita bisa mengidentifikasi:

✅ **Aspek game yang disukai pengguna** (grafik, hero, gameplay, dll.).  
✅ **Keluhan paling sering muncul** (bug, lag, matchmaking, dll.).  
✅ **Tren sentimen komunitas** dari waktu ke waktu.  

### 🎯 **Apa yang Akan Kita Lakukan?**
🔹 **Scraping data ulasan** langsung dari Google Play Store.  
🔹 **Membersihkan & memproses teks ulasan** agar siap untuk analisis.  
🔹 **Melabeli sentimen** menjadi **Positif 😍 | Netral 😐 | Negatif 😡**.  
🔹 **Membangun model Machine Learning & Deep Learning** untuk klasifikasi sentimen.  
🔹 **Menganalisis tren sentimen** & visualisasi menggunakan **word cloud**.  

---

## 🏆 **Hasil yang Diharapkan**

🎯 **Dataset ulasan Mobile Legends** yang telah diproses & dilabeli.  
🎯 **Model Machine Learning & Deep Learning** dengan akurasi **≥ 85%**.  
🎯 **Grafik & word cloud** untuk memahami distribusi sentimen.  
🎯 **Script inference untuk testing model** dengan data baru.  

🔥 **Hasil akhirnya? Kita bisa mengetahui apa yang sebenarnya dipikirkan para pemain tentang Mobile Legends!** 🎮🚀

---

## ✅ Kriteria yang Dipenuhi

### ✔ **Scraping Data Secara Mandiri**
- Data dikumpulkan menggunakan **Google Play Scraper**.
- **10.000 sampel ulasan**.

### ✔ **Preprocessing Data & Pelabelan Sentimen**
- **Cleaning teks**: hapus emoji, angka, simbol, dll.
- **Tokenization, stemming, dan stopword removal**.
- **Pelabelan sentimen** menggunakan **lexicon-based atau semi-supervised learning**.

### ✔ **Ekstraksi Fitur & Model Training**
- **TF-IDF** → untuk model Machine Learning.
- **Word2Vec / FastText** → untuk model Deep Learning.
- **3 model berbeda** digunakan:
  1. **Word2Vec + Random Forest** (Split 80:20)
  2. **TF-IDF + SVM** (Split 80:20)
  3. **Word Embedding + LSTM** (Split 80:20)

### ✔ **Evaluasi Model**
- Target **akurasi ≥ 85%** pada **testing set**.
- Optimasi model **Deep Learning** untuk mencapai **akurasi > 92%**.

---

## 🛠 Metodologi Proyek

### 🔹 **1️⃣ Scraping Data**
Mengambil ulasan **Mobile Legends: Bang Bang** dari **Google Play Store** menggunakan **Google Play Scraper**.

### 🔹 **2️⃣ Preprocessing Data**
- **Pembersihan teks** dari emoji, angka, simbol, dan kata tidak relevan.
- **Tokenization, stemming, dan stopword removal**.
- **Pelabelan sentimen** menggunakan **lexicon-based atau semi-supervised learning**.

### 🔹 **3️⃣ Ekstraksi Fitur**
- **TF-IDF** → Digunakan untuk model **Machine Learning** (SVM, RF).
- **Word2Vec / FastText** → Digunakan untuk model **Deep Learning** (LSTM).

### 🔹 **4️⃣ Training & Evaluasi Model**
Model yang digunakan:
- **Word2Vec + Random Forest** (Split 80:20)
- **TF-IDF + SVM** (Split 80:20)
- **Word Embedding + LSTM** (Split 80:20)

Evaluasi model menggunakan metrik:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

### 🔹 **5️⃣ Inference & Deployment**
- Model diuji dengan **data baru** untuk **prediksi sentimen**.
- Output akhir: **Positif 😊 | Netral 😐 | Negatif 😡**.

---


## 🚀 Cara Menjalankan Proyek

### 📌 Prasyarat

Pastikan Anda sudah menginstal **Python 3.x** di sistem Anda.

### 📌 Instalasi & Setup Virtual Environment

Disarankan untuk menjalankan proyek dalam **virtual environment** agar lebih terorganisir.

1️⃣ **Buat Virtual Environment**  

Jalankan perintah berikut untuk membuat environment baru:

```bash
python -m venv env
```

2️⃣ **Aktifkan Virtual Environment**

```bash
env\Scripts\activate
```

3️⃣ Instal Dependensi

Setelah environment aktif, install semua dependensi proyek:

```bash
pip install -r requirements.txt
```

## 📞 Contact

Jika ada pertanyaan atau ingin berdiskusi lebih lanjut, hubungi saya di:

- **GitHub**: [github.com/covryzne](https://github.com/covryzne)
- **LinkedIn**: [linkedin.com/in/shendyeff](https://linkedin.com/in/shendyeff)
- **Email**: shendyteuku2@gmail.com

🔥 Feel free to connect & collaborate! 🚀

