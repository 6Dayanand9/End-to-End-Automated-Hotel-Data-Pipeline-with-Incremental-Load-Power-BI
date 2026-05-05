# 🚀 End-to-End Automated Hotel Data Pipeline with Incremental Load & Power BI Report On Orders Cancellations, Sales & Cost Analysis And Performance Monitoring

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=2ECC71&size=28&center=true&vCenter=true&width=900&lines=Analytical+Engineering+Project;End-to-End+Data+Pipeline;Incremental+Ingestion+and+Loading;Automation+with+Power+Automate;Data+Engineering+Project">
</p>

---

## 📌 Problem Statement 1

A newly launched **🟢🟢 food delivery app startup in Mumbai 🟢🟢** is rapidly growing but facing operational and financial constraints.
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

# 🔴 Problem Statement 2: Order Cancellation Analysis

The Food Delivery App is experiencing a **20.48% order cancellation rate** across **18,526 total orders**, resulting in **3,794 lost transactions**.

The business needs to:

👉 Identify **root causes of cancellations**, including:

- ⚙️ Operational issues (late deliveries)  
- 🍽️ Product issues (pricing, wrong items)  
- 🚚 Service issues (delivery partner behavior)  
- 👤 Behavioral issues (abusive customers)

👉 Take **targeted actions** to reduce cancellations by **at least 30% in the next quarter**

#  Step 1: Cancellation Report Page 1

<p align="center">
  <img src="Docs/Cancellation report page 1.png" width="800"/>
</p>

---

## 📊 Dashboard Summary

This dashboard provides a **holistic view of order performance, cancellations, revenue, and profitability** for the food delivery platform.

* 📦 **Total Orders:** 19K
* ❌ **Cancelled Orders:** 3,794
* 📉 **Cancellation Rate:** **20.48%**
* ✅ **Conversion Rate:** 79.52%

💰 **Revenue Metrics**

* **Actual Revenue:** 9.03M
* **Gross Profit:** 1.03M
* **Gross Margin:** 11.43%

⚠️ **Profitability Gap**

* **GP Variance:** **-838.49K** (below target)

🧾 **Customer Metric**

* **Average Order Value (AOV):** 487.55

---

## 🔍 Key Insights

### 🚨 High Cancellation Rate

* **20.48% cancellation rate** indicates that **1 in every 5 orders is cancelled**
* Major contributor to **revenue loss and operational inefficiency**

---

### 💸 Strong Revenue but Weak Profitability

* Revenue is healthy (**9.03M**)
* However, **negative GP variance (-838K)** indicates:

  * High operational costs
  * Inefficiencies in delivery/logistics
  * Financial impact of cancellations

---

### 📈 Positive Growth Trend

* Yearly revenue shows **consistent growth**
* Business demand is strong, but **performance is not optimized**

---

### 📅 Monthly Revenue Patterns

* Peak months: **July – August**
* Low performance periods: **March – May, September**

👉 Indicates **seasonality or operational gaps**

---

### 🍽️ Revenue Concentration Across Restaurants

* A few restaurants contribute **major revenue share**
* Many low-performing restaurants exist

👉 Business is **dependent on top vendors**

---

### 🧾 Healthy Average Order Value

* AOV (~487) is stable and strong
* Suggests **pricing is not the primary issue**

---

### ⚠️ Impact of Cancellations

Cancellations are leading to:

* Lost revenue opportunities
* Increased operational costs
* Poor customer experience
* Lower retention rates

---

## 🎯 Business Recommendations

* 🚚 Improve delivery efficiency to reduce delays
* 📦 Enhance order accuracy (reduce wrong/missing items)
* 👤 Identify and control abusive/fake customers
* 📊 Focus on high-cancellation time slots
* 🍽️ Optimize performance of low-rated restaurants
* 💡 Introduce real-time tracking and alerts

---

## 🚀 Final Insight

> While the platform shows **strong demand and revenue growth**, high cancellations and operational inefficiencies are **impacting profitability**.
> Addressing these issues can significantly improve **revenue retention and customer satisfaction**.

---
#  Step 2: Cancellation Report Page 2

<p align="center">
  <img src="Docs/Cancellation report page 2.png" width="800"/>
</p>

## 📊 Order Cancellation Report (Page 2)

This dashboard focuses on **deep-diving into cancellation behavior**, identifying **key drivers**, and uncovering **operational inefficiencies** impacting order completion.

---

## 📌 Key Metrics

* ❌ **Total Cancelled Orders:** 3,794
* ⏱️ **Average Delivery Time:** 44.37 mins

