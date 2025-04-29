# **Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju**

## **Business Understanding**

Jaya Jaya Maju merupakan perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Meskipun perusahaan telah tumbuh menjadi besar, mereka menghadapi tantangan serius dalam mengelola karyawan, yang menyebabkan tingkat attrition (keluar karyawan) lebih dari 10%. Attrition yang tinggi dapat menyebabkan kerugian besar bagi perusahaan, mulai dari biaya rekrutmen dan pelatihan karyawan baru, menurunnya produktivitas, hingga hilangnya knowledge dan budaya organisasi. Oleh karena itu, diperlukan upaya proaktif untuk memahami faktor-faktor yang berkontribusi terhadap tingginya angka attrition.

### Permasalahan Bisnis

Perusahaan Jaya Jaya Maju mengalami tingkat employee attrition yang cukup tinggi dalam beberapa tahun terakhir. Tingginya tingkat keluar-masuk karyawan memberikan dampak signifikan terhadap produktivitas tim, peningkatan biaya rekrutmen dan pelatihan, serta menurunnya stabilitas organisasi.

Departemen HR mengalami kesulitan dalam mengidentifikasi secara akurat faktor-faktor utama yang menyebabkan karyawan meninggalkan perusahaan. Selain itu, belum adanya sistem pemantauan berbasis data yang dapat membantu mengawasi tren dan pola attrition secara rutin membuat pengambilan keputusan.

Jika kondisi ini terus berlanjut tanpa intervensi yang tepat, maka perusahaan berisiko kehilangan talenta-talenta terbaik, mengalami penurunan performa operasional, dan menghadapi biaya operasional yang membengkak akibat proses rekrutmen dan pelatihan yang berulang. Oleh karena itu, diperlukan pendekatan berbasis data untuk menganalisis dan memitigasi risiko attrition secara lebih efektif.

### **Cakupan Proyek**

Pada proyek ini, dilakukan beberapa tahap utama, yaitu:

1. Business Understanding <br>
   Mengidentifikasi dan memahami konteks permasalahan attrition yang berdampak pada performa organisasi.

2. Data Understanding & Preparation <br>
   Melakukan eksplorasi dataset karyawan, menangani missing values, outlier, serta melakukan transformasi fitur yang diperlukan untuk analisis lanjutan.

3. Exploratory Data Analysis (EDA) <br>
   Menganalisis pola dan tren attrition berdasarkan variabel-variabel seperti usia, pendapatan, durasi kerja, dan lainnya untuk menemukan insight awal.

4. Modeling <br>
   Membangun beberapa model prediksi attrition, seperti Logistic Regression, Random Forest, XGBoost, dan Gradient Boosting, serta membandingkan performanya menggunakan metrik seperti akurasi, F1-score, dan AUC.

5. Evaluation <br>
   Menentukan model terbaik berdasarkan evaluasi metrik serta menginterpretasikan fitur-fitur penting yang memengaruhi prediksi.

6. Script Prediction & Deployment Preparation <br>
   Menyusun script Python untuk melakukan prediksi secara otomatis dan menyimpan model terbaik dalam bentuk file .pkl agar dapat digunakan dalam sistem.

7. Dashboard Development <br>
   Mengembangkan dashboard interaktif menggunakan Looker Studio untuk memvisualisasikan insight dan metrik utama secara real-time.

8. Recommendation <br>
   Memberikan rekomendasi strategis berbasis data kepada tim HR untuk meningkatkan retensi karyawan dan mengurangi tingkat attrition.

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

## Business Dashboard

### Tujuan Dashboard:

- Memberikan visualisasi menyeluruh terkait attrition rate di perusahaan.
- Menunjukkan faktor-faktor penting seperti departemen, usia, penghasilan, lama bekerja, dan tingkat kepuasan kerja yang berhubungan dengan attrition.
- Menyediakan insight untuk pengambilan keputusan strategis oleh manajer HR.

### Visualize Dashboard:

Dashboard bisa diakses pada link dibawah: <br><br>
[![Built with Looker Studio](https://img.shields.io/badge/Built%20with-Looker%20Studio-4285F4?style=for-the-badge&logo=googleanalytics&logoColor=white)](https://lookerstudio.google.com/reporting/ddad8308-d445-4228-9208-ce9471113627)

![Screenshot (367)](https://github.com/user-attachments/assets/e7f7789a-e224-4810-a9a4-2dd4a388a62b)
![Screenshot (368)](https://github.com/user-attachments/assets/1d56bbf5-5716-4721-aa85-41d063ccd9ee)

## Conclusion

Proyek ini berhasil melakukan analisis menyeluruh terhadap faktor-faktor penyebab tingginya attrition rate di perusahaan Jaya Jaya Maju. Melalui proses EDA dan modeling, ditemukan bahwa faktor usia, loyalitas terhadap manajer, pengalaman kerja, serta kesejahteraan finansial sangat mempengaruhi keputusan karyawan untuk bertahan atau keluar.
Dengan membangun model prediksi dan business dashboard, departemen HR kini dapat memonitor faktor-faktor kritis secara real-time dan melakukan tindakan pencegahan berbasis data.

### Recommendation Actions

Berdasarkan hasil analisis dan modeling, berikut beberapa rekomendasi aksi untuk HR Department Jaya Jaya Maju:

1. Meningkatkan Program Training: Karyawan dengan rata-rata training lebih rendah per tahun cenderung lebih mudah keluar. Perlu ditingkatkan akses dan kualitas pelatihan.
2. Mendukung Loyalitas Terhadap Manager: Faktor Loyalty to Manager dan Stability in Role berhubungan dengan bertahannya karyawan. Disarankan adanya program engagement antara atasan dan bawahan.
3. Perhatikan Kebijakan Work-Life Balance: Karyawan yang tinggal jauh dari kantor (Distance From Home) memiliki kecenderungan lebih tinggi untuk keluar. Dapat dipertimbangkan kebijakan fleksibilitas kerja.
4. Mengidentifikasi dan Memberdayakan Karyawan Muda: Usia (Age) dan pengalaman kerja total (Total Working Years) berhubungan negatif terhadap attrition. Fokus pada retensi karyawan muda dan yang baru bergabung.
5. Evaluasi Kesejahteraan Finansial: Faktor Monthly Income dan Stock Option Level signifikan. Perlu ada evaluasi benefit kompensasi agar lebih kompetitif.
