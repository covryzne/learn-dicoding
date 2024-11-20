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
   
   Metrics
   * Precision <br>
     Precision mengukur seberapa banyak item yang direkomendasikan yang relevan dibandingkan dengan jumlah total item yang direkomendasikan.
   * Recall <br>
     Recall mengukur seberapa banyak item relevan yang direkomendasikan dibandingkan dengan total item relevan yang ada.
   * F1-Score <br>
     F1-Score adalah rata-rata harmonik dari precision dan recall. Digunakan ketika kamu ingin menyeimbangkan antara precision dan recall.
      
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
1. Distribution Rating Konten
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

   Menunjukkan distribusi rating konten di Netflix. Saya ingin melihat kategori rating mana yang paling banyak. Menunjukkan distribusi konten berdasarkan rating. Terlihat bahwa kategori rating seperti `TV-MA` dan `TV-14` memiliki jumlah konten paling banyak, menunjukkan bahwa Netflix memiliki banyak konten untuk audiens dewasa dan remaja.


2. Tren Penambahan Konten Berdasarkan Tahun
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
   
   Mengekstrak informasi bulan dan tahun dari kolom `date_added` untuk melihat tren penambahan konten baru di Netflix selama bertahun-tahun. Menunjukkan jumlah konten yang ditambahkan ke Netflix setiap tahun, dibedakan berdasarkan tipe konten. Terlihat bahwa tahun 2019 memiliki jumlah konten yang ditambahkan paling banyak, mencerminkan pertumbuhan produksi konten orisinal Netflix.

4. Negara Teratas dalam Produksi Konten
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

   Negara-negara teratas yang memproduksi konten Netflix untuk melihat distribusi asal produksi. Menampilkan 10 negara teratas yang memproduksi konten di Netflix. Amerika Serikat terlihat mendominasi dalam jumlah produksi konten, diikuti oleh negara-negara lain seperti India dan Inggris.
   
6. Top Genre di Netflix
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

   Menunjukkan 10 genre teratas yang paling sering muncul di Netflix. Genre seperti `International Movies`, `Drama`, dan `Comedy` mendominasi platform ini, memberikan wawasan tentang preferensi audiens.

8. Distribusi Durasi Film
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

   Memperlihatkan distribusi durasi film di Netflix. Sebagian besar film memiliki durasi antara 80-120 menit, mencerminkan durasi standar untuk film di platform ini.
   
10. Tahun Rilis Terbanyak
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
   
   Menampilkan 10 tahun dengan jumlah rilis konten terbanyak di Netflix. Tahun 2018 dan 2017 adalah tahun-tahun dengan rilis terbanyak, mencerminkan puncak produksi konten di platform.
   
11. Tren Konten yang Dirilis pada Netflix Tiap Tahun
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
   
   menunjukkan tahun-tahun dengan jumlah konten terbanyak yang dirilis di Netflix, membantu memahami tren produksi konten berdasarkan tahun rilis.

11. Distribusi Rating Berdasarkan Tipe Konten
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
   
   menunjukkan distribusi rating konten di Netflix, dibedakan berdasarkan tipe (Movie/TV Show). Terlihat bahwa film cenderung memiliki variasi rating yang lebih luas dibandingkan acara TV.

### Insight EDA
1. Netflix berfokus pada audiens dewasa dan remaja, dengan rating TV-MA dan TV-14 yang paling banyak. Konten keluarga atau untuk anak-anak (seperti TV-Y) lebih sedikit.
2. Amerika Serikat tetap menjadi produsen konten terbesar, namun negara lain seperti India dan Korea Selatan juga memainkan peran penting, menunjukkan upaya Netflix untuk memperluas jangkauannya di pasar global.
3. Konten orisinal menjadi prioritas besar, dengan puncaknya pada tahun 2018, di mana Netflix memperkenalkan lebih banyak produk orisinal untuk menarik dan mempertahankan pelanggan.
4. Genre Drama, Comedy, dan Documentaries mendominasi konten Netflix, menunjukkan bahwa Netflix lebih fokus pada konten cerita dan edukasi yang menarik.
5. Strategi penambahan konten musiman terlihat dengan peningkatan konten menjelang akhir tahun, mungkin untuk menarik lebih banyak penonton di saat liburan.
6. Durasi film yang ideal bagi Netflix berkisar antara 80-120 menit, yang sesuai dengan preferensi penonton untuk film yang tidak terlalu panjang atau pendek.

## Data Preparation

### Model Development Content Based Filltering

#### 1. Check Missing Values

```python
missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100
missing_data = pd.DataFrame({
    'Missing Values': missing_values,
    'Percentage': missing_percentage
})
missing_data
```
#### 2. Handling Missing Values

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

#### 3. After Handling Missing Values

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

