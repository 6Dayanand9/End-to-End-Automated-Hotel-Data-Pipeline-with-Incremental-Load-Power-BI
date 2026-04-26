# 🚀 End-to-End Automated Hotel Data Pipeline with Incremental Load & Power BI

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=36BCF7&size=28&center=true&vCenter=true&width=900&lines=End-to-End+Data+Pipeline+⚡;Incremental+Ingestion+%26+Loading+📈;Automation+with+Power+Automate+🤖;Data+Engineering+Project+🚀">
</p>

---

## 🧠 Project Overview

A fully automated **data engineering pipeline** that ingests hotel data from emails, processes it using Python, and delivers insights through Power BI with **incremental ingestion and incremental loading**.

---

## ⚡ Detailed Architecture (Incremental Pipeline)

## ⚡ End-to-End Architecture (Incremental Pipeline)

<p align="center">
  <a href="mermaid-diagram.png">
    <img src="mermaid-diagram.png" width="900">
  </a>
</p>

<p align="center">
  <em>Automated Data Flow with Incremental Ingestion & Incremental Load</em>
</p>


flowchart LR

    %% ---------------------------
    %% SOURCE LAYER
    %% ---------------------------
    A[Outlook Email] 
    A -->|CSV Attachment| B[Power Automate]

    %% ---------------------------
    %% INGESTION LAYER
    %% ---------------------------
    B -->|Auto Save Files| C[Google Drive - Landing Zone]

    %% ---------------------------
    %% DATA EXTRACTION
    %% ---------------------------
    C -->|API Fetch| D[Python Extraction Script]
    D -->|File Tracking| D1[processed_files.json]

    %% ---------------------------
    %% TRANSFORMATION LAYER
    %% ---------------------------
    D --> E[Data Cleaning and Transformation]
    E -->|Cleaned Data| F[Clean Data CSV]

    %% ---------------------------
    %% LOADING LAYER
    %% ---------------------------
    F --> G[Incremental Load Script]
    G -->|Duplicate Check| G1[loaded_files.json]
    G --> H[(MySQL Database)]

    %% ---------------------------
    %% DATA MODELING
    %% ---------------------------
    H --> I[Star Schema Model]
    I --> I1[Fact Table: fact_orders]
    I --> I2[Dimension Tables]

    %% ---------------------------
    %% BI LAYER
    %% ---------------------------
    H --> J[Power BI Desktop]
    J -->|Data Modeling and Measures| K[Power BI Dashboard]

    %% ---------------------------
    %% DEPLOYMENT LAYER
    %% ---------------------------
    K --> L[Power BI Service]
    L -->|Gateway Connection| M[On-Premise Gateway]
    M -->|Live Connection| H

    %% ---------------------------
    %% MONITORING
    %% ---------------------------
    D --> N[Logging System]
    E --> N
    G --> N

    %% ---------------------------
    %% UI LAYER
    %% ---------------------------
    O[Streamlit Dashboard]
    O -->|Trigger Pipeline| D
    O --> E
    O --> G


## 🔥 Incremental Logic (Core Highlight)

### 🧩 Incremental Ingestion

```python
# Check if file already processed
if file_id not in processed_files:
    process_file()
    processed_files.add(file_id)
else:
    skip_file()
```

### 🧩 Incremental Load

```python
# Load only new or updated records
if record_date > last_loaded_date:
    insert_into_fact_table()
elif record_exists:
    update_dimension_table()
else:
    skip_duplicate()
```

---

## 🏗️ Architecture Layers Explained

### 1️⃣ Data Source Layer

📩 Outlook Emails

* Managers send data files
* Trigger-based ingestion

---

### 2️⃣ Automation Layer

⚙️ Power Automate

* Filters emails using rules
* Moves attachments to Google Drive

---

### 3️⃣ Storage Layer

☁️ Google Drive (Landing Zone)

* Stores incoming raw files
* Acts as staging entry point

---

### 4️⃣ Processing Layer

🐍 Python (ETL)

* Fetches files using Drive API
* Performs:

  * Data cleaning
  * Schema validation
  * Transformation

---

### 5️⃣ Incremental Logic Layer

🧠 Core Intelligence

✔ Track processed files (JSON / metadata)
✔ Avoid duplicate ingestion
✔ Load only delta data
✔ Maintain history

---

### 6️⃣ Data Warehouse Layer

🗄️ MySQL

* Star Schema:

  * Fact Table → transactions
  * Dimension Tables → hotel, location, etc.
* Optimized for analytics

---

### 7️⃣ Visualization Layer

📊 Power BI

* Interactive dashboards
* KPI tracking
* Trend analysis

---

### 8️⃣ Security Layer

🔐 Row-Level Security (RLS)

* Restricts data access
* Role-based filtering

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,mysql,gcp,github" />
</p>

Python | Pandas | MySQL | Power BI | Power Automate | GCP

---

## 📈 Pipeline Highlights

🚀 Fully Automated Workflow
⚡ Incremental Ingestion + Load
📉 Reduced Processing Time
📊 Business-Ready Insights
🔐 Secure Data Access

---

## 🎯 Business Impact

✔ Eliminated manual data handling
✔ Improved data accuracy
✔ Faster reporting cycle
✔ Scalable architecture

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
