# Laporan Proyek Machine Learning - Shendi Teuku Maulana Efendi

## Domain Proyek
Dalam beberapa tahun terakhir, penerapan machine learning dalam berbagai industri telah meningkat secara signifikan, termasuk dalam industri real estate. Proyek prediksi harga properti menjadi salah satu fokus utama karena pentingnya estimasi harga yang akurat bagi pelaku pasar seperti pembeli, penjual, investor, hingga pengembang properti. Kondisi pasar yang sangat fluktuatif dan dipengaruhi oleh berbagai faktor internal serta eksternal membutuhkan pendekatan yang lebih canggih daripada metode konvensional, dan machine learning menawarkan solusi tersebut dengan kemampuannya mengolah data dalam jumlah besar dan memodelkan hubungan yang kompleks.

Dalam konteks proyek ini, saya menggunakan beberapa algoritma machine learning seperti Ridge Regression, Lasso Regression, ElasticNet, dan Support Vector Regression (SVR) untuk melakukan prediksi harga rumah. Berbagai model ini digunakan karena mereka mampu menangani masalah overfitting dan multikolinearitas, yang sering muncul dalam data prediksi properti. Misalnya, Ridge Regression menambahkan regularisasi untuk mengurangi varians model, sedangkan Lasso dapat membantu dalam melakukan feature selection dengan mendorong beberapa koefisien fitur menuju nol.

Dataset yang digunakan mengandung berbagai variabel atau fitur yang mencakup spesifikasi properti seperti luas tanah, jumlah kamar, lokasi, serta faktor eksternal seperti kondisi ekonomi dan infrastruktur sekitar. Pemanfaatan machine learning di sini memungkinkan untuk menangkap interaksi antara berbagai fitur ini dan menghasilkan prediksi yang lebih akurat dibandingkan metode regresi tradisional.
  
## Business Understanding
### Problem Statements
Pasar properti bersifat sangat dinamis dan dipengaruhi oleh banyak faktor yang kompleks, termasuk faktor ekonomi, lokasi geografis, hingga karakteristik fisik dari properti itu sendiri. Dalam kondisi seperti ini, memprediksi harga rumah dengan tepat menjadi tantangan yang sulit. Oleh karena itu, muncul beberapa pernyataan masalah utama:

1. Bagaimana memprediksi harga rumah secara akurat dengan mempertimbangkan berbagai faktor kompleks?
Di tengah beragam faktor seperti lokasi, luas tanah, jumlah kamar, dan kondisi ekonomi, prediksi harga yang akurat menjadi semakin rumit. Metode tradisional sering kali gagal dalam menangkap interaksi non-linier antar fitur-fitur ini.

2. Bagaimana mengatasi overfitting pada model prediksi harga properti?
Banyak model prediksi harga properti mengalami overfitting, terutama ketika jumlah fitur yang digunakan banyak. Overfitting dapat menyebabkan prediksi yang sangat tepat pada data latih, namun sangat buruk ketika dihadapkan pada data baru.

3. Bagaimana memilih fitur yang paling relevan dalam mempengaruhi harga rumah?
Salah satu tantangan terbesar dalam machine learning adalah memilih fitur yang benar-benar berpengaruh secara signifikan pada hasil prediksi. Tidak semua fitur dalam dataset akan memiliki dampak yang sama pada harga properti.

### Goals
Dari pernyataan masalah tersebut, tujuan proyek ini dapat dirumuskan sebagai berikut:

1. Membangun model machine learning yang mampu memprediksi harga rumah secara akurat
Jawaban untuk masalah pertama adalah dengan menggunakan beberapa algoritma machine learning seperti Ridge Regression, Lasso Regression, ElasticNet, dan Support Vector Regression (SVR) untuk menangkap hubungan kompleks antar variabel dan menghasilkan prediksi yang lebih baik dibandingkan metode regresi linier sederhana.

2. Mengurangi risiko overfitting dan meningkatkan generalisasi model
Untuk menangani overfitting, model akan dilatih menggunakan teknik regularisasi seperti yang diterapkan pada Ridge dan Lasso Regression, serta dengan menggunakan cross-validation untuk menguji performa model pada data yang belum pernah dilihat sebelumnya.

