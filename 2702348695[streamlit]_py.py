# -*- coding: utf-8 -*-
"""2702348695[streamlit].py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tBmOlFvMEpSsiLbNBRyLO0-uBQ0dvCMv
"""

import streamlit as st
import joblib
import numpy as np

def load_model(filename):
    model = joblib.load(filename)
    return model

def make_prediction(model, user_input):
    prediction = model.predict([user_input])
    return prediction[0]

def main():
    model_filename = 'xgboost_model.pkl'
    model = load_model(model_filename)

    # Judul Aplikasi Streamlit
    st.title('Loan Status Prediction')

    # Menambahkan input form untuk data pengguna
    person_age = st.number_input('Age', min_value=18, max_value=100, value=30)
    person_gender = st.selectbox('Gender', ['male', 'female'])
    person_education = st.selectbox('Education Level', ['High School', 'Associate', 'Bachelor', 'Master', 'Doctorate'])
    person_income = st.number_input('Income', min_value=0.0, value=50000.0)
    person_emp_exp = st.number_input('Employment Experience (Years)', min_value=0, max_value=50, value=5)
    loan_amnt = st.number_input('Loan Amount', min_value=1000, max_value=1000000, value=10000)
    loan_int_rate = st.number_input('Loan Interest Rate', min_value=0.0, max_value=100.0, value=10.5)
    loan_percent_income = st.number_input('Loan Percent of Income', min_value=0.0, max_value=1.0, value=0.2)
    cb_person_cred_hist_length = st.number_input('Credit History Length (Years)', min_value=0, max_value=100, value=5)
    credit_score = st.number_input('Credit Score', min_value=300, max_value=850, value=700)
    previous_loan_defaults_on_file = st.selectbox('Previous Loan Defaults on File', ['No', 'Yes'])
    loan_intent = st.selectbox('Loan Intent', ['DEBTCONSOLIDATION', 'EDUCATION', 'HOMEIMPROVEMENT', 'MEDICAL', 'PERSONAL', 'VENTURE'])
    home_ownership = st.selectbox('Home Ownership', ['MORTGAGE', 'OTHER', 'OWN', 'RENT'])

    # Mempersiapkan input data sesuai dengan model
    input_data = [
        person_age,
        1 if person_gender == 'male' else 0,  # Gender encoding
        ['High School', 'Associate', 'Bachelor', 'Master', 'Doctorate'].index(person_education),  # Education encoding
        person_income,
        person_emp_exp,
        loan_amnt,
        loan_int_rate,
        loan_percent_income,
        cb_person_cred_hist_length,
        credit_score,
        1 if previous_loan_defaults_on_file == 'Yes' else 0,  # Previous loan defaults encoding
        1 if loan_intent == 'DEBTCONSOLIDATION' else 0,
        1 if loan_intent == 'EDUCATION' else 0,
        1 if loan_intent == 'HOMEIMPROVEMENT' else 0,
        1 if loan_intent == 'MEDICAL' else 0,
        1 if loan_intent == 'PERSONAL' else 0,
        1 if loan_intent == 'VENTURE' else 0,
        1 if home_ownership == 'MORTGAGE' else 0,
        1 if home_ownership == 'OTHER' else 0,
        1 if home_ownership == 'OWN' else 0,
        1 if home_ownership == 'RENT' else 0
    ]

    # Prediksi ketika tombol ditekan
    if st.button('Predict'):
        result = make_prediction(model, input_data)
        st.success(f'The prediction is: {"Approved" if result == 1 else "Not Approved"}')

if __name__ == '__main__':
    main()