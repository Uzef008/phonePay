import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import pickle

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="PhonePe Dashboard", layout="wide")

st.title("📊 PhonePe Transaction Insights Dashboard")

# ---------------------------
# Connect Database
# ---------------------------
conn = sqlite3.connect("phonepe.db")

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

years = pd.read_sql("SELECT DISTINCT year FROM aggregated_transaction", conn)["year"]
selected_year = st.sidebar.selectbox("Select Year", sorted(years))

# ---------------------------
# Top States
# ---------------------------
st.subheader("Top States by Transaction Amount")

query1 = f"""
SELECT state, SUM(transaction_amount) as total
FROM aggregated_transaction
WHERE year = {selected_year}
GROUP BY state
ORDER BY total DESC
LIMIT 10;
"""

df1 = pd.read_sql(query1, conn)

fig1, ax1 = plt.subplots()
ax1.bar(df1["state"], df1["total"])
plt.xticks(rotation=45)
st.pyplot(fig1)

# ---------------------------
# Payment Type
# ---------------------------
st.subheader("Transaction by Payment Type")

query2 = f"""
SELECT transaction_type, SUM(transaction_amount) as total
FROM aggregated_transaction
WHERE year = {selected_year}
GROUP BY transaction_type
ORDER BY total DESC;
"""

df2 = pd.read_sql(query2, conn)

fig2, ax2 = plt.subplots()
ax2.bar(df2["transaction_type"], df2["total"])
plt.xticks(rotation=45)
st.pyplot(fig2)

# ---------------------------
# Year Trend
# ---------------------------
st.subheader("Year-wise Trend")

query3 = """
SELECT year, SUM(transaction_amount) as total
FROM aggregated_transaction
GROUP BY year
ORDER BY year;
"""

df3 = pd.read_sql(query3, conn)

fig3, ax3 = plt.subplots()
ax3.plot(df3["year"], df3["total"], marker='o')
st.pyplot(fig3)

# ---------------------------
# ML Prediction Section
# ---------------------------
st.subheader("🔮 Predict Transaction Amount")

try:
    model = pickle.load(open("model.pkl", "rb"))

    input_year = st.number_input("Year", min_value=2018, max_value=2025, value=2022)
    input_quarter = st.selectbox("Quarter", [1, 2, 3, 4])
    input_count = st.number_input("Transaction Count", value=1000)

    if st.button("Predict"):
        # Dummy input (structure must match training)
        sample = [[input_year, input_quarter, input_count] + [0]*(len(model.feature_importances_)-3)]
        prediction = model.predict(sample)

        st.success(f"Predicted Transaction Amount: ₹ {prediction[0]:,.2f}")

except:
    st.warning("Model file not found. Run ML notebook first.")

# ---------------------------
# Footer
# ---------------------------
st.write("✅ Built using Streamlit | Uzef Project")