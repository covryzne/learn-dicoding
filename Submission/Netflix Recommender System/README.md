# Laporan Proyek Machine Learning - Shendi Teuku Maulana Efendi

## Project Overview

With the rapid growth of streaming services like Netflix, users are often overwhelmed by thousands of movie and TV show options. This phenomenon, known as information overload, can make it difficult for users to find content that matches their preferences. To address this issue, recommendation systems play a vital role in guiding users toward relevant and appealing content.

Recommendation systems have proven essential in enhancing user experience and maintaining high engagement levels. Studies indicate that over 80% of the content watched on Netflix is driven by algorithmic recommendations [Smith et al., The Role of Recommendation Systems in User Engagement](https://link.springer.com/article/10.1186/s12889-021-11803-8). These systems create a more personalized experience, increasing watch time and ultimately boosting user retention.

In this project, I will develop a recommendation system using a Content-Based Filtering approach. This method leverages content attributes, such as directors, cast, genres, and descriptions, to create unique profiles for each movie. These profiles are then matched with user preferences based on their viewing history.

## Business Understanding
In this section, we will clarify the core problems that the project aims to solve and outline the objectives and strategies to address these challenges.

### Problem Statements
1. How can we develop a recommendation system that accurately suggests movies and shows based on the user's viewing preferences and history?
Problem Statement
2. How can we handle the cold start problem for new content that lacks sufficient user interaction data?
Problem Statement
3. How can we ensure that the recommendation system maintains a high level of relevance and engagement, keeping users satisfied over time?

### Goals
1. Build a content-based recommendation system that effectively matches user preferences with movie attributes (e.g., genre, director, cast).
Goal for Problem Statement.
2. Implement a system that can recommend new content by relying on content attributes instead of user interaction data.
Goal for Problem Statement.
3. Develop an evaluation framework to measure the relevance of recommendations and enhance system performance based on user feedback.

### Solution Approach

To achieve these goals, we propose the following solution approaches:

#### Solution Statements
1. Content-Based Filtering Algorithm

* Approach: Utilize TF-IDF Vectorization or other text representation techniques to encode movie descriptions, genres, and cast data into numerical features.
* Method: Apply cosine similarity to find the most similar content based on user preferences, ensuring the recommendations align with the characteristics of previously watched movies.

2. Cold Start Strategy

* Approach: Incorporate a hybrid content-profiling method that leverages detailed metadata (such as director, cast, listed_in, and description) to ensure new items can be recommended even without user interaction data.
* Method: Implement a fallback system that prioritizes trending or highly-rated new releases using content attributes for new users.

3. Evaluation and Improvement

* Approach: Use metrics such as precision, recall, and F1-score to evaluate the relevance of the recommendations. Implement feedback loops for continuous improvement based on user interactions and preferences.
* Method: Collect manual assessments and user ratings, and iterate on the model by adjusting weightings for different content attributes.

## Data Understanding

The dataset used in this project contains information about 8,807 movies and TV shows available on the Netflix platform. This dataset provides detailed attributes for each show, including metadata that can be leveraged to create a content-based recommendation system. The data can be downloaded from [Kaggle Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows).

The dataset consists of 12 columns, with a mix of numerical and categorical variables. Some values are missing, and these gaps will be handled during the data preprocessing phase.

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

The dataset contains some missing values in columns such as `director`, `cast`, `country`, and `date_added`. These missing values will be handled by either imputing with placeholder values, using a different method, or removing rows/columns with excessive missing data. The data will be preprocessed to ensure the quality and consistency of the information for building the recommendation system.

## Data Preparation
Pada bagian ini Anda menerapkan dan menyebutkan teknik data preparation yang dilakukan. Teknik yang digunakan pada notebook dan laporan harus berurutan.

**Rubrik/Kriteria Tambahan (Opsional)**: 
- Menjelaskan proses data preparation yang dilakukan
- Menjelaskan alasan mengapa diperlukan tahapan data preparation tersebut.

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
