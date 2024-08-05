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


### 3.2 Data Preparation

## Dataframe Info
```python
reviews_df.info()
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/1c5fd506cdd803e5cae5e3017772f54a4a957a10/Submission/Assets/df-info.png" width="400"/>

### 3.3 Text Processing

## Cleaning Text
```python
def cleaningText(text):
    text = re.sub(r'@[A-Za-z0-9]+', '', text)  # remove mentions
    text = re.sub(r'#[A-Za-z0-9]+', '', text)  # remove hashtags
    text = re.sub(r'RT[\s]', '', text)  # remove RT
    text = re.sub(r'http\S+', '', text)  # remove links
    text = re.sub(r'[0-9]+', '', text)  # remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation except spaces

    text = text.replace('\n', ' ')  # replace new line into space
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove all punctuations
    text = text.strip()  # remove leading and trailing spaces
    return text
```
## Case Folding Text
```python
def casefoldingText(text):
    return text.lower()
```

## Tokenizing Text
```python
def tokenizingText(text):
    return word_tokenize(text)
```
## Filtering Text
```python
def filteringText(tokens):
    listStopwords = set(stopwords.words('indonesian'))
    listStopwords1 = set(stopwords.words('english'))
    listStopwords.update(listStopwords1)
    listStopwords.update(['iya', 'yaa', 'gak', 'nya', 'na', 'sih', 'ku', "di", "ga", "ya", "gaa", "loh", "kah", "woi", "woii", "woy"])
    return [word for word in tokens if word not in listStopwords]
```

## Stemming Text
```python
def stemmingText(text):
    # Membuat objek stemmer
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()

    # Memecah teks menjadi daftar kata
    words = text.split()

    # Menerapkan stemming pada setiap kata dalam daftar
    stemmed_words = [stemmer.stem(word) for word in words]

    # Menggabungkan kata-kata yang telah distem
    return ' '.join(stemmed_words)
```

## List Token to Sentence
```python
def toSentence(list_words):
    return ' '.join(word for word in list_words)
```

### 3.4 Labeling
```python
def analyze_sentiment(words, positive_lexicon, negative_lexicon):

    sentiment_score = 0

    for word in words:
        if word in positive_lexicon:
            sentiment_score += positive_lexicon[word]

    for word in words:
        if word in negative_lexicon:
            sentiment_score += negative_lexicon[word]

    if sentiment_score > 0:
        sentiment_polarity = 'positive'
    elif sentiment_score < 0:
        sentiment_polarity = 'negative'
    else:
        sentiment_polarity = 'neutral'

    return sentiment_score, sentiment_polarity

def apply_sentiment_analysis(df, text_column, positive_lexicon, negative_lexicon):

    def sentiment_function(words):
        return analyze_sentiment(words, positive_lexicon, negative_lexicon)

    sentiment_results = df[text_column].apply(sentiment_function)

    sentiment_scores, sentiment_polarities = zip(*sentiment_results)

    df['sentiment_score'] = sentiment_scores
    df['sentiment_polarity'] = sentiment_polarities

    return df

cleaned_df = apply_sentiment_analysis(cleaned_df, 'text_stopword', lexicon_positive, lexicon_negative)

print(cleaned_df['sentiment_polarity'].value_counts())

```

### 3.5 Training Model

## Logistic Regression

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

log_reg_model = LogisticRegression(max_iter=1000, random_state=42)
log_reg_model.fit(X_train, y_train)

y_train_pred_lr = log_reg_model.predict(X_train)
y_test_pred_lr = log_reg_model.predict(X_test)

train_accuracy_lr = accuracy_score(y_train, y_train_pred_lr)
test_accuracy_lr = accuracy_score(y_test, y_test_pred_lr)
report = classification_report(y_test, y_test_pred_lr, target_names=y.unique())
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/a7e9b132ff6f5d4eb6d43ba2fd3ebe7c17c63f6f/Assets/report-model-lr.png" width="500"/>

## Light GBM

```python
import lightgbm as lgb
from sklearn.metrics import accuracy_score, classification_report