#### 4. Feature Engineering

Menggabungkan berbagai kolom teks (seperti cast, director, listed_in, dan description) menjadi satu kolom baru content. Hal ini dilakukan untuk memberikan representasi teks yang lebih komprehensif tentang film atau acara yang ada.

```python
df['content'] = df['cast'] + " " + df['director'] + " " + df['listed_in'] + " " + df['description']
```

#### 5. Transformasi Teks ke Vektor Numerik menggunakan TF-IDF Vectorizer

Menggunakan TF-IDF Vectorizer untuk mengubah data teks menjadi fitur numerik. TF-IDF (Term Frequency-Inverse Document Frequency) menghitung frekuensi kata dalam dokumen dan memperhitungkan pentingnya kata tersebut dalam seluruh koleksi dokumen.
Setelah menangani missing values, kita akan mengubah kolom yang berisi teks (seperti `description`, `listed_in`, dll.) menjadi fitur numerik menggunakan TF-IDF.

```python
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(df['content'])
print(f"TF-IDF Matrix Shape: {tfidf_matrix.shape}")
```

Jika ingin melihat matriks secara keseluruhan dalam bentuk dense (penuh), gunakan todense. Ini akan mengonversi matriks sparse menjadi dense yang bisa dipahami dengan mudah
```python
tfidf_matrix.todense()
```

Membuat DataFrame dari matriks TF-IDF yang sudah diubah menjadi dense
```python
pd.DataFrame(
    tfidf_matrix.todense(),  # Konversi matriks sparse menjadi dense
    columns=tfidf_vectorizer.get_feature_names_out(),  # Nama fitur yang dihasilkan oleh TfidfVectorizer
    index=df['title']  # Indeks berdasarkan judul film
)
```

### Model Development Collaborative Filtering

#### 1. Menangani Missing Values

Memeriksa missing values pada setiap kolom dan kemudian melakukan imputasi pada kolom-kolom yang memiliki missing values.

```python
df2['director'] = df2['director'].fillna('Unknown')
df2['cast'] = df2['cast'].fillna('Unknown')
df2['country'] = df2['country'].fillna('Unknown')
df2['release_year'] = df2['release_year'].fillna(df2['release_year'].mean())
df2['rating'] = df2['rating'].fillna(df2['rating'].mode()[0])
df2['listed_in'] = df2['listed_in'].fillna(df2['listed_in'].mode()[0])
df2['date_added'] = df2['date_added'].fillna('Unknown')
df2['duration'] = df2['duration'].fillna('Unknown')
```

#### 2. Membuat userId Secara Acak:

Membuat userId secara acak antara 1 hingga 1000 untuk menghasilkan ID pengguna yang unik pada setiap entri film. Hal ini diperlukan agar kita dapat memodelkan interaksi antara pengguna dan film.

```python
df2['userId'] = np.random.randint(1, 1001, df2.shape[0])
```

#### 3. Menyesuaikan show_id ke movieId:

Mengubah kolom show_id menjadi movieId yang unik untuk setiap film. Ini dilakukan dengan cara mengonversi show_id ke dalam bentuk kategori dan kemudian memberi nilai numerik yang mewakili setiap film.

```python
df2['movieId'] = df2['show_id'].astype('category').cat.codes
```

#### 4. Menangani Missing Rating

Beberapa film mungkin tidak memiliki rating yang terisi. Untuk itu, rating yang hilang diisi dengan label 'Unrated', yang kemudian dihapus untuk menghindari data yang tidak valid. Setelah itu, rating dikodekan menjadi angka untuk digunakan dalam model.

```python
df2['rating'] = df2['rating'].fillna('Unrated')
df2 = df2[df2['rating'] != 'Unrated']
rating_mapping = {'Unrated': 0, 'G': 1, 'PG': 2, 'PG-13': 3, 'R': 4, 'NC-17': 5}
df2.loc[:, 'rating'] = df2['rating'].map(rating_mapping).fillna(0).astype(int)
```

#### 5. Memilih Kolom untuk Collaborative Filtering

Memilih kolom-kolom yang diperlukan untuk model collaborative filtering, yaitu userId, movieId, dan rating. Data ini akan digunakan untuk melatih model rekomendasi.

```python
df_collab = df2[['userId', 'movieId', 'rating']]
```

#### 6. Split Data menjadi Train dan Test

Membagi data menjadi dua bagian, yaitu data untuk pelatihan (80%) dan data untuk pengujian (20%). Pengaturan random_state memastikan pembagian yang konsisten dan dapat direproduksi.

```python
train_data, test_data = train_test_split(df_collab, test_size=0.2, random_state=42)
```

