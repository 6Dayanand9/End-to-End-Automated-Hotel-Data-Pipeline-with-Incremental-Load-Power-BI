# 🚀 End-to-End Automated Hotel Data Pipeline with Incremental Load & Power BI

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=36BCF7&size=28&center=true&vCenter=true&width=900&lines=Analytical+Engineering+Project;End-to-End+Data+Pipeline;Incremental+Ingestion+and+Loading;Automation+with+Power+Automate;Data+Engineering+Project">
</p>

---

## 📌 Problem Statement

A newly launched **🟢 food delivery app startup in Mumbai** is rapidly growing but facing operational and financial constraints.
Being a startup, the company wants to **minimize infrastructure costs** and avoid investing heavily in cloud platforms, while still building a **scalable and automated data system**.

---

### 🚧 Business Challenges

* 📩 Order data is received via emails from multiple restaurant partners
* 🧾 Manual downloading and handling of files increases time and errors
* 📉 High number of **order cancellations** with no clear reason
* 📊 No proper system to track business performance and KPIs
* 💸 Limited budget → needs a **low-cost optimized solution**

---

### ⚙️ Technical Challenges

* No centralized data storage
* No automation for data ingestion
* Repetitive manual work
* Risk of duplicate data loading
* No structured pipeline for processing

---

### 🎯 Business Requirements

The company needs a solution that can:

* Automate data collection from emails
* Store data without expensive cloud usage
* Process and clean data efficiently
* Load only new data (incremental processing)
* Provide insights into **order cancellations**
* Build dashboards for overall performance monitoring

---

### 💡 Objective

> Build a **low-cost, automated, and scalable data pipeline** that converts raw email data into meaningful business insights and helps identify reasons behind order cancellations.

---

## 🛠️ Tech Stack

<p align="center">

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="50"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="50"/>

<img src="https://img.icons8.com/color/48/microsoft-outlook-2019.png" height="50"/>
<img src="https://img.icons8.com/color/48/power-bi-2021.png" height="48"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Microsoft_Power_Automate.svg" height="50"/>

<img src="https://img.icons8.com/fluency/48/cloud-link.png" height="50"/>

<img src="https://img.icons8.com/color/48/streamlit.png" height="48"/>

</p>

<p align="center">
Python | Pandas | MySQL | GCP | Outlook | Power BI | Power Automate | Gateway | Streamlit
</p>

---

## 🧠 Project Overview

This project provides a **fully automated solution** to solve the above challenges.

👉 Data is collected from emails
👉 Automatically stored in Google Drive
👉 Processed using Python (ETL)
👉 Stored in MySQL
👉 Visualized in Power BI

---

# 🔄 Step 1: Power Automate Workflow (Data Ingestion)

<p align="center">
  <img src="Docs/Power Automate Architecuture.png" width="800"/>
</p>

### 💡 Simple Explanation

* When a new email arrives in Outlook
* Power Automate checks the subject
* If subject contains **`food_data24`**
* It extracts the CSV attachment
* Saves it automatically into Google Drive

---

### 🧠 Logic Behind It

* **Trigger** → Email received
* **Condition** → Subject contains `food_data24`
* **Loop** → Iterate through attachments
* **Action** → Upload file to Google Drive

👉 This removes manual file handling completely

---

# ⚙️ Step 2: ETL Pipeline (Python Processing)

<p align="center">
  <img src="Docs/ETL architecture.png" width="900"/>
</p>

## 📌 What is ETL?

* **Extract** → Collect data
* **Transform** → Clean & prepare data
* **Load** → Store data

---

## 🔹 Extraction

* Connects to Google Drive
* Fetches only new files
* Tracks processed files
* Combines data

---

## 🔹 Cleaning

* Standardizes column names
* Removes duplicates
* Fixes date & time formats
* Filters invalid records
* Creates `date_id`

---

## 🔹 Incremental Loading

* Generates data signature
* Checks for duplicate data
* Loads only new records into MySQL
* Updates tracking file

---

### 🧠 Why this matters

✔ Prevents duplicate data
✔ Improves performance
✔ Saves processing time

---

# 🏗️ Step 3: Complete Architecture (End-to-End Flow)

<p align="center">
  <img src="Docs/Complete Architecture.png" width="1000"/>
</p>

---

## 🔄 Full Flow (Simple)

1. 📩 Email arrives
2. ⚙️ Power Automate processes file
3. ☁️ Google Drive stores raw data
4. 🐍 Python ETL processes data
5. 🗄️ MySQL stores structured data
6. 📊 Power BI generates dashboards
7. 📡 Streamlit monitors pipeline

---

## 📊 Final Summary

👉 Email → Drive → ETL → MySQL → Power BI

✔ Fully automated
✔ Cost-efficient
✔ Incremental processing
✔ Scalable architecture
✔ Data-driven insights

---

## 🎯 Business Impact

* Reduced manual effort
* Lower operational cost
* Faster data processing
* Improved decision-making
* Identified root causes of order cancellations

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
