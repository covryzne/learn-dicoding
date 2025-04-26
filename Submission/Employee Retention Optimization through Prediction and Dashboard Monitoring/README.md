# 🎯 **Business Understanding**

## Latar Belakang
Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun perusahaan telah tumbuh menjadi besar, mereka menghadapi tantangan serius dalam mengelola karyawan, yang menyebabkan tingkat attrition (keluar karyawan) lebih dari 10%. Attrition yang tinggi dapat menyebabkan kerugian besar bagi perusahaan, mulai dari biaya rekrutmen dan pelatihan karyawan baru, menurunnya produktivitas, hingga hilangnya knowledge dan budaya organisasi. Oleh karena itu, diperlukan upaya proaktif untuk memahami faktor-faktor yang berkontribusi terhadap tingginya angka attrition.

## Permasalahan Bisnis
Departemen HR Jaya Jaya Maju menghadapi dua tantangan utama:
1. Mengidentifikasi faktor-faktor utama yang berpengaruh terhadap keputusan karyawan untuk meninggalkan perusahaan.
2. Memantau dan menganalisis faktor-faktor tersebut secara rutin melalui business dashboard yang informatif dan mudah dipahami.

## Tujuan Proyek
1. Menganalisis data karyawan untuk menemukan pola dan faktor utama yang memengaruhi attrition rate.
2. Mengembangkan model prediksi untuk mengklasifikasikan risiko seorang karyawan untuk keluar dari perusahaan.
3. Membangun business dashboard interaktif menggunakan Metabase untuk membantu manajer HR dalam monitoring dan pengambilan keputusan berbasis data.

## Manfaat
1. Memberikan insight kepada manajemen HR tentang area yang perlu diperbaiki untuk meningkatkan retensi karyawan.
2. Mengoptimalkan strategi retensi dengan mengidentifikasi karyawan yang berisiko tinggi untuk keluar.
3. Meningkatkan efisiensi dan efektivitas dalam pengelolaan sumber daya manusia.

# 📌 **Cakupan Proyek**
Pada proyek ini, dilakukan beberapa tahap utama, yaitu:
1. Business Understanding: Memahami permasalahan tingginya attrition rate yang dihadapi perusahaan.
2. Data Understanding & Preparation: Mengeksplorasi dataset karyawan, melakukan pembersihan data (handling missing values dan outlier), serta transformasi fitur.
3. Exploratory Data Analysis (EDA): Menganalisis pola, tren, dan faktor-faktor yang berkorelasi terhadap attrition.
4. Modeling: Membangun beberapa model prediksi (seperti Logistic Regression, Random Forest, XGBoost, dan Gradient Boosting) untuk memprediksi kemungkinan karyawan keluar.
5. Evaluation: Membandingkan model berdasarkan metrik akurasi dan memilih model terbaik.
6. Deployment Preparation: Menyimpan model terbaik dalam bentuk file .pkl untuk digunakan dalam dashboard Metabase.
7. Recommendation: Memberikan rekomendasi berbasis data untuk mengurangi tingkat attrition.

# 📊 **Recommendation Actions**
Berdasarkan hasil analisis dan modeling, berikut beberapa rekomendasi aksi untuk HR Department Jaya Jaya Maju:
1. Meningkatkan Program Training: Karyawan dengan rata-rata training lebih rendah per tahun cenderung lebih mudah keluar. Perlu ditingkatkan akses dan kualitas pelatihan.
2. Mendukung Loyalitas Terhadap Manager: Faktor Loyalty to Manager dan Stability in Role berhubungan dengan bertahannya karyawan. Disarankan adanya program engagement antara atasan dan bawahan.
3. Perhatikan Kebijakan Work-Life Balance: Karyawan yang tinggal jauh dari kantor (Distance From Home) memiliki kecenderungan lebih tinggi untuk keluar. Dapat dipertimbangkan kebijakan fleksibilitas kerja.
4. Mengidentifikasi dan Memberdayakan Karyawan Muda: Usia (Age) dan pengalaman kerja total (Total Working Years) berhubungan negatif terhadap attrition. Fokus pada retensi karyawan muda dan yang baru bergabung.
5. Evaluasi Kesejahteraan Finansial: Faktor Monthly Income dan Stock Option Level signifikan. Perlu ada evaluasi benefit kompensasi agar lebih kompetitif.

