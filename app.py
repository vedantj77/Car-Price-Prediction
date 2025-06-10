import streamlit as st
import joblib
import numpy as np

# Load scaler and model (optimized: load once)
scalar = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Page config
st.set_page_config(
    page_title="🚗 Car Price Estimator",
    page_icon="🚗",
    layout="wide"
)

# CSS styling → only style button and profile card (safe)
st.markdown("""
    <style>
    .stButton button {
        background-color: #1f77b4;
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 12px 24px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #135a96;
    }
    .profile-card {
        background-color: rgba(240, 240, 240, 0.05);
        border: 1px solid #ccc;
        border-radius: 12px;
        padding: 16px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar - About + Inputs
with st.sidebar:
    st.title("🚗 Car Price Estimator")
    st.caption("Estimate car prices using ML model")
    st.divider()

    # About section
    with st.expander("ℹ️ About this app", expanded=True):
        st.write("""
            This app estimates a suitable **car price** for a customer based on:
            - Age
            - Salary
            - Net worth
            using a trained Machine Learning model.
        """)

    # Inputs
    st.subheader("🔢 Enter Customer Details")
    age = st.number_input("👤 Age", min_value=18, max_value=90, value=40, step=1)
    salary = st.number_input("💰 Salary (₹)", min_value=1000, max_value=99999999, value=30000, step=5000)
    networth = st.number_input("🏦 Net Worth (₹)", min_value=0, max_value=99999999, value=100000, step=20000)

    # Calculate button
    calculatebutton = st.button("🚀 Calculate Car Price")

# Main page content
st.title("📈 Estimated Car Price")
st.divider()

if calculatebutton:
    try:
        # Optimized + safe prediction
        input_data = np.array([[age, salary, networth]])
        estimated_price = float(model.predict(scalar.transform(input_data))[0])  # SAFE conversion to float!

        # Show result
        st.success(f"🎉 Estimated Car Price: ₹{estimated_price:,.2f}")
        st.balloons()

        # Customer Profile Summary
        st.markdown("""
            <div class="profile-card">
            <h4>📝 Customer Profile Summary</h4>
            <ul>
                <li>👤 Age: <strong>{}</strong></li>
                <li>💰 Salary: <strong>₹{:,.0f}</strong></li>
                <li>🏦 Net Worth: <strong>₹{:,.0f}</strong></li>
            </ul>
            </div>
        """.format(age, salary, networth), unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error during prediction: {e}")

else:
    st.info("👈 Please enter customer details in the sidebar and click 'Calculate' to estimate the car price.")
