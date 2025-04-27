import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import GradientBoostingClassifier

# === Load semua file yang diperlukan ===
with open('best_model_gradboost.pkl', 'rb') as f_model:
    model = pickle.load(f_model)

with open('scaler.pkl', 'rb') as f_scaler:
    scaler = pickle.load(f_scaler)

with open('imputer.pkl', 'rb') as f_imputer:
    imputer = pickle.load(f_imputer)

with open('feature_columns.pkl', 'rb') as f_cols:
    feature_columns = pickle.load(f_cols)

# === Masukkan data baru ===
# Misalnya hanya isi sebagian kolom, sisanya otomatis jadi NaN
data_baru = pd.DataFrame([{
    'Age': 35,
    'DailyRate': 1100,
    'DistanceFromHome': 5,
    'Education': 3,
    'EnvironmentSatisfaction': 2,
    'HourlyRate': 80,
    'JobInvolvement': 3,
    'JobLevel': 2,
    'JobSatisfaction': 4,
    'MonthlyIncome': 5000,
    'MonthlyRate': 20000,
    'NumCompaniesWorked': 2,
    'PercentSalaryHike': 14,
    'PerformanceRating': 3,
    'RelationshipSatisfaction': 2,
    'StockOptionLevel': 1,
    'TotalWorkingYears': 10,
    'TrainingTimesLastYear': 3,
    'WorkLifeBalance': 2,
    'YearsAtCompany': 5,
    'YearsInCurrentRole': 3,
    'YearsSinceLastPromotion': 1,
    'YearsWithCurrManager': 3,
    'BusinessTravel_Travel_Frequently': 0,
    'BusinessTravel_Travel_Rarely': 1,
    'Department_Research & Development': 1,
    'Department_Sales': 0,
    'EducationField_Life Sciences': 1,
    'EducationField_Marketing': 0,
    'EducationField_Medical': 0,
    'EducationField_Other': 0,
    'EducationField_Technical Degree': 0,
    'Gender_Male': 1,
    'JobRole_Human Resources': 0,
    'JobRole_Laboratory Technician': 0,
    'JobRole_Manager': 1,
    'JobRole_Manufacturing Director': 0,
    'JobRole_Research Director': 0,
    'JobRole_Research Scientist': 0,
    'JobRole_Sales Executive': 0,
    'JobRole_Sales Representative': 0,
    'MaritalStatus_Married': 0,
    'MaritalStatus_Single': 1,
    'OverTime_Yes': 1,
    'StabilityInRole': 0.6,
    'LoyaltyToManager': 0.6,
    'AvgTrainingPerYear': 0.6,
    'AgeWhenStarted': 25,
    'AvgYearsPerCompany': 5,
    'IncomePerKm': 220,
    'CompanyLoyalty': 0.5,
    'PromotionFrequency': 2.5,
    'AvgMonthlyIncomePerYear': 1000
}])

# Pastikan urutan kolom sama (dan lengkapi kolom yang kosong)
data_baru = data_baru.reindex(columns=feature_columns, fill_value=np.nan)

# Imputasi dan Scaling
data_baru_imputed = pd.DataFrame(imputer.transform(data_baru), columns=feature_columns)
data_baru_scaled = scaler.transform(data_baru_imputed)

# Predict
prediksi = model.predict(data_baru_scaled)
probabilitas = model.predict_proba(data_baru_scaled)[:, 1]

print("Prediksi Attrition:", int(prediksi[0]))
print("Probabilitas Attrition:", round(probabilitas[0], 4))
