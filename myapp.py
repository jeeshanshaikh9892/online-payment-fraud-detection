import streamlit as st
import pickle
import numpy as np

with open("fraud_detection_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💳 Online Payment Fraud Detection")

amount = st.number_input("Transaction Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Sender Old Balance", min_value=0.0)
newbalanceOrig = st.number_input("Sender New Balance", min_value=0.0)
oldbalanceDest = st.number_input("Receiver Old Balance", min_value=0.0)
newbalanceDest = st.number_input("Receiver New Balance", min_value=0.0)

tx_type = st.selectbox(
    "Transaction Type",
    ["CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER", "CASH_IN"]
)

# One-hot encoding
type_cash_out = 1 if tx_type == "CASH_OUT" else 0
type_debit = 1 if tx_type == "DEBIT" else 0
type_payment = 1 if tx_type == "PAYMENT" else 0
type_transfer = 1 if tx_type == "TRANSFER" else 0
type_cash_in = 1 if tx_type == "CASH_IN" else 0

if st.button("Predict"):
    data = np.array([[
        amount,
        oldbalanceOrg,
        newbalanceOrig,
        oldbalanceDest,
        newbalanceDest,
        type_cash_out,
        type_debit,
        type_payment,
        type_transfer,
        type_cash_in
    ]])

    pred = model.predict(data)[0]

    if pred == 1:
        st.error("🚨 Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