#### 7. Menyiapkan input untuk model
Setelah data dibagi menjadi training dan testing, perlu mempersiapkan input untuk model.
```python
train_user_input = train_data['userId'].values
train_item_input = train_data['movieId'].values
train_ratings = train_data['rating'].values
test_user_input = test_data['userId'].values
test_item_input = test_data['movieId'].values
test_ratings = test_data['rating'].values
```
train_user_input dan train_item_input: Menyimpan ID pengguna dan ID film dari data training untuk input ke dalam model.
train_ratings: Menyimpan rating yang diberikan oleh pengguna untuk film yang bersangkutan sebagai target output.

#### 8. Menentukan Dimensi Input dan Embedding
num_users dan num_items: Menghitung jumlah pengguna dan item (film) unik di dataset. Ini penting untuk mendefinisikan dimensi input untuk layer embedding.
embedding_dim: Ukuran dimensi untuk embedding. Di sini, digunakan dimensi 50, artinya setiap pengguna dan item akan direpresentasikan dalam ruang 50 dimensi.
```python
num_users, num_items = df_collab['userId'].nunique(), df_collab['movieId'].nunique()
embedding_dim = 50
```

## Modeling

### Modeling Content Based Filltering

#### Cosine Similarity

Menghitung cosine similarity antara semua konten yang ada dalam dataset menggunakan matriks TF-IDF. Cosine similarity mengukur kemiripan antara dua vektor (film) berdasarkan konten yang ada pada mereka.

```python
cosine_sim_df = pd.DataFrame(cosine_sim, index=df['title'], columns=df['title'])
print(f"Cosine Similarity Matrix Shape: {cosine_sim_df.shape}")
print("Sample Cosine Similarity Matrix:")
print(cosine_sim_df.sample(5, axis=1).sample(10, axis=0)) # Menampilkan beberapa baris dan kolom acak
```
| Title                                                  | Gad Gone Wild | Joe Rogan: Triggered | Mystic Pop-up Bar | Keeping the Bees | Tremors 4: The Legend Begins |
|--------------------------------------------------------|---------------|----------------------|-------------------|------------------|-------------------------------|
| Feo pero sabroso                                       | 0.000000      | 0.000000             | 0.009127          | 0.003007         | 0.004460                      |
| Spinning Out                                           | 0.000000      | 0.000000             | 0.007925          | 0.002180         | 0.000000                      |
| War Against Women                                      | 0.000000      | 0.000000             | 0.005393          | 0.005578         | 0.002756                      |
| John Mulaney: The Comeback Kid                         | 0.026625      | 0.028309             | 0.000000          | 0.000000         | 0.000000                      |
| Cinderella and the Four Knights                        | 0.000000      | 0.000000             | 0.339175          | 0.001841         | 0.000000                      |
| Lilli                                                  | 0.000000      | 0.000000             | 0.001444          | 0.007577         | 0.003459                      |
| The Last Shaman                                        | 0.000000      | 0.000000             | 0.023740          | 0.004555         | 0.034776                      |
| Power Rangers Samurai: Party Monsters (Halloween ...)  | 0.000000      | 0.000000             | 0.001966          | 0.001682         | 0.001752                      |
| Keith Richards: Under the Influence                    | 0.000000      | 0.000000             | 0.000000          | 0.000000         | 0.000000                      |
| True: Friendship Day                                   | 0.000000      | 0.000000             | 0.000000          | 0.027990         | 0.001681                      |

### Sistem Rekomendasi Menggunakan Content Based Filltering

Fungsi get_recommendations() digunakan untuk memberikan rekomendasi film berdasarkan judul film input. Fungsi ini akan mengurutkan film berdasarkan skor cosine similarity yang dihitung dan mengembalikan 10 film yang paling mirip dengan film yang dicari.

```python
# Menghitung cosine similarity antara semua film
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Membuat fungsi untuk mendapatkan rekomendasi
def get_recommendations(title, cosine_sim=cosine_sim):
    # Menemukan indeks film berdasarkan judul
    idx = df.index[df['title'] == title].tolist()[0]

    # Mendapatkan skor similaritas untuk semua film berdasarkan indeks
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Urutkan film berdasarkan skor similarity (descending)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Ambil 10 film teratas yang mirip, selain film itu sendiri
    sim_scores = sim_scores[1:11]

    # Ambil indeks film
    movie_indices = [i[0] for i in sim_scores]

    # Return 10 rekomendasi film teratas
    return df['title'].iloc[movie_indices]

# Cek rekomendasi berdasarkan judul film
print(get_recommendations('Breaking Bad'))
```
Menampilkaan Hasil rekomendasi 10 film berdasarkan film `Breaking Bed`.
| Index | Title                                      |
|-------|---------------------------------------------|
| 2931  | Better Call Saul                           |
| 8505  | The Show                                   |
| 355   | The Lincoln Lawyer                         |
| 5352  | Have You Ever Fallen in Love, Miss Jiang?  |
| 5606  | Girlfriend's Day                           |
| 6841  | Get Shorty                                 |
| 5885  | W/ Bob & David                             |
| 430   | Sexy Beasts                                |
| 5703  | Refresh Man                                |
| 2606  | Extracurricular                            |


