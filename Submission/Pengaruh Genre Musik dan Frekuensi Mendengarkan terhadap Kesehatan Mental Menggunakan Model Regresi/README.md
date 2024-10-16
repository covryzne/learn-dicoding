# Laporan Proyek Machine Learning - Shendi Teuku Maulana Efendi

## Domain Proyek
> **Domain proyek yang dipilih dalam proyek machine learning ini adalah mengenai kesehatan dengan judul proyek "Pengaruh Genre Musik dan Frekuensi Mendengarkan terhadap Kesehatan Mental Menggunakan Model Regresi"**.

### Latar Belakang
Kesehatan mental telah menjadi isu global yang semakin mendapat perhatian, terutama di tengah kondisi dunia yang penuh dengan tekanan dan kecemasan akibat berbagai faktor, termasuk pandemik, ketidakpastian ekonomi, dan perubahan sosial. Menurut Organisasi Kesehatan Dunia (WHO), kesehatan mental yang baik sangat penting untuk kesejahteraan individu dan berpengaruh terhadap produktivitas, hubungan sosial, serta kualitas hidup secara keseluruhan.

Musik dikenal sebagai salah satu terapi non-medis yang dapat membantu mengurangi stres dan meningkatkan suasana hati. Banyak penelitian menunjukkan bahwa genre musik dan frekuensi mendengarkan musik dapat memengaruhi kondisi mental seseorang. Misalnya, mendengarkan musik yang ceria dapat meningkatkan suasana hati dan mengurangi perasaan cemas, sedangkan musik yang lebih sedih bisa memperdalam perasaan melankolis bagi sebagian orang.

Beberapa penelitian juga menunjukkan hubungan antara jenis musik yang didengarkan dan kondisi kesehatan mental seperti kecemasan, depresi, dan insomnia. Musik dengan tempo cepat, seperti pop atau EDM, sering kali dikaitkan dengan peningkatan energi dan mood yang lebih baik, sementara genre yang lebih lambat, seperti klasik atau jazz, dapat digunakan untuk relaksasi dan pengurangan stres.

Penelitian ini bertujuan untuk menjelaskan hubungan antara genre musik yang sering didengarkan dan kondisi kesehatan mental individu, seperti kecemasan dan depresi, dengan menggunakan pendekatan model regresi. Dengan pemahaman yang lebih baik tentang bagaimana musik mempengaruhi kesehatan mental, diharapkan dapat dihasilkan rekomendasi untuk penggunaan musik sebagai salah satu cara untuk meningkatkan kesejahteraan mental.

## Business Understanding

Pada bagian ini, kamu perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Pernyataan Masalah 1
- Pernyataan Masalah 2
- Pernyataan Masalah n

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Jawaban pernyataan masalah 1
- Jawaban pernyataan masalah 2
- Jawaban pernyataan masalah n

Semua poin di atas harus diuraikan dengan jelas. Anda bebas menuliskan berapa pernyataan masalah dan juga goals yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Mengajukan 2 atau lebih solution statement. Misalnya, menggunakan dua atau lebih algoritma untuk mencapai solusi yang diinginkan atau melakukan improvement pada baseline model dengan hyperparameter tuning.
    - Solusi yang diberikan harus dapat terukur dengan metrik evaluasi.

## Data Understanding
Paragraf awal bagian ini menjelaskan informasi mengenai data yang Anda gunakan dalam proyek. Sertakan juga sumber atau tautan untuk mengunduh dataset. Contoh: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Restaurant+%26+consumer+data).

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Restaurant UCI dataset adalah sebagai berikut:
- accepts : merupakan jenis pembayaran yang diterima pada restoran tertentu.
- cuisine : merupakan jenis masakan yang disajikan pada restoran.
- dst

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

## Modeling
Tahapan ini membahas mengenai model machine learning yang digunakan untuk menyelesaikan permasalahan. Anda perlu menjelaskan tahapan dan parameter yang digunakan pada proses pemodelan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan kelebihan dan kekurangan dari setiap algoritma yang digunakan.
- Jika menggunakan satu algoritma pada solution statement, lakukan proses improvement terhadap model dengan hyperparameter tuning. **Jelaskan proses improvement yang dilakukan**.
- Jika menggunakan dua atau lebih algoritma pada solution statement, maka pilih model terbaik sebagai solusi. **Jelaskan mengapa memilih model tersebut sebagai model terbaik**.

## Evaluation
Pada bagian ini anda perlu menyebutkan metrik evaluasi yang digunakan. Lalu anda perlu menjelaskan hasil proyek berdasarkan metrik evaluasi yang digunakan.

Sebagai contoh, Anda memiih kasus klasifikasi dan menggunakan metrik **akurasi, precision, recall, dan F1 score**. Jelaskan mengenai beberapa hal berikut:
- Penjelasan mengenai metrik yang digunakan
- Menjelaskan hasil proyek berdasarkan metrik evaluasi

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

## Referensi
1. World Health Organization (WHO). (2021). Mental health: strengthening our response. [Link](https://www.who.int/news-room/fact-sheets/detail/mental-health-strengthening-our-response)
2. Garrido, S., & Schubert, E. (2011). The Impact of Music on the Mind: A Review of Research. International Journal of Psychology and Behavioral Sciences, 1(1), 1-10. [Link](https://www.researchgate.net/publication/259730931_Individual_Differences_in_the_Enjoyment_of_Negative_Emotion_in_Music_A_Literature_Review_and_Experiment)
3. Thoma, M. V., La Marca, R., Brönnimann, S., Finkel, L., & Nater, U. M. (2013). The effect of stress and music on health-related outcomes. Health Psychology Review, 7(3), 273-284. [Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3734071/)
4. Kuhlmann, A. M., & Scherer, K. R. (2017). The relationship between music preferences and emotional health. Psychology of Music, 45(5), 676-691. [Link](https://www.ijnrd.org/papers/IJNRD2405557.pdf)

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.

