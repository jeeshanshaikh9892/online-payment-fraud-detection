# 💳 Online Payment Fraud Detection using Machine Learning

## 📌 Overview
This project detects fraudulent online payment transactions using machine learning.
A Random Forest classifier was trained on historical transaction data and deployed
as an interactive web application using Streamlit.

## 🚀 Features
- Detects fraudulent vs legitimate transactions
- Handles highly imbalanced data
- Uses ROC-AUC, Precision, Recall, and F1-score for evaluation
- Interactive Streamlit web app for live predictions

## 🧠 Machine Learning Models
- Logistic Regression
- Random Forest (Final Model)
- XGBoost

## 📊 Model Performance (Random Forest)
- Precision (Fraud): 0.96
- Recall (Fraud): 0.80
- F1-score: 0.87
- ROC-AUC: ~0.96

## 🛠️ Tech Stack
- Python
- Scikit-learn
- Pandas, NumPy
- Streamlit

## ▶️ How to Run the App
```bash
pip install -r requirements.txt
streamlit run myapp.py