lgbm_model = lgb.LGBMClassifier(random_state=42)
lgbm_model.fit(X_train, y_train)

y_train_pred_lgbm = lgbm_model.predict(X_train)
y_test_pred_lgbm = lgbm_model.predict(X_test)

train_accuracy_lgbm = accuracy_score(y_train, y_train_pred_lgbm)
test_accuracy_lgbm = accuracy_score(y_test, y_test_pred_lgbm)
report = classification_report(y_test, y_test_pred_lgbm, target_names=y.unique())
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/a7e9b132ff6f5d4eb6d43ba2fd3ebe7c17c63f6f/Assets/report-model-lgbm.png" width="500"/>

## SVM

```python
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

svm_model = SVC(kernel='linear', random_state=42)

svm_model.fit(X_train, y_train)

y_train_pred_svm = svm_model.predict(X_train)
y_test_pred_svm = svm_model.predict(X_test)

train_accuracy_svm = accuracy_score(y_train, y_train_pred_svm)
test_accuracy_svm = accuracy_score(y_test, y_test_pred_svm)
svm_report = classification_report(y_test, y_test_pred_svm, target_names=y.unique())
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/a7e9b132ff6f5d4eb6d43ba2fd3ebe7c17c63f6f/Assets/report-model-svm.png" width="500"/>

## MLP

```python
from sklearn.neural_network import MLPClassifier

mlp_model = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500, random_state=42)

mlp_model.fit(X_train, y_train)

y_train_pred_mlp = mlp_model.predict(X_train)
y_test_pred_mlp = mlp_model.predict(X_test)

train_accuracy_mlp = accuracy_score(y_train, y_train_pred_mlp)
test_accuracy_mlp = accuracy_score(y_test, y_test_pred_mlp)
mlp_report = classification_report(y_test, y_test_pred_mlp, target_names=y.unique())
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/a7e9b132ff6f5d4eb6d43ba2fd3ebe7c17c63f6f/Assets/report-model-mlp.png" width="500"/>

## 4. Predict
```python
kalimat_baru = input("Masukkan kalimat baru: ")

kalimat_baru_cleaned = cleaningText(kalimat_baru)
kalimat_baru_casefolded = casefoldingText(kalimat_baru_cleaned)
kalimat_baru_slangfixed = fix_slangwords(kalimat_baru_casefolded)
kalimat_baru_tokenized = tokenizingText(kalimat_baru_slangfixed)
kalimat_baru_filtered = filteringText(kalimat_baru_tokenized)
kalimat_baru_final = toSentence(kalimat_baru_filtered)

X_kalimat_baru_tfidf = tfidf.transform([kalimat_baru_final])

text_length_new = len(kalimat_baru_final.split())

X_kalimat_baru_combined = hstack([X_kalimat_baru_tfidf, [[text_length_new]]])

prediksi_sentimen = log_reg_model.predict(X_kalimat_baru_combined)

if prediksi_sentimen[0] == 'positive':
    print("Sentimen kalimat baru adalah POSITIF.")
else:
    print("Sentimen kalimat baru adalah NEGATIF.")
```

<img src="https://github.com/shendyeff/learn-dicoding/blob/a5082f6817bcb1a14fddb27898aac849d459b90e/Assets/predict.png" width="500"/>

## 5. Conclusion
This sentiment analysis project provides valuable insights into user perceptions of the Grab app. By using NLP and machine learning techniques, we can identify user sentiments and suggest improvements that can increase customer satisfaction. The built model has good accuracy and can be implemented in an automated sentiment analysis system.

You can access for google colab link

[![Open in Google Drive](https://img.shields.io/badge/Open%20in-Google%20Drive-blue)](https://colab.research.google.com/drive/19Gyiqn-5UpGGg19aNcoV7FjSaiFAKuor?usp=sharing)