3.Melakukan feature selection untuk meningkatkan interpretabilitas model
Dengan menggunakan teknik Lasso Regression, fitur-fitur yang tidak terlalu signifikan dapat dihilangkan karena Lasso mendorong koefisien dari fitur-fitur tersebut menjadi nol. Ini akan membantu kita fokus pada variabel-variabel yang paling berpengaruh.

### Solution Statements
Untuk mencapai tujuan tersebut, saya mengajukan dua pendekatan solusi dengan mengandalkan model machine learning yang berbeda:

1. Menggunakan beberapa algoritma regresi (Ridge, Lasso, ElasticNet, SVR)
Setiap algoritma akan digunakan untuk memodelkan data yang sama, namun dengan pendekatan yang berbeda. Ridge Regression menambahkan regularisasi yang kuat untuk mengurangi varians model, Lasso Regression akan melakukan feature selection, sementara ElasticNet menggabungkan kedua pendekatan ini. SVR digunakan untuk mengatasi masalah data dengan noise yang tinggi atau hubungan non-linear.

2. Hyperparameter tuning untuk meningkatkan performa model
Untuk mengoptimalkan hasil, setiap model akan menjalani hyperparameter tuning menggunakan teknik GridSearchCV yang akan mencari kombinasi parameter terbaik berdasarkan performa metrik evaluasi seperti Mean Squared Error (MSE) dan Root Mean Squared Error (RMSE).

3. Solusi yang Terukur
Solusi yang diusulkan akan dievaluasi dengan menggunakan beberapa metrik evaluasi seperti RMSE dan MSE. Model dengan nilai RMSE terendah dianggap sebagai model terbaik karena menunjukkan bahwa model tersebut memiliki kesalahan prediksi yang lebih kecil.

## Data Understanding
Pada proyek ini, dataset yang digunakan adalah House Prices - Advanced Regression Techniques Dataset, yang merupakan dataset yang digunakan pada kompetisi di kaggle dalam pemodelan harga rumah. Dataset ini berisi berbagai informasi detail tentang properti yang dapat mempengaruhi harga jual rumah. Dataset ini tersedia secara publik dan dapat diunduh dari Kaggle [House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data.)

