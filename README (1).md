# 📊 Sales Data Pipeline and Dashboard

This project demonstrates a simple Data Engineering pipeline using **Python**, **SQL**, and **Streamlit**. It covers the full ETL (Extract, Transform, Load) process using a CSV file, stores the processed data in an SQLite database, and visualizes key sales metrics through an interactive dashboard.

---

## 🚀 Features

- 📥 Extracts sales data from a CSV file
- 🧹 Cleans and transforms data using Pandas
- 🗃 Loads transformed data into a SQLite database
- 🔍 SQL queries for business insights
- 📈 Visual dashboard using Streamlit

---

## 🛠 Tech Stack

- Python 3.x
- Pandas
- SQLite (via sqlite3)
- Streamlit

---

## 📁 Project Structure

```
sales_data_pipeline/
├── data/
│   └── sales.csv
├── db/
│   └── sales.db
├── etl/
│   └── etl_script.py
├── sql/
│   └── queries.sql
├── dashboard/
│   └── app.py
├── requirements.txt
└── README.md
```

---

## 📦 Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/sales_data_pipeline.git
cd sales_data_pipeline
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the ETL script:

```bash
python etl/etl_script.py
```

4. Launch the dashboard:

```bash
streamlit run dashboard/app.py
```

---

## ✅ Output Screens

- Line chart of monthly sales
- Bar chart of top 5 products sold
- Table of repeat customers

---

## 🧠 Concepts Covered

- Building an ETL pipeline with Python
- Data cleaning and transformation using Pandas
- Writing and executing SQL queries
- Dashboarding with Streamlit

---

## 📬 Author

**Your Name** – [Your LinkedIn or GitHub](https://github.com/your-username)

---

## 📄 License

This project is licensed under the MIT License.