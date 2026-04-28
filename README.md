# 🚀 End-to-End Automated Hotel Data Pipeline with Incremental Load & Power BI

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=36BCF7&size=28&center=true&vCenter=true&width=900&lines=End-to-End+Data+Pipeline;Incremental+Ingestion+and+Loading;Automation+with+Power+Automate;Data+Engineering+Project" alt="Typing SVG">
</p>

---

## 🧠 Project Overview

This project demonstrates a fully automated **end-to-end data engineering pipeline** that ingests hotel data from emails, processes it using Python, and delivers actionable **business insights through interactive Power BI dashboards**.

The pipeline uses **incremental ingestion and incremental loading**, ensuring scalability, efficiency, and reduced redundant processing.

---

## ⚡ End-to-End Architecture

```mermaid
flowchart LR

A[Outlook Email] --> B[Power Automate]
B --> C[Google Drive Landing Zone]

C --> D[Python ETL Script]
D --> D1[processed_files.json]

D --> E[Data Cleaning and Transformation]
E --> F[Clean Data]

F --> G[Incremental Load Script]
G --> G1[loaded_files.json]
G --> H[MySQL Database]

H --> I[Star Schema Model]
I --> I1[Fact Table]
I --> I2[Dimension Tables]

H --> J[Power BI Desktop]
J --> K[Dashboard]

K --> L[Power BI Service]
L --> M[On Premise Gateway]
M --> H

D --> N[Logging System]
E --> N
G --> N

O[Streamlit Monitoring App] --> D
O --> E
O --> G
```

---

## 🏗️ Architecture Layers Explained

### 1️⃣ Data Source Layer

* Outlook emails from hotel managers
* Rule-based filtering for relevant files

### 2️⃣ Automation Layer

* Power Automate for email processing
* Automatic file transfer to cloud storage

### 3️⃣ Storage Layer

* Google Drive as landing zone
* Centralized raw data repository

### 4️⃣ Processing Layer

* Python ETL pipeline
* Data cleaning, validation, transformation

### 5️⃣ Incremental Logic Layer

* Tracks processed files using JSON
* Prevents duplicate ingestion
* Loads only new or updated records

### 6️⃣ Data Warehouse Layer

* MySQL database
* Star schema (Fact + Dimension tables)

### 7️⃣ Visualization Layer

* Power BI dashboards
* KPI tracking and trend analysis

### 8️⃣ Security Layer

* Row-Level Security (RLS)
* Controlled data access

---

## 🛠️ Tech Stack

<p align="center">

<!-- Core Stack -->

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="50" alt="Python"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="50" alt="Pandas"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" height="50" alt="MySQL"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg" height="50" alt="GCP"/>

<!-- Microsoft Stack -->

<img src="https://img.icons8.com/color/48/microsoft-outlook-2019.png" height="50" alt="Outlook"/>
<img src="https://img.icons8.com/color/48/power-bi.png" height="50" alt="Power BI"/>
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Microsoft_Power_Automate.svg" height="50" alt="Power Automate"/>

<!-- Gateway (using generic network/server icon for clarity) -->

<img src="https://img.icons8.com/color/48/server.png" height="50" alt="On-Prem Gateway"/>

<!-- Other Tools -->

<img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/streamlit.svg" height="50" style="background-color:white; padding:6px; border-radius:8px;" alt="Streamlit"/>

<img src="https://img.icons8.com/ios-filled/50/ffffff/github.png" height="50" style="background-color:black; padding:6px; border-radius:50%;" alt="GitHub"/>

</p>

<p align="center">
Python | Pandas | MySQL | GCP | Outlook | Power BI | Power Automate | On-Prem Gateway | Streamlit | GitHub
</p>



---

## 📈 Pipeline Highlights

* Fully automated data pipeline
* Incremental ingestion and loading
* Reduced processing time
* Business-ready insights
* Secure data access
* Monitoring via Streamlit

---

## 🎯 Business Impact

* Eliminated manual data handling
* Improved data accuracy
* Faster reporting
* Scalable architecture

---

## 📂 Project Structure

```text
hotel-data-pipeline/
│
├── data/
├── scripts/
│   ├── etl_pipeline.py
│   ├── incremental_load.py
│
├── sql/
│   ├── create_tables.sql
│   ├── incremental_queries.sql
│
├── powerbi/
│   ├── dashboard.pbix
│
├── docs/
│   ├── architecture.png
│
├── app.py
├── main.py
├── processed_files.json
├── loaded_files.json
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository
2. Configure Google Drive API credentials (GCP Service Account)
3. Set up MySQL database
4. Run the ETL pipeline script
5. Execute the incremental load script
6. Open the Power BI dashboard

---

## ⭐ Support

If you found this project useful, give it a ⭐ on GitHub!