## Informasi Dataset
| No  | Column         | Non-Null Count | Dtype   | Description                                                |
|-----|----------------|----------------|---------|------------------------------------------------------------|
| 1   | Id             | 1460           | int64   | Unique identifier for each property.                       |
| 2   | MSSubClass     | 1460           | int64   | The building class.                                       |
| 3   | MSZoning       | 1460           | object  | Identifies the general zoning classification.              |
| 4   | LotFrontage    | 1201           | float64 | Linear feet of street connected to property.               |
| 5   | LotArea        | 1460           | int64   | Lot size in square feet.                                   |
| 6   | Street         | 1460           | object  | Type of road access to the property.                       |
| 7   | Alley          | 91             | object  | Type of alley access to the property.                      |
| 8   | LotShape       | 1460           | object  | General shape of property.                                 |
| 9   | LandContour    | 1460           | object  | Flatness of the property.                                  |
| 10  | Utilities      | 1460           | object  | Type of utilities available.                               |
| 11  | LotConfig      | 1460           | object  | Lot configuration.                                        |
| 12  | LandSlope      | 1460           | object  | Slope of property.                                        |
| 13  | Neighborhood   | 1460           | object  | Neighborhood designation.                                  |
| 14  | Condition1     | 1460           | object  | Proximity to various conditions.                           |
| 15  | Condition2     | 1460           | object  | Proximity to various conditions (if different from Condition1). |
| 16  | BldgType       | 1460           | object  | Type of dwelling.                                         |
| 17  | HouseStyle     | 1460           | object  | Style of dwelling.                                        |
| 18  | OverallQual    | 1460           | int64   | Rates the overall material and finish of the house.       |
| 19  | OverallCond    | 1460           | int64   | Rates the overall condition of the house.                 |
| 20  | YearBuilt      | 1460           | int64   | Original construction date.                                |
| 21  | YearRemodAdd   | 1460           | int64   | Remodel date (same as construction date if no remodeling or additions). |
| 22  | RoofStyle      | 1460           | object  | Type of roof.                                            |
| 23  | RoofMatl       | 1460           | object  | Roof material.                                          |
| 24  | Exterior1st    | 1460           | object  | Exterior covering on the house.                           |
| 25  | Exterior2nd    | 1460           | object  | Exterior covering on the house (if not 1st).             |
| 26  | MasVnrType     | 588            | object  | Masonry veneer type.                                     |
| 27  | MasVnrArea     | 1452           | float64 | Masonry veneer area in square feet.                       |
| 28  | ExterQual      | 1460           | object  | Evaluates the quality of the material on the exterior.    |
| 29  | ExterCond      | 1460           | object  | Evaluates the condition of the material on the exterior.   |
| 30  | Foundation     | 1460           | object  | Type of foundation.                                      |
| 31  | BsmtQual       | 1423           | object  | Evaluates the height of the basement.                     |
| 32  | BsmtCond       | 1423           | object  | Evaluates the general condition of the basement.          |
| 33  | BsmtExposure    | 1422           | object  | Exposure rating of the basement.                          |
| 34  | BsmtFinType1   | 1423           | object  | Rating of basement finished area.                         |
| 35  | BsmtFinSF1     | 1460           | int64   | Type 1 finished square feet.                              |
| 36  | BsmtFinType2   | 1422           | object  | Rating of basement finished area (if multiple types).     |
| 37  | BsmtFinSF2     | 1460           | int64   | Type 2 finished square feet.                              |
| 38  | BsmtUnfSF      | 1460           | int64   | Unfinished square feet of basement.                       |
| 39  | TotalBsmtSF    | 1460           | int64   | Total square feet of basement area.                       |
| 40  | Heating        | 1460           | object  | Type of heating system.                                   |
| 41  | HeatingQC      | 1460           | object  | Heating quality and condition.                             |
| 42  | CentralAir     | 1460           | object  | Central air conditioning.                                  |
| 43  | Electrical     | 1459           | object  | Electrical system.                                        |
| 44  | 1stFlrSF       | 1460           | int64   | First floor square feet.                                  |
| 45  | 2ndFlrSF       | 1460           | int64   | Second floor square feet.                                 |
| 46  | LowQualFinSF   | 1460           | int64   | Low quality finished square feet.                         |
| 47  | GrLivArea      | 1460           | int64   | Above grade living area square feet.                      |
| 48  | BsmtFullBath   | 1460           | int64   | Full bathrooms in basement.                               |
| 49  | BsmtHalfBath   | 1460           | int64   | Half bathrooms in basement.                               |
| 50  | FullBath       | 1460           | int64   | Full bathrooms above grade.                               |
| 51  | HalfBath       | 1460           | int64   | Half bathrooms above grade.                               |
| 52  | BedroomAbvGr   | 1460           | int64   | Bedrooms above grade.                                    |
| 53  | KitchenAbvGr   | 1460           | int64   | Kitchens above grade.                                    |
| 54  | KitchenQual    | 1460           | object  | Kitchen quality.                                         |
| 55  | TotRmsAbvGrd   | 1460           | int64   | Total rooms above grade (does not include bathrooms).    |
| 56  | Functional     | 1460           | object  | Home functionality rating.                                |
| 57  | Fireplaces     | 1460           | int64   | Number of fireplaces.                                     |
| 58  | FireplaceQu    | 770            | object  | Fireplace quality.                                       |
| 59  | GarageType     | 1379           | object  | Garage location.                                         |
| 60  | GarageYrBlt    | 1379           | float64 | Year garage was built.                                   |
| 61  | GarageFinish   | 1379           | object  | Interior finish of the garage.                           |
| 62  | GarageCars     | 1460           | int64   | Size of garage in car capacity.                           |
| 63  | GarageArea     | 1460           | int64   | Garage area in square feet.                               |
| 64  | GarageQual     | 1379           | object  | Garage quality.                                         |
| 65  | GarageCond     | 1379           | object  | Garage condition.                                       |
| 66  | PavedDrive     | 1460           | object  | Paved driveway.                                         |
| 67  | WoodDeckSF     | 1460           | int64   | Wood deck area in square feet.                            |
| 68  | OpenPorchSF    | 1460           | int64   | Open porch area in square feet.                           |
| 69  | EnclosedPorch  | 1460           | int64   | Enclosed porch area in square feet.                       |
| 70  | 3SsnPorch      | 1460           | int64   | Three season porch area in square feet.                  |
| 71  | ScreenPorch    | 1460           | int64   | Screen porch area in square feet.                         |
| 72  | PoolArea       | 1460           | int64   | Pool area in square feet.                                 |
| 73  | PoolQC         | 7              | object  | Pool quality.                                           |
| 74  | Fence          | 281            | object  | Fence quality.                                         |
| 75  | MiscFeature    | 54             | object  | Miscellaneous feature not covered in other categories.   |
| 76  | MiscVal        | 1460           | int64   | $Value of miscellaneous feature.                          |
| 77  | MoSold         | 1460           | int64   | Month Sold (MM).                                        |
| 78  | YrSold         | 1460           | int64   | Year Sold (YYYY).                                       |
| 79  | SaleType       | 1460           | object  | Type of sale.                                           |
| 80  | SaleCondition  | 1460           | object  | Condition of sale.                                      |
| 81  | SalePrice      | 1460           | int64   | Sale price of the house (target variable).                |

