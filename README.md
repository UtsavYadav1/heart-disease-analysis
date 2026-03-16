# Heart Disease Analysis Platform

This project is a **web-based analytics platform** for analyzing heart disease data. It has been built using **Flask** and embeds **interactive Tableau dashboards** to support different user scenarios (Clinical, Policy, and Personal).

---

## Interactive Tableau Dashboard

You can explore the interactive Tableau dashboard for this project here:

🔗 **Live Dashboard:**
https://public.tableau.com/app/profile/utsav.yadav8693/viz/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard3

### Dashboard Visualizations Included

The dashboard provides multiple analytical views to understand heart disease patterns:

1. **Age vs Heart Disease Risk**
   Shows how heart disease risk varies across different age groups.

2. **Smoking vs Heart Disease**
   Analyzes the relationship between smoking habits and heart disease occurrence.

3. **General Health Bubble Chart**
   Visualizes overall population health distribution (Excellent, Very Good, Good, Fair, Poor).

4. **Asthma vs Heart Disease**
   Examines whether asthma patients show different heart disease patterns.

5. **Stroke Distribution**
   Displays the proportion of stroke cases in the dataset.

### Purpose of the Dashboard

The goal of this dashboard is to help:

* Doctors identify high-risk patient groups
* Policy makers analyze public health trends
* Individuals understand lifestyle risk factors

The dashboard is fully interactive and allows users to visually explore health risk patterns within the dataset.


## 🛠 Tech Stack

**Backend**

* Python
* Flask

**Data Visualization**

* Tableau Public

**Frontend**

* HTML
* CSS (Premium Glassmorphism Dark Theme)

**Machine Learning (Optional Expansion)**

* scikit-learn
* joblib

---

## 👥 Scenarios Addressed

**Dr. Utsav (Cardiologist)**
Identifying high-risk middle-aged patients and analyzing lifestyle correlations.

** Urvashi (Policy Maker)**
Analyzing population trends to support public health policy decisions.

**Tarun (Patient)**
Monitoring personal health indicators against general benchmarks to guide lifestyle improvements.

---

## ▶️ How to Run the App

1️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

2️⃣ Run the Flask application:

```bash
python app.py
```

or

```bash
flask --app app.py run
```

3️⃣ Open the application in your browser:

```
http://127.0.0.1:5000
```

---

## 🔄 Updating Tableau Dashboards

Currently, `app.py` connects to a Tableau Public dashboard.

To use your own dashboard:

1. Open your `.twbx` file in **Tableau Desktop or Tableau Public**
2. Publish the workbook to **Tableau Public**
3. Click **Share** and copy the dashboard link
4. Replace the `tableau_url` inside the **SCENARIOS dictionary** in `app.py`

---

## 📁 Project Structure

```
app.py → Main Flask application and routing
templates/ → HTML templates for the UI
static/ → CSS styling assets
Heart_new2.csv → Dataset used for analysis
queries.sql → SQL queries for insights
dashboard.twbx → Original Tableau workbook
```

---

## 📌 Features

* Interactive Tableau dashboard integration
* Clean Flask web interface
* Healthcare analytics insights
* Scenario-based data exploration
* Easily extendable for machine learning models

---

## 🚀 Future Improvements

* Add predictive heart disease risk model
* Deploy the application online (Render / Railway / Heroku)
* Add more advanced Tableau visualizations
* Integrate real-time health monitoring data
