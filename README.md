# Employee_Resigned_Prediction_Analysis
# Employee Resignation Prediction (ML + Streamlit)

## Project Overview
This project aims to predict whether an employee will resign or not using machine learning. It helps organizations identify employees who are at risk of leaving and take preventive actions.

---

## Features
- Machine Learning model using XGBoost
- Handled class imbalance using SMOTE
- Interactive web app using Streamlit
- Real-time prediction based on user input

---

## Dataset Features
- Department
- Gender
- Age
- Job Title
- Years at Company
- Education Level
- Performance Score
- Monthly Salary
- Work Hours Per Week
- Projects Handled
- Overtime Hours
- Sick Days
- Remote Work Frequency
- Team Size
- Training Hours
- Promotions
- Employee Satisfaction Score

---

## Tech Stack
- Python
- Scikit-learn
- XGBoost
- Streamlit
- Pandas / NumPy

---

## Model Building Steps
1. Data Cleaning
2. Label Encoding of categorical variables
3. Splitting data into features (X) and target (y)
4. Handling class imbalance using SMOTE
5. Train-Test Split
6. Model training using XGBoost

---

## How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