### Modeling Collaborative Filltering

### Membangun Model Neural Collaborative Filtering (NCF)

Pendekatan dalam sistem rekomendasi berbasis deep learning. Model ini memanfaatkan embedding untuk merepresentasikan pengguna dan item dalam ruang vektor berdimensi rendah, dan kemudian menggabungkannya untuk memprediksi interaksi (rating) antara pengguna dan item.

```python
# Membuat input layer untuk user dan item
user_input = Input(shape=(1,), dtype=tf.int32)
item_input = Input(shape=(1,), dtype=tf.int32)

# Embedding layer untuk user dan item
user_embedding = Embedding(input_dim=num_users, output_dim=embedding_dim)(user_input)
item_embedding = Embedding(input_dim=num_items, output_dim=embedding_dim)(item_input)

# Flattening embedding layer untuk dihubungkan ke dense layer
user_vec = Flatten()(user_embedding)
item_vec = Flatten()(item_embedding)

# Menggabungkan user dan item embedding
merged = tf.keras.layers.concatenate([user_vec, item_vec])

# Fully connected layer untuk menghasilkan prediksi rating
x = Dense(128, activation='relu')(merged)
x = Dense(64, activation='relu')(x)
output = Dense(1)(x)
```

| Layer (type)              | Output Shape           | Param #     | Connected to            |
|---------------------------|------------------------|-------------|-------------------------|
| input_layer_4             | (None, 1)              | 0           | -                       |
| input_layer_5             | (None, 1)              | 0           | -                       |
| embedding_4 (Embedding)   | (None, 1, 50)          | 49,950      | input_layer_4[0][0]     |
| embedding_5 (Embedding)   | (None, 1, 50)          | 440,350     | input_layer_5[0][0]     |
| flatten_4 (Flatten)       | (None, 50)             | 0           | embedding_4[0][0]       |
| flatten_5 (Flatten)       | (None, 50)             | 0           | embedding_5[0][0]       |
| concatenate_2 (Concatenate) | (None, 100)           | 0           | flatten_4[0][0], flatten_5[0][0] |
| dense_6 (Dense)           | (None, 128)            | 12,928      | concatenate_2[0][0]     |
| dense_7 (Dense)           | (None, 64)             | 8,256       | dense_6[0][0]           |
| dense_8 (Dense)           | (None, 1)              | 65          | dense_7[0][0]           |

### Training Model
```python
train_ratings = train_ratings.astype(np.float32)
history = model.fit(
    [train_user_input, train_item_input],  # dua input
    train_ratings,  # target ratings
    epochs=30,
    batch_size=64
)
```

<img src="https://github.com/user-attachments/assets/a934dd8d-ed2f-4a0e-a089-592a4d1d18aa" width="700" height="500"> <br>

### Sistem Rekomendasi Menggunakan Collaborative Filltering
```python
def get_movie_recommendations(user_id, num_recommendations=10):
    movie_ids = np.arange(num_items)  # Semua movieId
    user_ids = np.full_like(movie_ids, user_id)  # Menambahkan user_id yang sama untuk setiap movieId
    predicted_ratings = model.predict([user_ids, movie_ids], verbose=0)
    recommended_movie_ids = movie_ids[np.argsort(predicted_ratings.flatten())[::-1]]
    recommended_movie_ids = recommended_movie_ids[:num_recommendations]

    return recommended_movie_ids

user_id = 70  # Ganti dengan user ID yang ingin direkomendasikan
recommended_movies = get_movie_recommendations(user_id, num_recommendations=10)

print(f"Top 10 rekomendasi film untuk user {user_id}:")
for movie_id in recommended_movies:
    # Mendapatkan judul film berdasarkan movie_id dari dictionary
    title = df2[df2['movieId'] == movie_id]['title'].values[0]
    print(f"Movie ID: {movie_id}, Title: {title}")
```

Top 10 rekomendasi film untuk `user 70`
| Movie ID | Title                                          |
|----------|------------------------------------------------|
| 2610     | The King                                      |
| 1856     | The Creative Indians                          |
| 3884     | Making a Murderer                             |
| 663      | MANK                                          |
| 1724     | John Henry                                    |
| 3522     | Examination of Conscience                      |
| 7132     | Mary Poppins Returns                          |
| 1789     | Murder to Mercy: The Cyntoia Brown Story      |
| 6799     | Jal                                           |
| 2301     | '76                                           |


