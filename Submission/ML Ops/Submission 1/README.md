# **Submission 1: Spam Email Machine Learning Pipeline**

**Nama:** `Shendi Teuku Maulana Efendi`<br>
**Username Dicoding:** `shendyeff`

<img src="https://github.com/shendyeff/learn-dicoding/blob/cde398abc771d0a04304a8e35ec964b55b203011/Submission/ML%20Ops/Submission%201/assets/cover.png">

|                         | Deskripsi                                                                       |
| ----------------------- | ------------------------------------------------------------------------------- |
| Dataset                 | [Email Spam Dataset](https://www.kaggle.com/datasets/mfaisalqureshi/spam-email) |
| Masalah                 | Masalah yang diangkat dalam proyek ini adalah klasifikasi email untuk menentukan apakah sebuah email merupakan spam atau tidak. Di dunia digital yang semakin berkembang, jumlah email yang masuk ke dalam kotak masuk (inbox) setiap hari meningkat secara signifikan. Banyak dari email tersebut adalah spam, yang dapat mengganggu dan menghambat produktivitas penggunanya. Masalahnya adalah bagaimana cara otomatis mendeteksi dan mengklasifikasikan email spam untuk mengurangi jumlah email yang tidak diinginkan, sehingga hanya email yang relevan yang masuk ke inbox pengguna.|
| Solusi machine learning | Solusi machine learning yang diusulkan adalah membangun model klasifikasi yang dapat memisahkan email menjadi dua kategori: **`spam`** dan **`bukan spam`**. Model ini akan menggunakan teknik pembelajaran mendalam (deep learning) dengan memanfaatkan arsitektur **`neural network`**, seperti **`LSTM`** dan **`Dense layers**`, untuk mempelajari pola dan fitur-fitur penting dari teks email. Dataset yang digunakan akan diproses dan dimodifikasi menggunakan teknik transformasi fitur, dan model akan dilatih untuk mengenali pola-pola ini dengan tujuan untuk memprediksi apakah suatu email termasuk dalam kategori spam atau bukan. Dengan menggunakan machine learning, solusi ini menawarkan pendekatan otomatis yang lebih efisien dan akurat dibandingkan dengan metode manual untuk menangani email spam.|
| Metode pengolahan       | Metode pengolahan data yang digunakan dalam proyek ini mencakup beberapa langkah penting untuk mempersiapkan dan memproses data sebelum digunakan dalam pelatihan model. **`Pertama`**, data email yang diterima akan diproses dengan **`teknik text vectorization`** , menggunakan TextVectorization dari TensorFlow. Teknik ini akan mengubah teks email menjadi representasi numerik berupa urutan angka yang mewakili kata-kata dalam email. Kemudian, **`TensorFlow Transform (TFT)`** digunakan untuk mentransformasikan fitur secara konsisten, yang memastikan bahwa data yang digunakan dalam pelatihan dan pengujian model memiliki kualitas dan struktur yang seragam. Setelah data diproses, model neural network dibangun dengan menggunakan arsitektur **`LSTM (Long Short-Term Memory)`** yang bertujuan untuk menangkap dependensi jangka panjang dalam teks email. Selain itu, Dense layers digunakan untuk menangkap hubungan non-linear yang ada dalam data. Model ini dilatih menggunakan **`binary crossentropy`** sebagai **`fungsi loss`** dan **`binary accuracy`** untuk evaluasi performa model. Selain itu, dilakukan juga **`hyperparameter tuning`** menggunakan **`Keras Tuner`** untuk mengoptimalkan kombinasi hyperparameter terbaik, seperti jumlah unit **`LSTM, dimensi embedding, learning rate, dan lainnya`**, dengan tujuan untuk meningkatkan performa model dalam klasifikasi spam. Dengan seluruh proses pengolahan data ini, diharapkan model dapat mengklasifikasikan email dengan akurat dan efisien.|
| Arsitektur model        | Arsitektur model yang digunakan dalam proyek ini adalah model klasifikasi berbasis teks menggunakan **`Bidirectional LSTM`**. Model dimulai dengan Input Layer yang menerima input berupa teks email yang terdiri dari satu kata **`(shape=(None, 1))`** dengan tipe data string. Selanjutnya, teks tersebut diproses menggunakan **`Text Vectorization Layer`**, yang mengonversi teks mentah menjadi urutan token numerik dengan panjang maksimal 100 kata **`(sequence_length=100)`** dan membatasi jumlah kata unik yang digunakan menjadi 10.000 (vocab_size=10000). Hasil dari proses ini kemudian diteruskan ke Embedding Layer, yang mengonversi token-token tersebut menjadi representasi dense berdimensi 16 **`(embedding_dim=16)`**, dimana setiap kata diwakili oleh vektor berdimensi 16. Setelah itu, output dari embedding dimasukkan ke dalam **`Bidirectional LSTM Layer dengan 32 unit`**, yang memungkinkan model untuk memproses informasi dari kedua arah (dari kiri ke kanan dan sebaliknya) untuk menangkap konteks yang lebih baik. Output dari LSTM selanjutnya diteruskan ke dua buah Dense Layer berturut-turut. **`Layer pertama`** memiliki **`64 unit`** dengan fungsi **`aktivasi ReLU`**, dan **`layer kedua`** memiliki **`32 unit`** dengan fungsi aktivasi yang sama. Kedua layer dense ini berfungsi untuk mengekstrak fitur-fitur kompleks yang relevan untuk tugas klasifikasi. Untuk mengurangi kemungkinan **`overfitting`**, **`Dropout Layer`** diterapkan dengan **`rate 0,1`**, yang secara acak menonaktifkan 10% neuron selama pelatihan. Terakhir, model diakhiri dengan **`Output Layer`** berupa **`layer Dense`** dengan **`1 unit dan fungsi aktivasi sigmoid`**, yang menghasilkan probabilitas antara 0 dan 1 untuk menentukan apakah email tersebut termasuk kategori **`spam (nilai mendekati 1)`** atau **`tidak spam (nilai mendekati 0)`**. Model ini dilatih menggunakan **`binary cross-entropy`** sebagai **`fungsi loss`** dan **`Adam optimizer`** dengan **`learning rate=0.001`**.|
| Metrik evaluasi         | Metrik evaluasi yang digunakan untuk mengevaluasi performa model ini adalah **`Binary Accuracy`**. Metrik ini digunakan karena model ini dirancang untuk masalah **`klasifikasi biner`**, yaitu untuk memprediksi apakah suatu email merupakan **`spam (label = 1)`** atau **`tidak spam (label = 0)`**. Binary Accuracy mengukur persentase prediksi yang benar dibandingkan dengan total jumlah prediksi. Dengan kata lain, ini menunjukkan berapa banyak email yang diprediksi dengan benar sebagai spam atau non-spam dibandingkan dengan seluruh dataset. Selain itu, pada proses pelatihan, model ini juga menggunakan Loss Function berupa Binary Crossentropy, yang menghitung seberapa besar perbedaan antara hasil prediksi probabilitas model dan label yang sebenarnya. Binary Crossentropy cocok untuk klasifikasi biner karena menghitung kerugian berdasarkan probabilitas prediksi yang diperoleh model dibandingkan dengan nilai sebenarnya (0 atau 1). Dalam konteks validasi dan pelatihan model, **`EarlyStopping`** diterapkan pada metrik **`val_binary_accuracy`** untuk menghentikan pelatihan lebih awal jika akurasi validasi tidak meningkat, sehingga mencegah model **`overfitting`** pada data pelatihan. Dengan mengandalkan **`binary accuracy`** dan **`binary crossentropy`**, model ini dapat dinilai seberapa baik dalam memprediksi dengan benar apakah suatu email adalah spam atau bukan, serta berfokus pada pengurangan kesalahan dalam pengklasifikasian spam.|
| Performa model          | Model yang dibangun menunjukkan performa yang sangat baik dengan berbagai metrik evaluasi yang mendalam. Berikut adalah beberapa hasil performa model: **`AUC`**: **`Area Under the Curve (AUC)`** model mencapai **`0.972`**, yang menandakan bahwa model memiliki kemampuan yang sangat baik dalam membedakan antara email `spam` dan `non-spam`.**`Binary Accuracy`**: Akurasi model dalam mengklasifikasikan email **`spam`** atau **`tidak spam`** adalah **`97.3%`**, menunjukkan bahwa model mampu memprediksi dengan sangat tepat. **`False Negatives`**: Model memiliki **`11 false negatives`**, yang berarti ada 11 email yang sebenarnya adalah spam namun diklasifikasikan sebagai **`bukan spam`**. **`False Positives`**: Model memiliki **`18 false positives`**, yang berarti ada 18 email yang sebenarnya **`bukan spam`** namun diklasifikasikan sebagai **`spam`**. **`True Negatives`**: 930 email non-spam berhasil diklasifikasikan dengan benar sebagai **`bukan spam`**. **`True Positives`**: Model berhasil mengidentifikasi 122 email spam dengan benar. **`Loss`**: Model memiliki loss sebesar **`0.117`**, yang menunjukkan bahwa model memiliki kesalahan prediksi yang relatif rendah selama proses pelatihan.|

## **Testing Prediction**

### With Deployment Model

```python
def predict_spam(email_message):
    url = "http://localhost:8080/v1/models/email-spam-detection-model:predict"
    data_to_predict = {
        "instances": [
            {
                "message_xf": email_message  # Mengirimkan pesan dengan nama input yang sesuai
            }
        ]
    }

    response = requests.post(url, data=json.dumps(data_to_predict), headers={"content-type": "application/json"})

    if response.status_code == 200:
        prediction = response.json()
        spam_probability = prediction['predictions'][0][0]  # Ambil nilai dari list yang dikembalikan model

        # Tentukan apakah spam atau tidak berdasarkan probabilitas
        if spam_probability > 0.5:
            return "Spam 🤡"
        else:
            return "Not Spam 🤠"
    else:
        return f"Error dalam request: {response.status_code}\n{response.text}"
```

### Membuat Menu Pilihan
Metode ini akan menggunakan email dari dataset yang tersedia (misalnya **email_spam.csv**). Program akan memilih salah satu email dan memprediksi apakah itu spam atau tidak dan juga bisa ketika ingin memasukkan email secara inputan untuk diprediksi, gunakan metode berikut. Cukup masukkan pesan email dan model akan mengklasifikasikan apakah itu spam atau bukan.

```python
def predict_from_dataset():
    df = pd.read_csv("data/email_spam.csv", encoding='latin-1')

    # Ambil pesan pertama sebagai contoh untuk diuji
    sample_email = df['message'][9]

    print("Pesan yang akan diprediksi dari dataset:")
    print(sample_email)
    print()

    result = predict_spam(sample_email)
    print("Hasil Prediksi:", result)

def predict_from_input():
    user_email = input("Masukkan pesan email untuk diprediksi: ")

    print("Pesan yang akan diprediksi:")
    print(user_email)
    print()

    result = predict_spam(user_email)
    print("Hasil Prediksi:", result)

print("Pilih metode prediksi:")
print("1. Prediksi dari dataset")
print("2. Prediksi dengan input manual")
print("-------------------------------------")

choice = input("Masukkan pilihan (1 atau 2): ")

if choice == "1":
    predict_from_dataset()
elif choice == "2":
    predict_from_input()
else:
    print("Pilihan tidak valid")

```
