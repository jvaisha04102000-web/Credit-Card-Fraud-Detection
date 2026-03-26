import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("fraud_model.pkl", "rb"))

st.title("Credit Card Fraud Detection App")
st.write("Enter transaction details:")

amount = st.number_input("Amount")
time = st.number_input("Time (0-23)")
is_international = st.selectbox("Is International?", [0,1])
card_present = st.selectbox("Card Present?", [0,1])

if st.button("predict"):
    input_data = np.array([[amount, time, is_international, card_present]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error(" Fraud Transaction Detected!")
    else:
        st.success("Normal Transaction")