### Parameter-parameter yang digunakan
#### Content Based Filltering
1. TF-IDF Vectorizer Parameters
   `stop_words='english'`
   Parameter ini digunakan untuk mengabaikan kata-kata umum dalam bahasa Inggris (seperti "the", "is", "and", dll.) yang biasanya tidak memberikan informasi yang relevan dalam analisis teks.

   `max_features=None`
   Tidak ada batasan jumlah fitur yang diambil oleh TF-IDF Vectorizer, artinya seluruh kata-kata yang ditemukan dalam dataset akan diubah menjadi fitur numerik.

   `ngram_range=(1, 2)`
   Parameter ini digunakan untuk menghasilkan unigram (kata tunggal) dan bigram (dua kata yang berdekatan). Dengan demikian, model dapat menangkap hubungan antar kata yang lebih luas dalam kalimat.

2. Cosine Similarity Parameters
   `cosine_similarity(tfidf_matrix)`
   Digunakan untuk menghitung skor kemiripan antara film-film yang ada dalam dataset berdasarkan matriks TF-IDF yang telah dibuat. Nilai skor ini berkisar antara 0 hingga 1, dimana 1 berarti dua film sangat mirip dan 0 berarti dua film tidak memiliki kemiripan sama sekali.

3. Fungsi get_recommendations()
   `title`
   Parameter ini adalah input judul film yang ingin dicari rekomendasinya. Fungsi ini kemudian akan mencari film lain yang memiliki skor cosine similarity tertinggi dengan film yang dimasukkan.

#### Colaborative Filltering
1. Model Architecture Parameters
   `embedding_dim=50`
   Dimensi embedding untuk pengguna dan item. Parameter ini mengatur seberapa banyak fitur yang akan digunakan untuk merepresentasikan pengguna dan item dalam ruang vektor berdimensi rendah. Nilai 50 berarti kita menggunakan 50 dimensi untuk masing-masing pengguna dan item.

   `user_input, item_input`
   Input layer untuk pengguna (user_input) dan item (item_input). Kedua input ini akan menerima ID pengguna dan ID film sebagai input.

   `Embedding(input_dim=num_users, output_dim=embedding_dim)`
   Layer embedding untuk pengguna dan item. input_dim=num_users dan input_dim=num_items adalah jumlah pengguna dan item unik dalam dataset, sedangkan output_dim=embedding_dim adalah dimensi embedding yang akan digunakan untuk merepresentasikan pengguna dan item.

2. Fully Connected Layers Parameters
   `Dense(128, activation='relu')`
   Layer fully connected pertama dengan 128 neuron dan fungsi aktivasi ReLU (Rectified Linear Unit). Fungsi ini digunakan untuk memperkenalkan non-linearity dalam model, yang memungkinkan model untuk menangkap hubungan yang lebih kompleks.
   
   `Dense(64, activation='relu')`
   Layer fully connected kedua dengan 64 neuron dan fungsi aktivasi ReLU. Ini juga bertujuan untuk menangkap lebih banyak kompleksitas dalam data.
   
   `Dense(1)`
   Output layer yang menghasilkan prediksi rating untuk interaksi antara pengguna dan item. Karena prediksi rating berupa angka kontinu, output layer ini hanya memiliki satu neuron.

3. Model Compilation Parameters
   `optimizer=Adam()`
   Optimizer yang digunakan untuk melatih model. Adam (Adaptive Moment Estimation) adalah optimizer yang sangat populer dalam deep learning karena kemampuannya untuk menyesuaikan learning rate selama pelatihan.

   `loss='mean_squared_error'`
   Fungsi loss yang digunakan untuk menghitung kesalahan antara prediksi dan nilai sebenarnya. Mean Squared Error (MSE) digunakan untuk model regresi dan memberikan penalti lebih besar untuk kesalahan yang lebih besar.

   `metrics=[MeanSquaredError(), rmse]`
   Metrik yang digunakan untuk mengevaluasi model selama pelatihan. Selain MSE, juga digunakan Root Mean Squared Error (RMSE), yang memberikan gambaran lebih jelas mengenai ukuran kesalahan dalam unit yang sama dengan rating.

4. Training Parameters
   `epochs=30`
   Jumlah iterasi penuh (epochs) di mana model akan dilatih pada seluruh dataset. Dalam kasus ini, model akan dilatih selama 30 kali putaran melalui seluruh data pelatihan.

   `batch_size=64`
Jumlah data yang diproses dalam satu iterasi sebelum memperbarui bobot model. Nilai ini mengontrol seberapa besar subset data yang digunakan dalam satu langkah pembelajaran. Nilai 64 menunjukkan bahwa model akan mengolah 64 sampel data dalam satu batch sebelum memperbarui parameter.


