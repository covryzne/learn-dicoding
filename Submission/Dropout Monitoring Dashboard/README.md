# Final Project: Solving Dropout Issues in an Edutech Company

## Business Understanding

Jaya Jaya Institut adalah lembaga pendidikan tinggi berbasis edutech yang mengalami tantangan serius dalam mempertahankan mahasiswa hingga lulus. Tingginya tingkat dropout tidak hanya berdampak pada reputasi institusi, tetapi juga menyebabkan kerugian finansial dan rendahnya efisiensi operasional. Oleh karena itu, institusi membutuhkan sistem yang mampu memprediksi kemungkinan mahasiswa berhenti kuliah secara dini, agar dapat dilakukan intervensi yang tepat waktu.

## Permasalahan Bisnis

Jaya Jaya Institut menghadapi permasalahan serius terkait tingginya tingkat mahasiswa yang mengalami dropout dari semester ke semester. Fenomena ini berdampak signifikan terhadap reputasi institusi dan keberlanjutan finansial operasional kampus. Sayangnya, hingga saat ini, belum tersedia sistem prediktif yang mampu mengidentifikasi secara dini mahasiswa yang memiliki risiko tinggi untuk berhenti kuliah. Hal ini menyebabkan institusi kesulitan untuk melakukan intervensi secara tepat waktu dan personal.

Selain itu, pengambilan keputusan strategis oleh manajemen institusi sering kali tidak berbasis pada data historis yang akurat dan terstruktur. Ketiadaan alat bantu analisis yang komprehensif membuat proses evaluasi kinerja akademik dan sosial mahasiswa menjadi kurang optimal. Terlebih lagi, kurangnya visualisasi data yang intuitif menyulitkan pemangku kebijakan dalam memahami pola-pola penting yang tersembunyi dalam data. Oleh karena itu, dibutuhkan solusi berbasis machine learning dan visual analytics untuk membantu institusi dalam mengatasi tantangan ini secara lebih terukur dan efisien.

## Cakupan Proyek

Pada proyek ini, dilakukan beberapa tahap utama untuk menyelesaikan permasalahan dropout mahasiswa di Jaya Jaya Institut, yaitu:

1. Business Understanding <br>
Mengidentifikasi konteks permasalahan dropout mahasiswa yang berdampak pada kualitas pendidikan dan reputasi institusi, serta kebutuhan akan sistem prediktif untuk mendukung intervensi dini oleh pihak manajemen.

2. Data Understanding & Preparation <br>
Melakukan eksplorasi awal terhadap dataset historis mahasiswa, mengidentifikasi dan menangani nilai yang hilang, outlier, serta melakukan transformasi fitur seperti encoding dan feature engineering untuk menyiapkan data yang layak digunakan pada proses modeling.

3. Exploratory Data Analysis (EDA) <br>
Menganalisis distribusi dan pola dropout berdasarkan fitur-fitur penting seperti tingkat pendidikan orang tua, status beasiswa, gender, nilai akademik, dan kondisi ekonomi, guna menemukan insight yang relevan.

4. Modeling <br>
Membangun beberapa model prediksi dropout seperti Random Forest, XGBoost, dan Gradient Boosting. Model-model tersebut kemudian dibandingkan kinerjanya menggunakan metrik seperti akurasi, F1-score, precision dan recall.

5. Evaluation <br>
Memilih model terbaik berdasarkan hasil evaluasi dan menginterpretasikan fitur-fitur yang paling berpengaruh terhadap kemungkinan mahasiswa mengalami dropout.

6. Script Prediction & Deployment Preparation <br>
Menyusun script inference berbasis Python dengan memuat model terbaik yang telah disimpan dalam format .pkl, serta preprocessing yang konsisten menggunakan scaler.pkl dan feature_columns.pkl. Model ini kemudian diintegrasikan ke dalam sebuah aplikasi user-friendly berbasis Streamlit, di mana pengguna dapat menginput data mahasiswa (seperti nilai akademik, status beasiswa, usia saat mendaftar, dan faktor sosial ekonomi lainnya) melalui antarmuka web. Aplikasi ini telah berhasil dideploy ke Streamlit Community Cloud, sehingga dapat diakses secara remote oleh stakeholder dan reviewer untuk melakukan prediksi secara langsung terhadap kemungkinan seorang mahasiswa mengalami dropout.

7. Dashboard Development <br>
Mengembangkan dashboard interaktif berbasis Looker Studio yang terhubung dengan database Supabase. Dashboard ini digunakan untuk menampilkan statistik dropout, tren berdasarkan gender, beasiswa, nilai masuk, dan metrik akademik lainnya secara real-time.
 
8. Recommendation <br>
Memberikan rekomendasi aksi berbasis data kepada pihak kampus, seperti menguatkan program beasiswa, memperbaiki sistem monitoring akademik, serta intervensi sosial untuk kelompok mahasiswa berisiko tinggi.

## Persiapan

### Sumber Data
Dataset berasal dari data internal mahasiswa Jaya Jaya Institut, terdiri dari informasi demografis, akademik, serta kondisi sosial ekonomi.

