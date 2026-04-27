# 📊 PhonePe Transaction Insights Dashboard

## 🚀 Project Overview
This project analyzes digital transaction data from PhonePe to uncover meaningful insights about user behavior, transaction trends, and regional performance across India.

The project follows a complete data pipeline:
- Data Extraction from PhonePe Pulse GitHub repository
- SQL Database creation and querying (SQLite)
- Exploratory Data Analysis (EDA) with visualizations
- Machine Learning model for transaction prediction
- Interactive dashboard using Streamlit

---

## 🧠 Problem Statement
With the rapid growth of digital payments, it is important to understand transaction patterns, user engagement, and regional trends. This project aims to analyze PhonePe transaction data and provide actionable insights for business decision-making.

---

## 🛠️ Tech Stack
- Python
- Pandas
- SQLite (SQL)
- Matplotlib / Seaborn
- Scikit-learn (ML)
- Streamlit

---

## 📂 Project Structure
phonepe_project/
│
├── app.py # Streamlit Dashboard
├── model.pkl # Trained ML Model
├── phonepe.db # SQLite Database
├── requirements.txt # Dependencies
├── notebook.ipynb # Colab / Jupyter Notebook


---

## 📊 Features
- 📈 Top States by Transaction Amount
- 💳 Payment Type Analysis
- 📅 Year-wise Transaction Trends
- 🔍 SQL-based Data Queries
- 🤖 Machine Learning Prediction (Transaction Amount)
- 🎛️ Interactive Streamlit Dashboard with filters

---

## ⚙️ Installation & Setup

### 1. Clone Repository
git clone https://github.com/your-username/phonepe-project.git

cd phonepe-project


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Run Streamlit App

streamlit run app.py


---

## 📊 Dataset
- Source: PhonePe Pulse GitHub Repository  
- Contains structured JSON data for:
  - Aggregated Transactions
  - Map Data
  - Top Performing Regions

---

## 🤖 Machine Learning
- Problem Type: Regression
- Target Variable: Transaction Amount
- Models Used:
  - Linear Regression
  - Decision Tree
  - Random Forest (Best Model)
- Evaluation Metrics:
  - R2 Score
  - Mean Squared Error (MSE)

---

## 📈 Key Insights
- Digital transactions show strong growth over time
- Few states dominate total transaction volume
- Certain payment types are more widely used
- Transaction count and amount are highly correlated

---

## 🔮 Future Improvements
- Add real-time data integration
- Deploy dashboard online (Streamlit Cloud)
- Implement fraud detection models
- Add interactive maps for geographical insights

---

## 👨‍💻 Author
Uzef Zardoz

---

## ⭐ Conclusion
This project demonstrates a complete data analysis pipeline from raw data extraction to interactive visualization and machine learning. It highlights the power of data-driven insights in improving digital payment systems.