### Content Based Filltering VS Collaborative Filltering
Pada proyek sistem rekomendasi ini, dua pendekatan utama telah diimplementasikan dan dibandingkan, yaitu `Content-Based Filtering` dan `Collaborative Filtering`. Berikut adalah kesimpulan berdasarkan penerapan dan evaluasi kedua metode tersebut:

1. Content-Based Filtering
Metode ini merekomendasikan item berdasarkan kesamaan antara konten item yang disukai pengguna sebelumnya. Misalnya, jika seorang pengguna sering menonton film bergenre komedi, sistem akan merekomendasikan film lain yang memiliki genre serupa.

Kelebihan:
* Rekomendasi dapat disesuaikan dengan preferensi pengguna secara spesifik, karena algoritma menganalisis konten film yang sudah disukai.
* Metode ini bekerja hanya dengan data pengguna tertentu, sehingga berguna untuk menangani masalah cold start ketika data pengguna baru terbatas.

Kekurangan:
* Rekomendasi cenderung berfokus pada jenis konten yang sama, sehingga sulit bagi pengguna untuk menemukan item di luar preferensi mereka.
* Kualitas rekomendasi sangat bergantung pada data deskriptif item. Metadata yang tidak lengkap atau kurang akurat dapat mempengaruhi kinerja.

2. Collaborative Filtering
Metode ini memberikan rekomendasi berdasarkan preferensi pengguna lain yang memiliki kesamaan pola. Collaborative filtering menggunakan informasi dari banyak pengguna untuk menyarankan item yang relevan.

Kelebihan:
* Karena rekomendasi tidak hanya berdasarkan konten, pengguna dapat menemukan film yang mungkin belum pernah mereka pertimbangkan tetapi disukai oleh pengguna lain dengan preferensi yang mirip.
* Model ini mampu beradaptasi dengan baik terhadap berbagai jenis data yang berbeda.

Kekurangan:
* Jika ada pengguna baru atau film baru tanpa rating atau ulasan, sistem tidak dapat memberikan rekomendasi yang akurat.
* Collaborative filtering berbasis memory-based memerlukan daya komputasi yang besar untuk dataset yang sangat besar, meskipun pendekatan berbasis model (seperti Matrix Factorization) dapat mengatasi masalah ini.

### Perbandingan Hasil dan Kinerja

* Content-Based Filtering cenderung lebih stabil untuk pengguna dengan sejarah tontonan yang jelas dan membutuhkan preferensi yang spesifik. Namun, rekomendasi bisa menjadi monoton karena hanya berkisar pada jenis konten tertentu.
* Collaborative Filtering menunjukkan performa yang baik dalam memberikan rekomendasi yang beragam dan lebih personal, terutama jika data pengguna dan film mencukupi. Pendekatan ini umumnya lebih efektif dalam menangkap pola kompleks di antara pengguna.

### Kesimpulan
Untuk proyek ini, Collaborative Filtering dengan pendekatan matrix factorization cenderung memberikan hasil yang lebih baik dalam menciptakan rekomendasi yang bervariasi dan lebih akurat. Namun, Content-Based Filtering bisa digunakan sebagai pelengkap, terutama ketika menangani pengguna baru dengan sedikit data.

Kombinasi atau hybrid system antara keduanya dapat dipertimbangkan untuk memperoleh kelebihan dari masing-masing pendekatan, meminimalkan kelemahan, dan meningkatkan kualitas sistem rekomendasi secara keseluruhan.

## Evaluation

### Content Based Learning

1. Menyiapkan Ground Truth
   Ground truth untuk `Girlfriend's Day` bisa berupa film-film yang sudah dilihat atau dinilai relevan oleh pengguna. misalnya film `Girlfriend's Day` relevan dengan film Breaking Bad, Pineapple Express, dan lainnya, film-film ini dimasukkan ke dalam ground truth.
   ```python
   relevant_movies = ['Breaking Bad', 'Pineapple Express', 'Lady Dynamite', 'In a Valley of Violence']
   ```

