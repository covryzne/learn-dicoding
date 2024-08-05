# **Documentation Sentiment Analysis Grab DICODING**
This project aims to analyze the sentiment of Grab app user reviews.

## Table of Contents
1. [Introduction](#1-introduction)
2. [Objective](#2-objective)

## 1. Introduction
As technology develops and the use of transportation service applications such as Grab increases, 
user reviews become an important source of information to understand customer satisfaction and dissatisfaction. 
are becoming an important source of information to understand customer satisfaction and dissatisfaction. 
Sentiment analysis is technique that can be used to extract and understand users' feelings from their review texts. 
This project aims to analyze the sentiment of Grab app user reviews, helping the company to improve its services based on customer feedback. 
feedback from customers.

## 2. Objective
The objectives of this project are:
* Collect and process Grab app user review data from Google Play Store.
* Apply natural language processing (NLP) techniques to clean and prepare the review data.
* Train a machine learning model to classify the sentiment of reviews as positive or negative.
* Evaluate the built model and provide useful insights for Grab service improvement.

## 3. Method
### 3.1 Collecting Data
User review data is collected using data scraping to retrieve data from the Google Play Store. Each review includes the required information.

## Scrapping Data

### Install Libraries
```python
!pip install google-play-scraper
```

### Import Libraries
```python
from google_play_scraper import app, reviews, Sort, reviews_all

reviews_data = reviews_all(
    'com.grabtaxi.passenger',  # ID aplikasi Grab
    lang='id',                # Bahasa ulasan
    country='id',             # Negara
    sort=Sort.MOST_RELEVANT,  # Urutan ulasan
    count=10000               # Jumlah maksimum ulasan
)
```

### Export to CSV File
```python
import csv

with open('grab_reviews.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])  # Menulis header kolom
    for review in reviews_data:
        writer.writerow([review['content']])  # Menulis konten ulasan ke dalam file CSV
```

## Export CSV to Dataframe
```python
import pandas as pd
reviews_df = pd.DataFrame(reviews_data)
reviews_df.to_csv('grab_reviews.csv', index=False)
```

After scrapping the data, the dataset can be accessed here.
[![Open in Google Drive](https://img.shields.io/badge/Open%20in-Google%20Drive-blue)](https://drive.google.com/file/d/12DmWM9TnNdV661L4UEpkDs6_9MumzJ55/view?usp=drive_link)


### 3.2 Text Processing
