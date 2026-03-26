#  Credit Card Fraud Detection System

##  Project Overview
This project aims to detect fraudulent credit card transactions using machine learning techniques. It includes data generation, analysis, model building, and deployment.

---

##  Features
- Synthetic dataset creation with realistic fraud patterns
- Exploratory Data Analysis (EDA)
- Handling class imbalance using SMOTE
- Machine Learning model using Random Forest
- Model evaluation (Confusion Matrix, Classification Report)
- Interactive web app using Streamlit
- Data visualization using Tableau

---

##  Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- Imbalanced-learn (SMOTE)
- Streamlit
- Tableau
- Git & GitHub

---

##  Dataset
- Custom-generated dataset (`fraud_dataset.csv`)
- Includes features like:
  - Amount
  - Time
  - is_international
  - card_present
  - Class (Target: 0 = Normal, 1 = Fraud)

---

##  Model
- Algorithm: Random Forest Classifier
- Handled imbalanced data using SMOTE
- Evaluated using:
  - Confusion Matrix
  - Precision, Recall, F1-score

---

##  Tableau Dashboard
- Fraud vs Normal Transactions
- Amount vs Fraud Analysis
- International vs Fraud Patterns
- Time-based Fraud Trends

---

##  Streamlit App
Run the app locally:

```bash
streamlit run app.py