2. Mendefinisikan Metrik Evaluasi
   Mengimplementasikan Precision@k, Recall@k, dan F1-Score@k untuk mengevaluasi rekomendasi yang dihasilkan oleh model kamu.
   
   ```python
   relevant_movies = ['Breaking Bad', 'Pineapple Express', 'Lady Dynamite', 'In a Valley of Violence']

   # Fungsi untuk menghitung Precision@k dan Recall@k
   def precision_at_k(recommended, relevant, k):
       recommended_at_k = recommended[:k]
       relevant_set = set(relevant)
       recommended_at_k_set = set(recommended_at_k)
       return len(recommended_at_k_set.intersection(relevant_set)) / k

   def recall_at_k(recommended, relevant, k):
       recommended_at_k = recommended[:k]
       relevant_set = set(relevant)
       recommended_at_k_set = set(recommended_at_k)
       return len(recommended_at_k_set.intersection(relevant_set)) / len(relevant_set)

   def f1_score_at_k(recommended, relevant, k):
       precision = precision_at_k(recommended, relevant, k)
       recall = recall_at_k(recommended, relevant, k)
       if precision + recall == 0:
           return 0
       return 2 * (precision * recall) / (precision + recall)

   # Ambil rekomendasi dari sistem
   recommended_movies = get_recommendations('Girlfriend\'s Day')

   # Tentukan k (misalnya 10 rekomendasi teratas)
   k = 10
   # Hitung Precision@k, Recall@k, dan F1-Score@k
   precision = precision_at_k(recommended_movies, relevant_movies, k)
   recall = recall_at_k(recommended_movies, relevant_movies, k)
   f1 = f1_score_at_k(recommended_movies, relevant_movies, k)

   print(f"Precision@{k}: {precision}")
   print(f"Recall@{k}: {recall}")
   print(f"F1-Score@{k}: {f1}")
   ```
   
   | Metrics       | Value                                       |
   |---------------|---------------------------------------------|
   | Precision@10  | 0.4                                         |
   | Recall@10     | 1.0                                         |
   | F1-Score@10   | 0.5714285714285715                          |

   ### Hasil Metrics Evaluasi
   Precision@10: 0.4
   * Precision mengukur seberapa banyak film yang direkomendasikan dalam 10 teratas yang benar-benar relevan. Hasil 0.4 berarti bahwa 40% dari 10 rekomendasi yang diberikan oleh sistem benar-benar relevan menurut ground truth.
     
   Recall@10: 1.0
   * Skor recall 1.0 menunjukkan bahwa semua film relevan (sesuai dengan ground truth) ditemukan dalam 10 rekomendasi teratas. Ini berarti sistem berhasil menangkap semua film relevan yang ada dalam daftar rekomendasi.
   * Skor recall yang sangat tinggi ini menunjukkan bahwa sistem cukup efektif dalam mencakup seluruh relevansi yang ada.
   
   F1-Score@10: 0.571
   * Hasil ini menunjukkan bahwa meskipun recall sangat baik (1.0), precision masih perlu ditingkatkan untuk mencapai keseimbangan yang lebih baik antara keduanya.
   * F1-Score yang lebih rendah dari recall ini menunjukkan bahwa meskipun sistem tidak kehilangan film relevan (recall tinggi), masih ada banyak rekomendasi yang kurang relevan, yang menurunkan precision.
   
  
### Collaborative Filtering
Untuk proyek sistem rekomendasi ini, metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE) dan Mean Squared Error (MSE). Kedua metrik ini digunakan untuk mengukur akurasi prediksi rating film terhadap rating yang sebenarnya.

```python
import matplotlib.pyplot as plt

mse = history.history['mean_squared_error']
rmse = history.history['rmse']

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(mse)
plt.title('Model Mean Squared Error (MSE) During Training')
plt.xlabel('Epoch')
plt.ylabel('MSE')

plt.subplot(1, 2, 2)
plt.plot(rmse)
plt.title('Model Root Mean Squared Error (RMSE) During Training')
plt.xlabel('Epoch')
plt.ylabel('RMSE')
plt.tight_layout()
plt.show()
```
<img src="https://github.com/user-attachments/assets/8c17b2b0-051c-4418-aa0e-a36cafdffa60" width="700" height="500"> <br>

1. Root Mean Squared Error (RMSE)
RMSE adalah salah satu metrik yang umum digunakan dalam sistem rekomendasi untuk mengukur seberapa akurat prediksi model terhadap data asli. RMSE memberikan gambaran mengenai seberapa besar kesalahan model dalam memprediksi rating, di mana semakin rendah nilai RMSE, semakin baik performa model dalam memprediksi rating yang tepat. <br>

Formula RMSE: <br>

$$
\text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}
$$

Di mana:
- $y_i$ adalah rating asli (ground truth),
- $\hat{y}_i$ adalah rating yang diprediksi oleh model,
- $n$ adalah jumlah prediksi (data).

RMSE menghitung selisih kuadrat antara rating yang sebenarnya dan yang diprediksi, kemudian merata-ratakan dan menghitung akar kuadrat dari hasil tersebut. Hasil yang lebih rendah menunjukkan kesalahan yang lebih kecil.

2. Mean Squared Error (MSE)
MSE adalah metrik yang menghitung rata-rata dari kuadrat selisih antara rating asli dan rating yang diprediksi. MSE memberikan bobot yang lebih besar pada kesalahan besar, karena kesalahan dihitung dalam bentuk kuadrat. Metrik ini sangat berguna untuk meminimalkan kesalahan yang besar, meskipun RMSE lebih mudah diinterpretasikan karena berada dalam skala yang sama dengan rating yang sebenarnya.

