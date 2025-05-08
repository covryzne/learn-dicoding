import streamlit as st
import pandas as pd
import pickle

# Load model dan scaler
with open('model/best_model_randomforest.pkl', 'rb') as f_model:
    model = pickle.load(f_model)

with open('model/scaler.pkl', 'rb') as f_scaler:
    scaler = pickle.load(f_scaler)

with open('model/feature_columns.pkl', 'rb') as f_cols:
    feature_columns = pickle.load(f_cols)
    

st.set_page_config(page_title="Dropout Prediction", layout="centered")
st.title("🎓 Student Dropout Prediction")
st.markdown("Isi data mahasiswa di bawah ini untuk memprediksi kemungkinan dropout.")

# Form Input
with st.form("dropout_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        marital_status = st.selectbox("Marital_status", [0, 1])
        application_mode = st.number_input("Application_mode", 0, 20, 1)
        application_order = st.number_input("Application_order", 0, 10, 1)
        attendance = st.selectbox("Daytime_evening_attendance", [0, 1])
        previous_qualification = st.number_input("Previous_qualification", 0, 20, 1)
        previous_grade = st.number_input("Previous_qualification_grade", 0.0, 200.0, 150.0)
        admission_grade = st.number_input("Admission_grade", 0.0, 200.0, 150.0)
        displaced = st.selectbox("Displaced", [0, 1])
        special_needs = st.selectbox("Educational_special_needs", [0, 1])
        debtor = st.selectbox("Debtor", [0, 1])
        tuition_paid = st.selectbox("Tuition_fees_up_to_date", [0, 1])
        gender = st.selectbox("Gender", [0, 1])
        scholarship_holder = st.selectbox("Scholarship_holder", [0, 1])
        age = st.number_input("Age_at_enrollment", 15, 100, 20)

    with col2:
        international = st.selectbox("International", [0, 1])
        sem1_enrolled = st.number_input("Curricular_units_1st_sem_enrolled", 0, 20, 6)
        sem1_evals = st.number_input("Curricular_units_1st_sem_evaluations", 0, 20, 6)
        sem1_approved = st.number_input("Curricular_units_1st_sem_approved", 0, 20, 6)
        sem1_grade = st.number_input("Curricular_units_1st_sem_grade", 0.0, 20.0, 14.0)
        sem1_credited = st.number_input("Curricular_units_1st_sem_credited", 0, 20, 0)
        sem1_wo_eval = st.number_input("Curricular_units_1st_sem_without_evaluations", 0, 10, 0)
        sem2_enrolled = st.number_input("Curricular_units_2nd_sem_enrolled", 0, 20, 6)
        sem2_evals = st.number_input("Curricular_units_2nd_sem_evaluations", 0, 20, 6)
        sem2_approved = st.number_input("Curricular_units_2nd_sem_approved", 0, 20, 6)
        sem2_grade = st.number_input("Curricular_units_2nd_sem_grade", 0.0, 20.0, 14.0)
        sem2_credited = st.number_input("Curricular_units_2nd_sem_credited", 0, 20, 0)
        sem2_wo_eval = st.number_input("Curricular_units_2nd_sem_without_evaluations", 0, 10, 0)

    with col3:
        unemployment = st.number_input("Unemployment_rate", 0.0, 100.0, 6.5)
        inflation = st.number_input("Inflation_rate", -10.0, 100.0, 1.2)
        gdp = st.number_input("GDP", 0.0, 1000.0, 180.0)
        course_group = st.number_input("Course_group", 0, 10, 1)
        is_local = st.selectbox("Is_local", [0, 1])
        mother_edu = st.number_input("Mother_edu_level", 0, 10, 3)
        father_edu = st.number_input("Father_edu_level", 0, 10, 4)
        mother_job = st.number_input("Mother_job", 0, 20, 10)
        father_job = st.number_input("Father_job", 0, 20, 10)
        edu_gap = st.number_input("Parental_education_gap", -10, 10, -1)
        parents_work = st.selectbox("Is_both_parents_employed", [0, 1])

    submitted = st.form_submit_button("Prediksi")

    if submitted:
        input_dict = {
            "Marital_status": marital_status,
            "Application_mode": application_mode,
            "Application_order": application_order,
            "Daytime_evening_attendance": attendance,
            "Previous_qualification": previous_qualification,
            "Previous_qualification_grade": previous_grade,
            "Admission_grade": admission_grade,
            "Displaced": displaced,
            "Educational_special_needs": special_needs,
            "Debtor": debtor,
            "Tuition_fees_up_to_date": tuition_paid,
            "Gender": gender,
            "Scholarship_holder": scholarship_holder,
            "Age_at_enrollment": age,
            "International": international,
            "Curricular_units_1st_sem_enrolled": sem1_enrolled,
            "Curricular_units_1st_sem_evaluations": sem1_evals,
            "Curricular_units_1st_sem_approved": sem1_approved,
            "Curricular_units_1st_sem_grade": sem1_grade,
            "Curricular_units_1st_sem_credited": sem1_credited,
            "Curricular_units_1st_sem_without_evaluations": sem1_wo_eval,
            "Curricular_units_2nd_sem_enrolled": sem2_enrolled,
            "Curricular_units_2nd_sem_evaluations": sem2_evals,
            "Curricular_units_2nd_sem_approved": sem2_approved,
            "Curricular_units_2nd_sem_grade": sem2_grade,
            "Curricular_units_2nd_sem_credited": sem2_credited,
            "Curricular_units_2nd_sem_without_evaluations": sem2_wo_eval,
            "Unemployment_rate": unemployment,
            "Inflation_rate": inflation,
            "GDP": gdp,
            "Course_group": course_group,
            "Is_local": is_local,
            "Mother_edu_level": mother_edu,
            "Father_edu_level": father_edu,
            "Mother_job": mother_job,
            "Father_job": father_job,
            "Parental_education_gap": edu_gap,
            "Is_both_parents_employed": parents_work
        }

        # DataFrame, Reindex, Scaling, dan Prediksi
        input_df = pd.DataFrame([input_dict])
        input_df = input_df.reindex(columns=feature_columns, fill_value=0)
        scaled_input = scaler.transform(input_df)
        pred = model.predict(scaled_input)[0]
        prob = model.predict_proba(scaled_input)[0][1]

        status = "🔴 Dropout" if pred == 1 else "🟢 Tidak Dropout"
        st.success(f"Hasil Prediksi: **{status}**")
        st.metric("Probabilitas Dropout", f"{prob:.2%}")