### 🚚 Delivery Performance

* ✅ **On-time Deliveries:** 12K
* ⚠️ **Orders Exceeding Time:** 6,780

---

## 🔍 Cancellation Insights

### 🚨 Late Deliveries Impact

* 📦 **Orders Cancelled Due to Late Deliveries:** 1,388 (**36.58%**)
* ⚠️ Late delivery is a **major driver of cancellations**

---

### 🤔 Unexpected Behavior (Critical Insight)

* 📦 **Orders Cancelled Despite On-Time Delivery:** 2,406 (**63.40%**)

👉 Indicates:

* Issues beyond logistics such as:

  * 🍽️ Wrong or missing items
  * ❄️ Food quality (cold food)
  * 🚚 Poor delivery partner behavior
  * 💰 Pricing or charges complaints

---

### ⏱️ Delivery Time Comparison

* Avg time (On-time cancelled orders): **42 mins**
* Avg time (Late cancelled orders): **42 mins**

👉 Suggests:

* **Perception of delay matters more than actual time**
* Customer expectations may not be aligned with service delivery

---

## 🧩 Cancellation Reason Breakdown

Main contributing factors:

* 🕒 **Delayed Orders (~37.56%)**
* 🚚 **Delivery Partner Behavior (~24.96%)**
* 🍽️ **Order Issues (~23.33%)**
* 💰 **Charges/Other Complaints (~14.15%)**

👉 Insight:

* Cancellations are **multi-dimensional**, not just logistics-driven

---

## 📍 Location-Based Insights

* Highest cancellations observed in:

  * 📍 Lower Parel
  * 📍 Kharadi
  * 📍 Churchgate

👉 Indicates:

* High-demand areas may face **delivery bottlenecks**

---

## 🍽️ Restaurant-Level Insights

* Top contributors to cancellations:

  * The Bombay Canteen
  * Shree Thaker Bhojanalay
  * Pizza By The Bay

👉 Suggests:

* Certain restaurants have:

  * Higher order volume
  * Or operational inefficiencies

---

## 🎯 Key Takeaways

* 🚨 **Late delivery is important but NOT the biggest issue**
* ⚠️ Majority cancellations happen **even when delivery is on time**
* 🧠 Indicates strong influence of:

  * Food quality
  * Order accuracy
  * Service experience

---

## 🚀 Recommendations

* 🚚 Improve delivery experience (not just speed)
* 🍽️ Implement strict restaurant quality checks
* 📦 Reduce wrong/missing item issues
* 👤 Monitor delivery partner behavior
* 📊 Focus on high-cancellation locations
* ⏱️ Align customer expectations with realistic delivery times

---
# Step 3: Cancellation Report Page 3

<p align="center">
  <img src="Docs/Cancellation report page 3.png" width="800"/>
</p>


## 📊 Order Cancellation Report – Deeper View (Page 3)

This dashboard provides a **granular analysis of cancellation patterns**, focusing on **delivery time impact, restaurant-level issues, and high-risk segments** to uncover deeper operational insights.

---

## 📌 Key Metrics

* ❌ **Total Cancelled Orders:** 3,794
* 📉 **Cancellation Rate:** **20.48%**
* ⏱️ **Average Delivery Time:** 44.37 mins

### 🚚 Delivery Performance

* ✅ **On-time Deliveries:** 12K
* ⚠️ **Orders Exceeding Time:** 6,780

---

## 🔍 Advanced Insights

### ⏱️ Delivery Time Impact on Cancellations

* 📊 **Highest cancellations occur in the 40–50 minute time window**
* 🚨 **Late deliveries contribute ~36.6% of cancellations**

👉 Key Insight:

* Delivery delay is a **primary driver**, but not the only factor

---

### ⚠️ Early Cancellations (Before Delay Occurs)

* 📦 **63.40% of orders are cancelled before delay happens**

👉 Indicates:

* Customers are cancelling due to:

  * 🍽️ Poor food quality expectations
  * 📦 Wrong/missing items
  * 🚚 Service dissatisfaction
  * ⏳ Long perceived wait times

---

### 🧠 Customer Behavior Insight

* Average cancellation time (~42 mins) is similar for:

  * On-time deliveries
  * Late deliveries

👉 Insight:

* **Customer perception matters more than actual delivery time**

---

## 🍽️ Restaurant-Level Deep Dive

### 🔴 High Cancellation Restaurants

* Some restaurants show **extremely high cancellation rates**
* Example insights:

  * Certain outlets exceed **80–100% cancellation rate (data anomaly or repeated failures)**
  * Others consistently contribute high cancellation volume

