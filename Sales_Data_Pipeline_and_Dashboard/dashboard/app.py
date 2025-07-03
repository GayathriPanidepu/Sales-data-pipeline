import streamlit as st
import pandas as pd
import sqlite3

st.title("📊 Sales Dashboard")

conn = sqlite3.connect('../db/sales.db')

df = pd.read_sql("SELECT * FROM sales", conn)

st.subheader("1. Monthly Sales Trend")
monthly_sales = pd.read_sql("""
    SELECT strftime('%Y-%m', order_date) as month, SUM(total_price) as total_sales
    FROM sales GROUP BY month
""", conn)
st.line_chart(monthly_sales.set_index('month'))

st.subheader("2. Top 5 Products")
top_products = pd.read_sql("""
    SELECT product, SUM(quantity) as total_sold
    FROM sales GROUP BY product ORDER BY total_sold DESC LIMIT 5
""", conn)
st.bar_chart(top_products.set_index('product'))

st.subheader("3. Repeat Customers")
repeat_customers = pd.read_sql("""
    SELECT customer_id, COUNT(DISTINCT order_id) as orders
    FROM sales GROUP BY customer_id HAVING orders > 1
""", conn)
st.dataframe(repeat_customers)
