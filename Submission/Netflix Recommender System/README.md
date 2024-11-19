# Laporan Proyek Machine Learning - Shendi Teuku Maulana Efendi

## Project Overview
Proyek ini bertujuan untuk mengembangkan sistem rekomendasi film untuk Netflix, salah satu platform streaming terbesar di dunia yang memiliki jutaan pengguna aktif setiap hari. Dalam rangka meningkatkan pengalaman pengguna dan memperkuat keterlibatan mereka, penting untuk menyediakan rekomendasi yang dipersonalisasi—sebuah solusi yang membantu pengguna menemukan konten yang paling sesuai dengan preferensi pribadi mereka. Sebuah sistem rekomendasi yang efektif tidak hanya akan meningkatkan kepuasan pengguna, tetapi juga berkontribusi pada peningkatan waktu menonton dan retensi pengguna secara keseluruhan.

Dengan katalog film dan acara TV Netflix yang sangat luas, tantangan utama yang dihadapi adalah menciptakan sebuah sistem yang dapat memahami preferensi individu pengguna dan secara efisien menampilkan konten yang relevan. Dalam proyek ini, dua pendekatan utama digunakan untuk membangun sistem rekomendasi: `content-based filtering` dan `collaborative filtering`.

Sistem rekomendasi telah terbukti memainkan peran yang sangat penting dalam meningkatkan pengalaman pengguna serta mempertahankan tingkat keterlibatan yang tinggi. Menurut penelitian, lebih dari 80% konten yang ditonton di Netflix berasal dari rekomendasi algoritmik yang disarankan oleh sistem mereka. Hal ini menunjukkan seberapa efektif sistem rekomendasi dalam mempengaruhi pilihan konten pengguna. Untuk itu, proyek ini fokus pada penerapan kedua pendekatan tersebut—content-based filtering dan collaborative filtering—untuk menciptakan pengalaman penemuan konten yang lebih baik dan lebih relevan bagi setiap pengguna. 

