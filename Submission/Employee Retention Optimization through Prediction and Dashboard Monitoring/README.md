# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju**

## **Business Understanding**
Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun perusahaan telah tumbuh menjadi besar, mereka menghadapi tantangan serius dalam mengelola karyawan, yang menyebabkan tingkat attrition (keluar karyawan) lebih dari 10%. Attrition yang tinggi dapat menyebabkan kerugian besar bagi perusahaan, mulai dari biaya rekrutmen dan pelatihan karyawan baru, menurunnya produktivitas, hingga hilangnya knowledge dan budaya organisasi. Oleh karena itu, diperlukan upaya proaktif untuk memahami faktor-faktor yang berkontribusi terhadap tingginya angka attrition.

### Permasalahan Bisnis
Departemen HR Jaya Jaya Maju menghadapi dua tantangan utama:
1. Mengidentifikasi faktor-faktor utama yang berpengaruh terhadap keputusan karyawan untuk meninggalkan perusahaan.
2. Memantau dan menganalisis faktor-faktor tersebut secara rutin melalui business dashboard yang informatif dan mudah dipahami.

### **Cakupan Proyek**
Pada proyek ini, dilakukan beberapa tahap utama, yaitu:
1. Business Understanding: Memahami permasalahan tingginya attrition rate yang dihadapi perusahaan.
2. Data Understanding & Preparation: Mengeksplorasi dataset karyawan, melakukan pembersihan data (handling missing values dan outlier), serta transformasi fitur.
3. Exploratory Data Analysis (EDA): Menganalisis pola, tren, dan faktor-faktor yang berkorelasi terhadap attrition.
4. Modeling: Membangun beberapa model prediksi (seperti Logistic Regression, Random Forest, XGBoost, dan Gradient Boosting) untuk memprediksi kemungkinan karyawan keluar.
5. Evaluation: Membandingkan model berdasarkan metrik akurasi dan memilih model terbaik.
6. Deployment Preparation: Menyimpan model terbaik dalam bentuk file .pkl untuk digunakan dalam dashboard Metabase.
7. Recommendation: Memberikan rekomendasi berbasis data untuk mengurangi tingkat attrition.

### **Persiapan Data**
#### 1. Sumber Dataset
Link dataset bisa diakses di dibawah ini: <br> <br>
[![GitHub - employee_data.csv](https://img.shields.io/badge/GitHub-Dataset-black?logo=github)](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv)

#### 2. Setup Environment
   
   - Buat dan Aktifkan Environment Conda
   ```
   conda create -n attrition-env python=3.9 -y
   conda activate attrition-env
   ```
   - Install Requirements
   ```
   pip install -r requirements.txt
   ```

   - Let's Run The Notebook!

#### 3. How Predict The Attrition With Modelling?

   - Run file
   ```
   python predict.py
   ```

#### 4. Cara Setup Metabase

   - Jalankan Metabase menggunakan Docker:
   ```
   docker run -d -p 3000:3000 --name metabase metabase/metabase
   ```
   
   - Akses Metabase di browser:
   ```
   http://localhost:3000
   ```

   - Login Metabase
   ```
   Email: root@mail.com
   Password: root123
   ```

   - Connect Metabase ke Supabase
   Masukkan URL Database
   ```
   postgresql://postgres.bvnuasnbwmaxzgboenvl:[YOURPASSWORDDB]@URLTransactionPooler
   ```

   - Upload Data ke Supabase
   Gunakan kode berikut untuk mengupload data ke Supabase:
   ```python
   from sqlalchemy import create_engine
   # URL Database Supabase
   URL = "postgresql://postgres.bvnuasnbwmaxzgboenvl:[YOURPASSWORDDB]@URLTransactionPooler"

   # Create Engine
   engine = create_engine(URL)

   # Upload DataFrame ke Supabase (jangan lupa ubah 'df' sesuai nama DataFrame kamu)
   df.to_sql('employee_data_supabase', engine, index=False, if_exists='replace')
  ```


## Business Dashboard
### Tujuan Dashboard:
- Memberikan visualisasi menyeluruh terkait attrition rate di perusahaan.
- Menunjukkan faktor-faktor penting seperti departemen, usia, penghasilan, lama bekerja, dan tingkat kepuasan kerja yang berhubungan dengan attrition.
- Menyediakan insight untuk pengambilan keputusan strategis oleh manajer HR.

### Visualize Dashboard:

![Screenshot (367)](https://github.com/user-attachments/assets/e7f7789a-e224-4810-a9a4-2dd4a388a62b)
![Screenshot (368)](https://github.com/user-attachments/assets/1d56bbf5-5716-4721-aa85-41d063ccd9ee)

## **Conclusion**
Proyek ini berhasil melakukan analisis menyeluruh terhadap faktor-faktor penyebab tingginya attrition rate di perusahaan Jaya Jaya Maju. Melalui proses EDA dan modeling, ditemukan bahwa faktor usia, loyalitas terhadap manajer, pengalaman kerja, serta kesejahteraan finansial sangat mempengaruhi keputusan karyawan untuk bertahan atau keluar.
Dengan membangun model prediksi dan business dashboard, departemen HR kini dapat memonitor faktor-faktor kritis secara real-time dan melakukan tindakan pencegahan berbasis data.

### Recommendation Actions
Berdasarkan hasil analisis dan modeling, berikut beberapa rekomendasi aksi untuk HR Department Jaya Jaya Maju:
1. Meningkatkan Program Training: Karyawan dengan rata-rata training lebih rendah per tahun cenderung lebih mudah keluar. Perlu ditingkatkan akses dan kualitas pelatihan.
2. Mendukung Loyalitas Terhadap Manager: Faktor Loyalty to Manager dan Stability in Role berhubungan dengan bertahannya karyawan. Disarankan adanya program engagement antara atasan dan bawahan.
3. Perhatikan Kebijakan Work-Life Balance: Karyawan yang tinggal jauh dari kantor (Distance From Home) memiliki kecenderungan lebih tinggi untuk keluar. Dapat dipertimbangkan kebijakan fleksibilitas kerja.
4. Mengidentifikasi dan Memberdayakan Karyawan Muda: Usia (Age) dan pengalaman kerja total (Total Working Years) berhubungan negatif terhadap attrition. Fokus pada retensi karyawan muda dan yang baru bergabung.
5. Evaluasi Kesejahteraan Finansial: Faktor Monthly Income dan Stock Option Level signifikan. Perlu ada evaluasi benefit kompensasi agar lebih kompetitif.
