# 🚗 Car Price Prediction App

This is a simple and intuitive machine learning web application built using **Streamlit** that predicts how much a person can afford to spend on a car based on their **age**, **salary**, and **net worth**.

🔗 **Live App**: [car-price-prediction.streamlit.app](https://car-price-prediction-ckc2srrn9jexga6gnklgu3.streamlit.app/)

---

## 🧠 Model Overview

- **Model Type**: Linear Regression
- **Inputs**:
  - Age
  - Salary
  - Net Worth
- **Output**: Predicted Car Price
- The model was trained using synthetic or collected data and saved using `pickle`.

---

## 💻 Technologies Used

- Python
- Streamlit (for UI)
- Pandas, NumPy
- Scikit-learn (for Linear Regression)
- Pickle (for model saving/loading)

---

## 🛠️ How to Run This Project Locally

### 1️⃣ Clone the Repository

bash
git clone https://github.com/vedantj77/Car-Price-Prediction.git
cd Car-Price-Prediction

2️⃣ Create a Virtual Environment (Optional but Recommended)
bash
Copy
Edit
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If requirements.txt is missing, use:

bash
Copy
Edit
pip install streamlit scikit-learn pandas numpy

4️⃣ Run the App
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📁 Project Structure
bash
Copy
Edit
Car-Price-Prediction/
│
├── app.py                  # Streamlit app file
├── car_price_model.pkl     # Trained linear regression model
├── requirements.txt        # Required libraries
└── README.md               # Project documentation
📸 App Preview
You can visit the live app to try it out:
👉 Streamlit Live Demo

🙋‍♂️ Author
Vedant Jadhav
GitHub • LinkedIn



---