👉 Possible reasons:

* Poor order management
* Food preparation delays
* Quality issues

---

### 📊 Cancellation vs Order Volume

* High-order restaurants → **higher absolute cancellations**
* But some low-volume restaurants → **very high cancellation %**

👉 Insight:

* Need to evaluate both:

  * Volume impact
  * Efficiency (rate-based performance)

---

## 📍 Location-Level Insights

* Certain locations show:

  * High order volume
  * High cancellation rates

👉 Indicates:

* Delivery network inefficiencies
* Traffic/logistics challenges
* Demand-supply imbalance

---

## 🧩 Cancellation Reasons (Detailed View)

Across restaurants, key recurring reasons:

* 🕒 Delayed Orders
* 🚚 Delivery Partner Behavior
* 🍽️ Order Quality Issues
* 💰 Charges/Other Complaints

👉 Insight:

* Issues vary by restaurant → requires **targeted interventions**

---

## 🎯 Key Takeaways

* 🚨 **40–50 mins is the critical risk window for cancellations**
* ⚠️ Majority cancellations occur **before actual delay**
* 🍽️ Restaurant performance plays a **major role**
* 📍 Location and logistics significantly impact outcomes
* 🧠 Customer perception is a **key hidden driver**

---

## 🚀 Recommendations

* ⏱️ Optimize delivery to stay within **<40 min window**
* 🍽️ Implement restaurant-level quality monitoring
* 🚚 Improve delivery partner accountability
* 📊 Flag high-risk restaurants & locations
* 🔍 Investigate anomalies (extremely high cancellation rates)
* 💡 Improve customer communication (real-time updates)

---

# Step 4: Cancellation Report Page 4

<p align="center">
  <img src="Docs/Cancellation report page 4.png" width="800"/>
</p>


## 📊 Order Cancellation Report – Customer Analysis (Page 4)

This dashboard focuses on **customer behavior and cancellation patterns**, identifying **high-risk users**, understanding **cancellation concentration**, and uncovering **behavioral drivers behind cancellations**.

---

## 📌 Key Metrics

* 📦 **Total Customers:** 952
* ❌ **Total Cancelled Orders:** 3,794

### 🚨 High-Risk Customer Segment

* 👥 **Customers with >5 Cancellations:** 64
* 📊 **High-Risk Customers (%):** **6.72%**
* 📦 **Orders from High-Risk Customers:** 12K
* ❌ **Cancellations by High-Risk Customers:** 2,561

👉 **Cancellation Contribution:** **67.50%**

---

## 🔍 Key Insights

### ⚠️ Pareto Effect in Cancellations

* Only **6.7% of customers** are responsible for **67.5% of total cancellations**

👉 Insight:

* Strong **Pareto (80/20) pattern**
* Small group of users causing **major business impact**

---

### 🚨 High-Risk / Abusive Customer Behavior

* Frequent cancellations indicate:

  * Fake or non-serious orders
  * Misuse of platform
  * Lack of accountability

👉 These users significantly:

* Increase operational costs
* Reduce delivery efficiency
* Impact service quality

---

### 🍽️ Restaurant Type Analysis

* **Delivery-based restaurants** have the highest cancellations (~63.94%)
* Followed by:

  * Casual Dining (~30.65%)
  * Quick Service (~5.40%)

👉 Insight:

* Delivery-heavy models are more prone to cancellations

---

### 💳 Subscription-Based Insights

* Customers without subscription show:

  * Higher order volume
  * Higher cancellations

* Discounted delivery pass users:

  * Lower cancellation rate

👉 Insight:

* Subscription plans may **improve customer commitment**

---

### 📅 Monthly Cancellation Trends

* Peak cancellation observed in:

  * 📈 **September (highest)**
  * Followed by July & October

* Lower cancellations in:

  * 📉 February & May

👉 Insight:

* Seasonal or demand-based behavioral patterns exist

---

### 🧑‍💻 Top Cancellation Contributors

* A ranked list shows **top users contributing highest cancellations**
* Some individual users contribute **50–100+ cancellations**

👉 Insight:

* Strong need for **user-level monitoring & control**

---

## 🎯 Key Takeaways

* 🚨 A small group of users drives the majority of cancellations
* 👤 High-risk customers are a **major hidden problem**
* 📦 Delivery-based orders are more cancellation-prone
* 💳 Subscription users show **better behavior**
* 📊 Customer behavior significantly impacts business performance

---

## 🚀 Recommendations

