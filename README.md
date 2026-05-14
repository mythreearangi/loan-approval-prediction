# 🏦 Loan Approval Prediction

A Machine Learning web application that predicts whether a loan application will be **Approved ✅** or **Rejected ❌** based on applicant details such as income, education, employment status, and credit history.

---

## 🚀 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn

---

# 📂 Project Structure

```bash
Loan_Approval_Prediction/
│
├── app.py
├── loan_model.pkl
├── requirements.txt
├── train_model.py
├── loan_data.csv
├── README.md
│
├── notebooks/
│   └── EDA.ipynb
│
└── images/
    └── screenshot.png
```

---

# 📊 Project Overview

This project follows the complete Machine Learning workflow:

1. Data Cleaning & Preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Web App Deployment using Streamlit

---

# 📋 Dataset Features

| Feature | Description |
|----------|-------------|
| Gender | Male/Female |
| Married | Marital Status |
| Dependents | Number of Dependents |
| Education | Graduate/Not Graduate |
| Self_Employed | Employment Status |
| ApplicantIncome | Applicant Income |
| CoapplicantIncome | Co-applicant Income |
| LoanAmount | Loan Amount |
| Loan_Amount_Term | Loan Term |
| Credit_History | Credit History |
| Property_Area | Urban/Semiurban/Rural |
| Loan_Status | Approved/Rejected |

---

# 🤖 Machine Learning Models Used

- Logistic Regression
- Decision Tree Classifier

---

# 📈 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 80%+ |
| Decision Tree | 75%+ |

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Praneeth-376/Loan_Approval_Prediction.git
```

---

## 2️⃣ Navigate to Project Folder

```bash
cd Loan_Approval_Prediction
```

---

## 3️⃣ Create Virtual Environment (Optional)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Run the Streamlit App

```bash
streamlit run app.py
```

---

# 🌐 Live Demo

👉 https://loanapprovalprediction-unthbgemaw2fdwdpnlt6df.streamlit.app/

---

# 📦 requirements.txt

```txt
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

# 🔮 Future Enhancements

- Add Random Forest Model
- Add XGBoost
- Improve UI Design
- Add Authentication System
- Deploy using Docker

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request