Referensi: [Evaluating the use of a recommender system for selecting optimal messages for smoking cessation: patterns and effects of user-system engagement](https://link.springer.com/article/10.1186/s12889-021-11803-8)

## Business Understanding
Netflix menawarkan berbagai pilihan film dan acara TV yang sangat luas, namun hal ini juga bisa menjadi tantangan bagi penggunanya. Dengan begitu banyaknya konten yang tersedia, pengguna sering kali merasa kesulitan untuk menemukan film atau acara yang sesuai dengan selera mereka. Tanpa adanya sistem rekomendasi yang efektif, pengguna bisa merasa kewalahan atau kehilangan minat untuk terus mengeksplorasi konten di platform ini. Oleh karena itu, membangun sistem rekomendasi yang bisa memahami preferensi individu pengguna menjadi hal yang sangat penting dalam menjaga pengalaman pengguna tetap positif.

### Problem Statements
1. Dengan jutaan pilihan film dan acara TV di Netflix, pengguna sering kali kesulitan untuk menemukan konten yang sesuai dengan selera pribadi mereka.
2. Banyaknya pilihan yang tersedia sering menyebabkan pengguna merasa bingung atau lelah dalam memilih, yang berpotensi mengurangi keterlibatan mereka dengan platform.
3. Meskipun ada fitur pencarian di Netflix, metode pencarian yang ada belum tentu dapat menggambarkan selera dan preferensi individu dengan baik, sehingga pengguna mungkin tidak menemukan film yang mereka sukai dengan cepat.

### Goals
1. Memberikan rekomendasi film yang lebih sesuai dengan minat dan preferensi pengguna, sehingga meningkatkan pengalaman penemuan konten.
2. Dengan menyediakan rekomendasi yang lebih relevan, sistem ini akan mengurangi waktu yang dibutuhkan pengguna untuk mencari film atau acara yang mereka inginkan, sehingga meningkatkan kenyamanan pengguna.
3. Dengan menyajikan konten yang sesuai dengan preferensi pengguna, diharapkan pengguna akan lebih sering kembali ke platform dan melanjutkan menonton, yang berkontribusi pada peningkatan retensi pengguna.

### Solution Approachment
Untuk mengatasi tantangan dalam menemukan konten yang relevan di Netflix, proyek ini menggunakan dua pendekatan utama dalam membangun sistem rekomendasi: `Content-Based Filtering` dan `Collaborative Filtering`. Kedua metode ini dikembangkan secara terpisah, dengan fokus pada aspek yang berbeda dari preferensi pengguna dan karakteristik konten.

#### Solution Statements
1. Content-Based Filtering <br>
Pendekatan ini berfokus pada karakteristik konten itu sendiri, seperti genre, deskripsi, dan kata kunci terkait. Sistem ini menganalisis film atau acara yang sudah ditonton atau disukai oleh pengguna dan memberikan rekomendasi berdasarkan kesamaan konten.

  Feature Extraction:
   - Dalam pendekatan ini, atribut-atribut film seperti genre, deskripsi, dan judul digunakan untuk memahami konten setiap film.
   - Film-film yang memiliki kesamaan fitur dengan film yang sudah pernah berinteraksi dengan pengguna (misalnya, ditonton atau diberi rating tinggi) akan direkomendasikan. <br>
   
   Similarity Measurement:
   - Kemiripan antara film dihitung menggunakan teknik seperti cosine similarity atau pengukuran jarak lainnya, berdasarkan fitur-fitur yang telah diekstraksi dari setiap film. <br>
   
   Recommendation:
   - Sistem mengurutkan film berdasarkan skor kesamaan dan merekomendasikan film yang paling mirip dengan film yang sudah disukai atau ditonton oleh pengguna sebelumnya.
   - Pendekatan ini fokus pada karakteristik konten itu sendiri, seperti genre, deskripsi, dan kata kunci terkait. Sistem menganalisis film atau acara yang sudah pernah ditonton atau disukai oleh pengguna, kemudian memberikan rekomendasi berdasarkan kesamaan konten tersebut. <br> 
   
2. Collaborative Filtering <br>
Pendekatan ini berfokus pada interaksi antar pengguna dan item (film). Sistem ini memanfaatkan data interaksi pengguna, seperti rating atau preferensi yang telah diberikan kepada film, untuk memprediksi konten yang mungkin disukai pengguna lain dengan pola yang serupa.

  Model Deep Learning:
  - Sistem ini dibangun menggunakan model deep learning berbasis TensorFlow/Keras, yang memanfaatkan embedding layer untuk pengguna dan film. Embedding ini menangkap preferensi pengguna dan karakteristik film dalam bentuk vektor densitas. <br>
  
  Proses Training:
  - Selama proses pelatihan, model deep learning dilatih menggunakan data interaksi pengguna, seperti rating film atau preferensi lainnya, untuk memprediksi rating yang belum diberikan oleh pengguna pada film yang belum mereka tonton. Pelatihan ini bertujuan untuk meningkatkan akurasi dalam memprediksi film yang paling relevan bagi pengguna. <br>
   
  Model Optimization:
  - Menggunakan teknik optimisasi seperti Adam optimizer untuk memperbaiki akurasi prediksi melalui pelatihan model dengan data interaksi pengguna.

  Metrics:
  - RMSE (Root Mean Squared Error): Metrik ini digunakan untuk mengukur rata-rata kesalahan prediksi model dalam satuan yang sama dengan data aslinya. Semakin rendah nilai RMSE, semakin baik model dalam memprediksi rating yang sesuai.
  - MSE (Mean Squared Error): Metrik ini menghitung rata-rata kuadrat kesalahan prediksi antara nilai yang diprediksi dan nilai aktual. Seperti halnya RMSE, semakin kecil nilai MSE, semakin baik model dalam memberikan prediksi yang akurat.

## Data Understanding

Dataset yang digunakan dalam proyek ini berisi informasi tentang 8.807 film dan acara TV yang tersedia di platform Netflix. Dataset ini menyediakan atribut-atribut detail untuk setiap acara, termasuk metadata yang dapat dimanfaatkan untuk membangun sistem rekomendasi berbasis konten. 

### Sumber Datasets
Data ini dapat didownload dari [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows). Dataset ini terdiri dari 12 kolom, yang mencakup variabel numerik dan kategorikal. Beberapa nilai dalam dataset ini hilang, dan celah-celah tersebut akan ditangani selama fase praproses data.

### Features in the Dataset

| **Feature**     | **Type**           | **Description**                                                                                         | **Missing Values**                    |
|-----------------|--------------------|---------------------------------------------------------------------------------------------------------|---------------------------------------|
| **show_id**     | Object (string)    | A unique identifier for each movie or TV show in the dataset.                                             | None                                  |
| **type**        | Object (string)    | Indicates the type of content (e.g., "Movie" or "TV Show").                                              | None                                  |
| **title**       | Object (string)    | The title of the movie or TV show.                                                                       | None                                  |
| **director**    | Object (string)    | The director of the movie or TV show.                                                                   | Some missing entries                 |
| **cast**        | Object (string)    | The main actors or cast of the movie or TV show.                                                         | Some missing entries                 |
| **country**     | Object (string)    | The country where the movie or TV show was produced.                                                     | Some missing entries                 |
| **date_added**  | Object (string)    | The date the movie or TV show was added to Netflix.                                                      | Some missing entries                 |
| **release_year**| Integer (int64)    | The year the movie or TV show was released.                                                              | None                                  |
| **rating**      | Object (string)    | The rating of the movie or TV show (e.g., "PG", "TV-MA", etc.).                                          | Some missing entries                 |
| **duration**    | Object (string)    | The duration of the movie or TV show. For movies, it is the runtime in minutes, while for TV shows, it refers to the number of seasons. | Some missing entries                 |
| **listed_in**   | Object (string)    | The genres or categories the movie or TV show is listed under (e.g., "Action", "Drama", "Comedy", etc.). | None                                  |
| **description** | Object (string)    | A brief summary or description of the movie or TV show.                                                  | None                                  |

### Data Quality and Missing Values

Dataset ini mengandung beberapa nilai yang hilang pada kolom seperti `director`, `cast`, `country`, dan `date_added`. Nilai yang hilang ini akan ditangani dengan cara mengisi dengan nilai pengganti, menggunakan metode lain, atau menghapus baris/kolom yang memiliki data yang hilang secara berlebihan. Data akan diproses terlebih dahulu untuk memastikan kualitas dan konsistensi informasi sebelum membangun sistem rekomendasi.

| Column        | Missing Values | Percentage    |
|---------------|----------------|---------------|
| show_id       | 0              | 0.000000      |
| type          | 0              | 0.000000      |
| title         | 0              | 0.000000      |
| director      | 2634           | 29.908028     |
| cast          | 825            | 9.367549      |
| country       | 831            | 9.435676      |
| date_added    | 10             | 0.113546      |
| release_year  | 0              | 0.000000      |
| rating        | 4              | 0.045418      |
| duration      | 3              | 0.034064      |
| listed_in     | 0              | 0.000000      |
| description   | 0              | 0.000000      |

### Exploratory Data Analysis
1. Distribution of content ratings on Netflix
   ```python
   plt.figure(figsize=(10, 6))
   sns.countplot(x='rating', order = df['rating'].value_counts().index, data = df)
   plt.title('Distribution of content ratings on Netflix')
   plt.xlabel('Rating')
   plt.ylabel('Count')
   plt.xticks(rotation = 45)
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/4324c2ba-c5d6-41c2-b33b-72a4b56f96de" width="700" height="500"> <br>

2. Number of TV shows and movies added to Netflix changed over the years
   ```python
    df['year_added'] = df['date_added'].dt.year 
    plt.figure(figsize=(10, 6)) 
    sns.countplot(data=df, x='year_added', hue='type', order=sorted(df['year_added'].dropna().unique())) 
    plt.title('Number of TV Shows and Movies Added to Netflix Over the Years') 
    plt.xlabel('Year Added') 
    plt.ylabel('Count') 
    plt.xticks(rotation=45) 
    plt.show()
    ```
   <img src="https://github.com/user-attachments/assets/4b0d0ab4-6007-4f1a-b6de-ec604b1cf25a" width="700" height="500"> <br>

3. Top 10 countries producing Netflix content
   ```python
   top_countries = df['country'].value_counts().head(10) 
   plt.figure(figsize=(12, 8)) 
   sns.barplot(x=top_countries.values, y=top_countries.index) 
   plt.title('Top 10 Countries Producing Netflix Content') 
   plt.xlabel('Number of Titles') 
   plt.ylabel('Country') 
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/61321b6e-9904-4dcf-8e46-95c816c5c925" width="700" height="500"> <br>
   
4. Genres listed on Netflix
   ```python
   genres = df['listed_in'].str.split(', ', expand=True).stack().value_counts()
   plt.figure(figsize=(12, 8))
   sns.barplot(x=genres.values[:10], y=genres.index[:10])
   plt.title('Top 10 Genres on Netflix')
   plt.xlabel('Number of Titles')
   plt.ylabel('Genre')
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/8b397434-bc77-4b32-95e6-44efdf2296ec" width="700" height="500"> <br>

5. Duration of movies vary on Netflix
   ```python
   movies = df[df['type'] == 'Movie']
   movies['duration'] = pd.to_numeric(movies['duration'].str.replace(' min', ''), errors='coerce')
   plt.figure(figsize=(10, 6))
   sns.histplot(movies['duration'], bins=30, kde=True)
   plt.title('Distribution of Movie Durations on Netflix')
   plt.xlabel('Duration (minutes)')
   plt.ylabel('Frequency')
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/17054d56-c4fa-4552-b653-1386530f47e9" width="700" height="500"> <br>

   
6. Trends in content production by month and year
   ```python
   import pandas as pd
   plt.figure(figsize=(10, 6))
   sns.countplot(data=df, x='month_added', hue='year_added')
   plt.title('Trends in Content Production by Month and Year on Netflix')
   plt.xlabel('Month Added')
   plt.ylabel('Count')
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/8f454875-aea2-4ca6-87a2-7b308fc8e5da" width="700" height="500"> <br>
   
7. Most common release years for content on Netflix
   ```python
   plt.figure(figsize=(10, 6))
   sns.countplot(data=df, x='release_year', order=df['release_year'].value_counts().index[:10])
   plt.title('Most Common Release Years for Content on Netflix')
   plt.xlabel('Release Year')
   plt.ylabel('Count')
   plt.xticks(rotation=45)
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/3287f62b-08ca-42fa-b721-d43b040a1d14" width="700" height="500"> <br>

8. Distribution of content ratings vary by content type (TV Show vs. Movie)
   ```python
   plt.figure(figsize=(10, 6))
   sns.countplot(data=df, x='rating', hue='type', order=df['rating'].value_counts().index)
   plt.title('Distribution of Content Ratings by Content Type on Netflix')
   plt.xlabel('Rating')
   plt.ylabel('Count')
   plt.xticks(rotation=45)
   plt.show()
   ```
   <img src="https://github.com/user-attachments/assets/de6b3947-363a-4ef4-9d38-fa9279eaaa2b" width="700" height="500"> <br>

## Data Preparation
### Model Development Content Based Filtering
#### Check Missing Values
```python
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})
missing_data
```
#### Handling Missing Values
```python
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['release_year'] = df['release_year'].fillna(df['release_year'].mean())
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
df['listed_in'] = df['listed_in'].fillna(df['listed_in'].mode()[0])
df['date_added'] = df['date_added'].fillna('Unknown')
df['duration'] = df['duration'].fillna('Unknown')
```

#### After Handling Missing Values
```python
missing_values_after = df.isnull().sum()
missing_values_after
```
| Column        | Missing Values | Percentage |
|---------------|----------------|------------|
| show_id       | 0              | 0%         |
| type          | 0              | 0%         |
| title         | 0              | 0%         |
| director      | 0              | 0%         |
| cast          | 0              | 0%         |
| country       | 0              | 0%         |
| date_added    | 0              | 0%         |
| release_year  | 0              | 0%         |
| rating        | 0              | 0%         |
| duration      | 0              | 0%         |
| listed_in     | 0              | 0%         |
| description   | 0              | 0%         |

#### Feature Engineering
Setelah menangani missing values, kita akan mengubah kolom yang berisi teks (seperti `description`, `listed_in`, dll.) menjadi fitur numerik menggunakan TF-IDF.
```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df['content'] = df['cast'] + " " + df['director'] + " " + df['listed_in'] + " " + df['description']
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['content'])
print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")
```

Jika ingin melihat matriks secara keseluruhan dalam bentuk dense (penuh), gunakan todense. Ini akan mengonversi matriks sparse menjadi dense yang bisa dipahami dengan mudah
```python
tfidf_matrix.todense()
```

Membuat DataFrame dari matriks TF-IDF yang sudah diubah menjadi dense
pd.DataFrame(
    tfidf_matrix.todense(),  # Konversi matriks sparse menjadi dense
    columns=tfidf_vectorizer.get_feature_names_out(),  # Nama fitur yang dihasilkan oleh TfidfVectorizer
    index=df['title']  # Indeks berdasarkan judul film
)

## Modeling
Tahapan ini membahas mengenai model sisten rekomendasi yang Anda buat untuk menyelesaikan permasalahan. Sajikan top-N recommendation sebagai output.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menyajikan dua solusi rekomendasi dengan algoritma yang berbeda.
- Menjelaskan kelebihan dan kekurangan dari solusi/pendekatan yang dipilih.

## Evaluation
Pada bagian ini Anda perlu menyebutkan metrik evaluasi yang digunakan. Kemudian, jelaskan hasil proyek berdasarkan metrik evaluasi tersebut.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan formula metrik dan bagaimana metrik tersebut bekerja.

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
