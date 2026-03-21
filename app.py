import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("Employee_Resigned.pkl", "rb"))

st.title("Employee Resignation Prediction")

# ----------- INPUTS -----------

# Categorical Encoding Mapping
dept_dict = {'IT':0, 'Finance':1, 'Customer Support':2, 'Engineering':3, 'Marketing':4, 'HR':5, 'Operations':6, 'Sales':7, 'Legal':8}
gender_dict = {'Male':0, 'Female':1, 'Other':2}
job_dict = {'Specialist':0, 'Developer':1, 'Analyst':2, 'Manager':3, 'Technician':4, 'Engineer':5, 'Consultant':6}
edu_dict = {'High School':0, 'Bachelor':1, 'Master':2, 'PhD':3}

# UI Inputs
Department = st.selectbox("Department", list(dept_dict.keys()))
Gender = st.selectbox("Gender", list(gender_dict.keys()))
Age = st.number_input("Age", 18, 65)
Job_Title = st.selectbox("Job Title", list(job_dict.keys()))
Years_At_Company = st.number_input("Years At Company", 0, 10)
Education_Level = st.selectbox("Education Level", list(edu_dict.keys()))
Performance_Score = st.slider("Performance Score", 1, 5)

Monthly_Salary = st.number_input("Monthly Salary")
Work_Hours_Per_Week = st.number_input("Work Hours Per Week")
Projects_Handled = st.number_input("Projects Handled")
Overtime_Hours = st.number_input("Overtime Hours")
Sick_Days = st.number_input("Sick Days")
Remote_Work_Frequency = st.number_input("Remote Work Frequency")
Team_Size = st.number_input("Team Size")
Training_Hours = st.number_input("Training Hours")
Promotions = st.number_input("Promotions")
Employee_Satisfaction_Score = st.slider("Satisfaction Score", 0.0, 5.0)

# ----------- PREDICTION -----------

if st.button("Predict"):

    input_data = np.array([[
        dept_dict[Department],
        gender_dict[Gender],
        Age,
        job_dict[Job_Title],
        Years_At_Company,
        edu_dict[Education_Level],
        Performance_Score,
        Monthly_Salary,
        Work_Hours_Per_Week,
        Projects_Handled,
        Overtime_Hours,
        Sick_Days,
        Remote_Work_Frequency,
        Team_Size,
        Training_Hours,
        Promotions,
        Employee_Satisfaction_Score
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("Employee will Resign")
    else:
        st.success("Employee will NOT Resign")