### Missing Values pada Dataset
| Fitur         | Total Missing Values | Percentage (%) |
|---------------|----------------------|----------------|
| PoolQC        | 1453                 | 99.52          |
| MiscFeature   | 1406                 | 96.30          |
| Alley         | 1369                 | 93.77          |
| Fence         | 1179                 | 80.75          |
| MasVnrType    | 872                  | 59.73          |
| FireplaceQu   | 690                  | 47.26          |
| LotFrontage   | 259                  | 17.74          |
| GarageYrBlt   | 81                   | 5.55           |
| GarageCond    | 81                   | 5.55           |
| GarageType    | 81                   | 5.55           |
| GarageFinish  | 81                   | 5.55           |
| GarageQual    | 81                   | 5.55           |
| BsmtFinType2  | 38                   | 2.60           |
| BsmtExposure  | 38                   | 2.60           |
| BsmtQual      | 37                   | 2.53           |
| BsmtCond      | 37                   | 2.53           |
| BsmtFinType1  | 37                   | 2.53           |
| MasVnrArea    | 8                    | 0.55           |
| Electrical    | 1                    | 0.07           |

`Ada 19 attributes punya missing values and 5 features (PoolQC, MiscFeature, Alley, Fence, FireplaceQu) punya missing values lebih besar dari 45%`

### Pembagian Feature
`Numerical features`: 1stFlrSF, 2ndFlrSF, 3SsnPorch, BedroomAbvGr, BsmtFinSF1, BsmtFinSF2, BsmtFullBath, BsmtHalfBath, BsmtUnfSF, EnclosedPorch, Fireplaces, FullBath, GarageArea, GarageCars, GarageYrBlt, GrLivArea, HalfBath, KitchenAbvGr, LotArea, LotFrontage, LowQualFinSF, MSSubClass, MasVnrArea, MiscVal, MoSold, OpenPorchSF, OverallCond, OverallQual, PoolArea, ScreenPorch, TotRmsAbvGrd, TotalBsmtSF, WoodDeckSF, YearBuilt, YearRemodAdd, YrSold
```python
numerical = train.select_dtypes(include=['int64','float64']).drop(['SalePrice','Id'],axis=1)
numerical.head()
```
`Categorical features`: Alley, BldgType, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinType2, BsmtQual, CentralAir, Condition1, Condition2, Electrical, ExterCond, ExterQual, Exterior1st, Exterior2nd, Fence, FireplaceQu, Foundation, Functional, GarageCond, GarageFinish, GarageQual, GarageType, Heating, HeatingQC, HouseStyle, KitchenQual, LandContour, LandSlope, LotConfig, LotShape, MSZoning, MasVnrType, MiscFeature, Neighborhood, PavedDrive, PoolQC, RoofMatl, RoofStyle, SaleCondition, SaleType, Street, Utilities,
```python
categorical = train.select_dtypes(exclude=['int64','float64'])
categorical.head()
```
### Exploratory Data Analysis (EDA)
#### Plotting missing values on train and test data 
```python
def showvalues(ax,m=None):
    for p in ax.patches:
        ax.annotate("%.1f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),\
                    ha='center', va='center', fontsize=14, color='k', rotation=0, xytext=(0, 7),\
                    textcoords='offset points',fontweight='light',alpha=0.9)

plt.figure(figsize=(20,20))
plt.subplot(2,1,1)
ax1=sns.barplot(x=missing_train.index,y='Percentage',data=missing_train)
showvalues(ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45, horizontalalignment='right')
ax1.set_title('Missing Values in Train Data')
plt.subplot(2,1,2)
ax2=sns.barplot(x=missing_test.index,y='Percentage',data=missing_test)
showvalues(ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, horizontalalignment='right')
ax2.set_title('Missing Values in Test Data')
plt.show()
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/c0cbdbec0673f34b174f11d4b623e5b94d40d1d2/Submission/Regression%20House%20Proce%20Prediction/Assets/missingvalues.png" width="750">

#### Numerical Predictor Variables dengan Target Variabel Target
```python
train_num = train.select_dtypes(include=['int64','float64'])
fig,axs= plt.subplots(12,3,figsize=(20,80))
#adjust horizontal space between plots
fig.subplots_adjust(hspace=0.6)
for i,ax in zip(train_num.columns,axs.flatten()):
    sns.scatterplot(x=i, y='SalePrice', hue='SalePrice',data=train_num,ax=ax,palette='viridis_r')
    plt.xlabel(i,fontsize=12)
    plt.ylabel('SalePrice',fontsize=12)
    ax.set_title('SalePrice'+' - '+str(i),fontweight='bold',size=20)
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/03ce3dd82770b5c2c106f00cf12fedd2cdf6b8b1/Submission/Regression%20House%20Proce%20Prediction/Assets/numerical%20predictor.png" width="750">