Link dataset bisa diakses di dibawah ini: <br> <br>
[![GitHub - education_data.csv](https://img.shields.io/badge/GitHub-Dataset-black?logo=github)]()

### Setup Environment

Untuk menyiapkan lingkungan (environment) yang diperlukan untuk menjalankan aplikasi dan model prediksi dropout, Anda dapat mengikuti langkah-langkah berikut:

1. Buat environment baru dengan Conda

Jalankan perintah berikut untuk membuat environment baru bernama dropout-prediction menggunakan Python 3.9.15 <br>
```
conda create -n dropout-prediction python=3.9.15
```

2. Aktifkan environment yang telah dibuat

Setelah environment berhasil dibuat, aktifkan environment tersebut dengan perintah berikut<br>

```
conda activate dropout-prediction
```

3. Install dependencies

Setelah environment aktif, install semua dependensi yang diperlukan untuk menjalankan aplikasi dan model prediksi dropout. Anda dapat menggunakan file `requirements.txt` yang sudah disediakan dalam proyek ini <br>

```
pip install -r requirements.txt
```

## Dashboard

Dashboard interaktif dibuat menggunakan Looker Studio untuk membantu manajemen memantau tren dropout, melakukan analisis berdasarkan faktor-faktor penting seperti usia, latar belakang pendidikan, status pembayaran, dan lainnya.

Dashboard bisa diakses pada link dibawah: <br><br>
[![Built with Looker Studio](https://img.shields.io/badge/Built%20with-Looker%20Studio-4285F4?style=for-the-badge&logo=googleanalytics&logoColor=white)](https://lookerstudio.google.com/reporting/d3df41d2-81cc-49a6-b147-211f7f8ff911)

![Screenshot (453)](https://github.com/user-attachments/assets/6230cb24-ced8-4f00-a439-2c6a2ebd182e)
![Screenshot (454)](https://github.com/user-attachments/assets/f34ecabe-33e1-4973-b8e1-e24afdb5552e)


## Menjalankan Sistem Machine Learning
Prototype sistem prediksi dropout dikembangkan menggunakan Streamlit, yang memungkinkan pengguna memasukkan data mahasiswa dan mendapatkan prediksi secara real-time.

🔗 Coba Prototype Streamlit (https://dropout-prediction-submission-2-penerapan-ds.streamlit.app/)

Langkah menjalankan di lokal:
```
streamlit run app.py
```

File penting:

1. `app.py`: untuk input prediksi.
2. `best_model_randomforest.pkl`: Model machine learning terlatih.
3. `scaler.pkl`: Skaler fitur untuk preprocessing data.
4. `feature_columns.pkl`: Urutan fitur untuk input model.

## Conclusion
Model machine learning yang dibangun dengan algoritma RandomForest berhasil mengidentifikasi mahasiswa yang berpotensi mengalami dropout dengan akurasi dan interpretabilitas yang baik. Dashboard bisnis juga memberikan wawasan yang sangat berguna untuk pengambilan keputusan berbasis data.

## Rekomendasi Action Items
Berdasarkan data dan temuan dari dashboard Jaya Jaya Institut Student Dropout Monitoring, berikut adalah beberapa langkah strategis yang direkomendasikan untuk menurunkan angka dropout dan meningkatkan retensi mahasiswa:

1. Perkuat Program Beasiswa dan Bantuan Finansial
   - Tingkatkan jumlah dan cakupan beasiswa untuk mahasiswa dari keluarga kurang mampu.
   - Prioritaskan mahasiswa dengan risiko tinggi dropout berdasarkan data historis, terutama yang tidak menerima beasiswa dan berasal dari keluarga dengan orang tua tidak bekerja.

2. Intervensi Akademik Dini
   - Lakukan pemantauan ketat terhadap performa akademik di semester 1 dan 2.
   - Mahasiswa dengan nilai masuk rendah dan rata-rata nilai semester rendah perlu segera mendapat bimbingan belajar, mentoring, atau program remedial.

3. Penilaian dan Penyaringan Lebih Ketat di Tahap Penerimaan
   - Evaluasi kembali standar nilai masuk dan kualifikasi sebelumnya, karena korelasinya cukup kuat dengan status kelulusan.
   - Gunakan sistem skor risiko dropout pada saat seleksi untuk mengantisipasi potensi masalah.

4. Keterlibatan Orang Tua dan Latar Belakang Sosial
   - Libatkan orang tua dalam proses edukasi sejak awal, terutama pada mahasiswa dengan latar belakang keluarga yang kurang stabil secara ekonomi.
   - Sediakan konseling sosial dan psikologis bagi mahasiswa yang menunjukkan tanda-tanda tekanan sosial.

5. Optimalisasi Pembayaran Biaya Kuliah
   - Buat sistem pembayaran cicilan yang fleksibel dan transparan untuk membantu mahasiswa dalam hal finansial.
   - Sediakan dukungan keuangan darurat untuk mahasiswa yang mengalami krisis ekonomi mendadak.

6. Peningkatan Engagement dan Monitoring Mahasiswa Aktif
   - Gunakan sistem pelaporan mingguan atau bulanan berbasis platform digital untuk memantau keterlibatan akademik dan sosial mahasiswa aktif.
   - Implementasikan early warning system berbasis data dari dashboard ini untuk mengidentifikasi dan mengintervensi mahasiswa berisiko sebelum terlambat.