* 🚫 Identify & restrict high-risk customers
* ⚠️ Introduce cancellation penalties or limits
* 💳 Promote subscription plans to improve retention
* 📊 Monitor repeat cancellation patterns
* 🎯 Target high-risk users with stricter policies
* 📢 Improve communication to reduce unnecessary cancellations

---



## 📊 Final Executive Summary (All Dashboards)

This project provides a **comprehensive analysis of order cancellations, revenue performance, operational efficiency, and customer behavior** for a food delivery platform.

### 📌 Overall Performance

* 📦 **Total Orders:** 18,526
* ❌ **Total Cancelled Orders:** 3,794
* 📉 **Cancellation Rate:** **20.48%** (~1 in 5 orders)
* 💰 **Total Revenue:** 9.03M
* 📊 **Gross Profit:** 1.03M
* ⚠️ **GP Variance:** **-838K (below target)**
* 🧾 **Average Order Value:** 487.55

👉 While the platform shows **strong demand and revenue growth**, high cancellations are causing **significant revenue leakage and operational inefficiencies**

---

## 🔍 Consolidated Insights

### 🚨 1. High Cancellation Rate is the Core Problem

* 20.48% cancellation rate is **critically high**
* Direct impact on:

  * Revenue loss
  * Delivery inefficiency
  * Customer dissatisfaction

---

### ⏱️ 2. Delivery Delays are Important — But Not the Only Issue

* ~36.6% cancellations due to **late deliveries**
* Highest cancellations occur in **40–50 minute delivery window**

👉 However:

* **63.4% cancellations happen before delay occurs**

➡️ Indicates **customer experience issues beyond logistics**

---

### 🍽️ 3. Service & Product Issues Drive Hidden Cancellations

Key contributors:

* Wrong or missing items
* Poor food quality (cold food)
* Delivery partner behavior
* Pricing/charges complaints

👉 Insight:

* Problem is **multi-dimensional**, not just delivery speed

---

### 📍 4. Location & Restaurant Performance Matter

* Certain locations (e.g., high-demand areas) show **higher cancellations**
* Some restaurants contribute **disproportionately high cancellations**

👉 Indicates:

* Operational inefficiencies
* Vendor-specific issues

---

### 👤 5. Customer Behavior is a Major Driver (Critical Insight)

* Only **6.7% of customers** contribute to **67.5% of cancellations**
* Strong **Pareto effect (few users causing most issues)**

👉 Indicates:

* Presence of **high-risk / abusive customers**
* Behavioral misuse of platform

---

### 📊 6. Revenue vs Profitability Gap

* Revenue is strong (**9.03M**)
* But profitability is weak (**-838K variance**)

👉 Causes:

* Failed deliveries
* Refunds & cancellations
* Operational inefficiencies

---

### 📅 7. Demand & Seasonal Patterns

* Peak performance: **July–August**
* High cancellations: **September**
* Low periods: **Feb, May**

👉 Indicates:

* Seasonal demand fluctuations
* Operational inconsistency

---

## 🎯 Final Recommendations

### 🚚 1. Optimize Delivery Operations

* Improve route planning & dispatching
* Reduce delivery time to **<40 mins**
* Provide accurate ETAs

---

### 🍽️ 2. Improve Restaurant Quality Control

* Monitor high-cancellation restaurants
* Reduce wrong/missing items
* Ensure food quality standards

---

### 🚨 3. Control High-Risk Customers (Biggest Opportunity)

* Identify users with repeated cancellations
* Introduce:

  * Cancellation limits
  * Penalties for misuse
  * Account restrictions

👉 This alone can reduce cancellations significantly

---

### 📊 4. Focus on High-Impact Areas

* Target:

  * High-cancellation locations
  * Peak time slots
  * Low-performing vendors

---

### 💳 5. Encourage Better Customer Behavior

* Promote subscription plans
* Offer incentives for successful orders
* Improve communication & tracking

---

### 📢 6. Enhance Customer Experience

* Real-time order tracking
* Proactive delay notifications
* Better support resolution

---

### 🔍 7. Monitor & Act Continuously

* Build alerts for:

  * High cancellation spikes
  * Poor delivery performance
* Use dashboards for **real-time decision making**

---

## 🚀 Final Conclusion

> Order cancellations are a **multi-dimensional problem** involving
> **operations, service quality, and customer behavior**.

> While delivery delays contribute, the **biggest hidden driver is high-risk customer behavior and service experience gaps**.

👉 By addressing these areas, the business can realistically achieve:

* ✅ **30%+ reduction in cancellations**
* 💰 Improved profitability
* 😊 Better customer satisfaction

---