#### Categorical Predictor Variables dengan Target Variabel Target
```python
def facetgrid_boxplot(x, y, **kwargs):
    sns.boxplot(x=x, y=y)
    x=plt.xticks(rotation=90)

f = pd.melt(train, id_vars=['SalePrice'], value_vars=sorted(train[categorical.columns]))
g = sns.FacetGrid(f, col="variable", col_wrap=3, sharex=False, sharey=False, height=5)
g = g.map(facetgrid_boxplot, "value", "SalePrice")
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/7576517887dc3062ce8e3bed5ae7b5f80c4c31d3/Submission/Regression%20House%20Proce%20Prediction/Assets/categorikal%20predictor.png" width="750">

#### Distribution of Target variable (SalePrice)
```python
train['SalePrice'] = np.log1p(train['SalePrice'])
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/7576517887dc3062ce8e3bed5ae7b5f80c4c31d3/Submission/Regression%20House%20Proce%20Prediction/Assets/after%20normal%20distributed.png" width="500">

#### Heatmap Correlation
```python
plt.subplots(figsize = (30,20))
mask = np.zeros_like(train_num.corr(), dtype=bool)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(train_num.corr(), cmap=sns.diverging_palette(20, 220, n=200), mask = mask, annot=True, center = 0)
```
<img src="https://github.com/shendyeff/learn-dicoding/blob/7576517887dc3062ce8e3bed5ae7b5f80c4c31d3/Submission/Regression%20House%20Proce%20Prediction/Assets/heatmapcorr.png" width="">
1. Terdapat korelasi sebesar 0,83 atau 83% antara `GarageYrBlt` dan `YearBuilt`. <br>
2. Korelasi 83% antara `TotRmsAbvGrd` dan `GrLivArea`. <br>
3. Korelasi 89% antara `GarageCars` dan `GarageArea`. <br>
4. Demikian pula banyak fitur lain seperti `BsmtUnfSF`, `FullBath` memiliki korelasi yang baik dengan fitur independen lainnya.



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

**---Ini adalah bagian akhir laporan---**

# Referensi 
1. Aswin Sivam Ravikumar. Real Estate Price Prediction Using Machine Learning. MSc Research Project, Data Analytics, School of Computing, National College of Ireland, Supervisor: Thibaut Lust. [https://norma.ncirl.ie/3096/1/aswinsivamravikumar.pdf](https://norma.ncirl.ie/3096/1/aswinsivamravikumar.pdf)
2. Alistair Adair, Stanley McGreal. The Application of Multiple Regression Analysis in Property Valuation. Journal of Valuation, ISSN: 0263-7480. [https://www.emerald.com/insight/content/doi/10.1108/eb008022/full/html](https://www.emerald.com/insight/content/doi/10.1108/eb008022/full/html)
3. Winky K.O. Ho, Bo-Sin Tang, Siu Wai Wong. Predicting Property Prices with Machine Learning Algorithms. Journal of Property Research, 38:1, 48-70, DOI: 10.1080/09599916.2020.1832558. [https://www.researchgate.net/publication/346308101_Predicting_property_prices_with_machine_learning_algorithms](https://www.researchgate.net/publication/346308101_Predicting_property_prices_with_machine_learning_algorithms)


_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
