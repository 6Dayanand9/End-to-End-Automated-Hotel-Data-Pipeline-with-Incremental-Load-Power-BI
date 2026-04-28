# 🚀 End-to-End Automated Hotel Data Pipeline with Incremental Load & Power BI

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=36BCF7&size=28&center=true&vCenter=true&width=900&lines=End-to-End+Data+Pipeline;Incremental+Ingestion+and+Loading;Automation+with+Power+Automate;Data+Engineering+Project">
</p>

---

## 🛠️ Tech Stack

<p align="center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="50"/>

<img src="https://img.icons8.com/color/48/microsoft-outlook-2019.png" height="50"/>
<img src="https://img.icons8.com/color/48/power-bi-2021.png" height="48" alt="Power BI"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Microsoft_Power_Automate.svg" height="50"/>

<img src="https://img.icons8.com/fluency/48/cloud-link.png" height="50" alt="Data Gateway"/>

<img src="https://img.icons8.com/color/48/streamlit.png" height="48" alt="Streamlit"/>
</p>

<p align="center">
Python | Pandas | MySQL | GCP | Outlook | Power BI | Power Automate | Gateway | Streamlit
</p>

---

## 🧠 Project Overview

This project is a **fully automated data pipeline**.

👉 Data comes from emails
👉 Gets processed using Python
👉 Stored in MySQL
👉 Visualized in Power BI

Everything works automatically — no manual work needed.

---

# 🔄 Step 1: Power Automate Workflow (Data Ingestion)

<p align="center">
  <img src="Docs/power_automate_flow.png" width="800"/>
</p>

### 💡 Simple Explanation

* When a new email arrives in Outlook
* Power Automate checks the subject
* If subject contains **`food_data24`**
* It takes the CSV file from email
* Saves it automatically into **Google Drive**

---

### 🧠 Logic Behind It

* **Trigger** → Email received
* **Condition** → Subject contains `food_data24`
* **Loop** → Goes through attachments
* **Action** → Upload file to Google Drive

👉 No manual download needed

---

# ⚙️ Step 2: ETL Pipeline (Python Processing)

<p align="center">
  <img src="Docs/ETL architecture.png" width="900"/>
</p>

## 📌 What is ETL?

* **Extract** → Get data
* **Transform** → Clean data
* **Load** → Store data

---

## 🔹 Extraction

* Fetch data from Google Drive
* Skip already processed files
* Combine all files

---

## 🔹 Cleaning

* Fix column names
* Remove duplicates
* Validate data
* Create `date_id`

---

## 🔹 Incremental Loading

* Check if data already exists
* Load only new data
* Skip duplicates

---

### 🧠 Why this matters

✔ Faster processing
✔ No duplicate data
✔ Efficient pipeline

---

# 🏗️ Step 3: Complete Architecture (End-to-End Flow)

<p align="center">
  <img src="Docs/Complete Architecture.png" width="1000"/>
</p>

---

## 🔄 Full Flow (Simple)

1. Email arrives
2. Power Automate saves file
3. Google Drive stores data
4. Python ETL processes data
5. MySQL stores data
6. Power BI shows insights
7. Streamlit monitors pipeline

---

## 📊 Final Summary

👉 Email → Drive → ETL → MySQL → Power BI

✔ Fully automated
✔ Incremental loading
✔ Scalable

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
