import streamlit as st
import joblib
import numpy as np

# Load scaler and model
scalar = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# App title and description
st.title("Customer Car Price Estimator App")
st.divider()

st.write("""This app estimates an appropriate car price based on customer profile details.""")

# User inputs
age = st.number_input("Enter the age", min_value=18, max_value=90, value=40, step=1)
salary = st.number_input("Enter the salary", min_value=1000, max_value=99999999, value=30000, step=5000)
networth = st.number_input("Enter the net worth", min_value=0, max_value=99999999, step=20000,value = 100000)

# Wrap in a 2D array
x = np.array([[age, salary, networth]])

# Prediction button
calculatebutton = st.button("Calculate")
st.divider()

# Prediction logic
if calculatebutton:
    try:
        x_scaled = scalar.transform(x)
        prediction = model.predict(x_scaled)
        st.success(f"Estimated Car Price: ₹{float(prediction[0]):,.2f}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")
else:
    st.info("Please enter the values and press the Calculate button.")