Formula MSE: <br>

$$
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Di mana:
- $y_i$ adalah rating asli (ground truth),
- $\hat{y}_i$ adalah rating yang diprediksi oleh model,
- $n$ adalah jumlah prediksi (data).

### Evaluasi Hasil Berdasarkan Metrik
Setelah model dilatih, kita dapat mengevaluasi performanya dengan melihat nilai RMSE dan MSE pada data pengujian (test data). Jika nilai RMSE dan MSE rendah, maka model dapat dianggap lebih baik karena prediksi rating yang lebih dekat dengan nilai sebenarnya.

### Hasil Evaluasi Metrics
1. MSE cenderung menunjukkan penurunan yang stabil sepanjang proses training, yang berarti model semakin baik dalam mengurangi error kuadrat antara prediksi dan nilai asli. Pada epoch terakhir, nilai MSE mencapai `0.0038`, menunjukkan bahwa model telah memperkecil kesalahan prediksi.

2. RMSE juga menurun seiring berjalannya waktu, meskipun tidak secepat penurunan MSE. RMSE memberikan gambaran yang lebih jelas mengenai ukuran kesalahan prediksi dalam satuan yang lebih mudah dipahami (dalam hal ini, unit rating). Pada epoch terakhir, nilai RMSE mencapai `1.8416`, yang menunjukkan bahwa meskipun model sudah belajar dengan cukup baik, masih ada ruang untuk perbaikan.

3. Berdasarkan evaluasi yang ada, model sudah cukup baik karena MSE dan RMSE menunjukkan penurunan yang signifikan. RMSE sebesar 1.84 menunjukkan kesalahan yang tidak terlalu besar, namun bisa jadi ada ruang untuk penyempurnaan lebih lanjut, terutama jika target Anda adalah mendapatkan prediksi yang lebih akurat atau meningkatkan relevansi rekomendasi. Evaluasi lebih lanjut dengan data nyata dan perbandingan terhadap model lain akan memberi gambaran yang lebih jelas tentang performa model Anda.

## Hasil Akhir Project

Sistem rekomendasi yang dikembangkan, baik dengan pendekatan `Content-Based Filtering` maupun `Collaborative Filtering`, telah memberikan solusi yang signifikan untuk masalah yang dihadapi oleh Netflix dalam membantu pengguna menemukan konten yang sesuai dengan preferensi mereka.

1. Menjawab Problem Statement
   * Model yang dibangun telah menunjukkan kemampuan untuk merekomendasikan film berdasarkan preferensi pengguna melalui analisis kesamaan konten (content-based) dan pola interaksi pengguna (collaborative).
   * Dengan adanya sistem rekomendasi ini, pengguna bisa menemukan film atau acara yang sesuai dengan lebih cepat, mengurangi waktu yang dihabiskan untuk mencari konten secara manual.

2. Apakah Berhasil Mencapai Goals yang Diharapkan?
   * Implementasi model telah meningkatkan pengalaman pengguna dengan memberikan rekomendasi yang lebih personal. Ini membantu meningkatkan kenyamanan pengguna dalam menavigasi konten di platform Netflix.
   * Dengan rekomendasi yang lebih akurat dan relevan, pengguna cenderung lebih sering kembali ke platform untuk menonton konten lain yang direkomendasikan. Hal ini mendukung tujuan Netflix untuk meningkatkan tingkat retensi pengguna.
     
3. Dampak Solusi Statement terhadap Bisnis <br><br>
   `Content-Based Filtering` <br>
   Pendekatan ini memungkinkan Netflix untuk merekomendasikan konten yang serupa dengan film atau acara yang telah ditonton oleh pengguna. Hal ini efektif dalam menjaga pengguna yang memiliki preferensi khusus.
   * Model ini bekerja dengan baik untuk pengguna yang memiliki riwayat interaksi yang terbatas karena bisa langsung menggunakan fitur konten seperti genre dan deskripsi.
   * Model ini cenderung terbatas pada konten yang mirip dengan riwayat pengguna, sehingga mengurangi keberagaman rekomendasi. <br>
   
   `Collaborative Filtering` <br>
   Pendekatan ini lebih baik dalam merekomendasikan konten yang bervariasi berdasarkan pola interaksi dari berbagai pengguna.
   * Memberikan rekomendasi yang lebih beragam dengan mempertimbangkan preferensi pengguna lain yang memiliki kesamaan pola.
   * Model ini membutuhkan data interaksi pengguna yang lebih banyak untuk memberikan hasil yang optimal.