# 📋 **Conclusion**
Proyek ini berhasil melakukan analisis menyeluruh terhadap faktor-faktor penyebab tingginya attrition rate di perusahaan Jaya Jaya Maju. Melalui proses EDA dan modeling, ditemukan bahwa faktor usia, loyalitas terhadap manajer, pengalaman kerja, serta kesejahteraan finansial sangat mempengaruhi keputusan karyawan untuk bertahan atau keluar.
Dengan membangun model prediksi dan business dashboard, departemen HR kini dapat memonitor faktor-faktor kritis secara real-time dan melakukan tindakan pencegahan berbasis data.

Outcome dari proyek ini:
1. Model prediksi attrition berbasis Gradient Boosting dengan akurasi terbaik.
2. Dataset terstruktur dan siap digunakan untuk visualisasi dashboard.
3. Rekomendasi actionable untuk meningkatkan retensi karyawan.

# **How to Run The Notebook?**
Ikuti langkah-langkah berikut untuk menjalankan proyek ini:

1. Buat dan Aktifkan Environment Conda
   ```
   conda create -n attrition-env python=3.9 -y
   conda activate attrition-env
   ```
2. Install Requirements
   ```
   pip install -r requirements.txt
   ```

3. Let's Run The Notebook!

# **How Predict The Attrition With Modelling?**

1. Run file
   ```
   python predict.py
   ```
   
2. Input Data <br><br>
   Di dalam `predict.py`, sudah disiapkan contoh data input baru berbentuk dictionary. Anda dapat mengganti nilai-nilai tersebut sesuai dengan profil karyawan yang ingin diprediksi.

3. Catatan <br><br>
   Model yang digunakan adalah Gradient Boosting Classifier, model dengan performa terbaik berdasarkan akurasi evaluasi.

# 📊 **Business Dashboard with Metabase and Supabase**

## Tujuan Dashboard
Dashboard ini dibuat untuk membantu departemen HR Jaya Jaya Maju dalam:
1. Memahami faktor-faktor yang berpengaruh terhadap attrition rate.
2. Memantau secara real-time berbagai indikator penting terkait karyawan.

## Tools yang Digunakan
1. Metabase -> Untuk visualisasi dan pembuatan business dashboard.
2. Supabase -> Untuk menyimpan dan mengelola data karyawan secara cloud (menggunakan database PostgreSQL Supabase).

## Cara Setup Metabase
1. Jalankan Metabase menggunakan Docker:
   ```
   docker run -d -p 3000:3000 --name metabase metabase/metabase
   ```
   
2. Akses Metabase di browser:
   ```
   http://localhost:3000
   ```

3. Login Metabase
   ```
   Email: root@mail.com
   Password: root123
   ```

4. Connect Metabase ke Supabase
   Masukkan URL Database
   ```
   postgresql://postgres.bvnuasnbwmaxzgboenvl:[YOURPASSWORDDB]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres
   ```

5. Upload Data ke Supabase
   Gunakan kode berikut untuk mengupload data ke Supabase:
   ```python
   from sqlalchemy import create_engine
   # URL Database Supabase
   URL = "postgresql://postgres.bvnuasnbwmaxzgboenvl:[YOURPASSWORDDB]@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

   # Create Engine
   engine = create_engine(URL)

   # Upload DataFrame ke Supabase (jangan lupa ubah 'df' sesuai nama DataFrame kamu)
   df.to_sql('employee_data_supabase', engine, index=False, if_exists='replace')
  ```
