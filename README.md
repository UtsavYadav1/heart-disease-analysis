# Heart Disease Analysis Platform

This project is a **web-based analytics platform** for analyzing heart disease data. It has been built using **Flask** and embeds **interactive Tableau dashboards** to support different user scenarios (Clinical, Policy, and Personal).

---

## 📊 Interactive Tableau Dashboard

You can explore the **live interactive Tableau dashboard** here:

🔗 **Tableau Public Dashboard**
https://public.tableau.com/app/profile/utsav.yadav8693/viz/HeartDiseaseAnalysisDashboard_17736583160470/Dashboard2

The dashboard provides insights such as:

* Age vs Heart Disease distribution
* Smoking vs Heart Disease relationship
* BMI vs Heart Disease analysis
* Asthma vs Heart Disease correlation

These visualizations help users understand patterns and risk factors related to heart disease.

---

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

**Dr. Sharma (Cardiologist)**
Identifying high-risk middle-aged patients and analyzing lifestyle correlations.

**Ramesh (Policy Maker)**
Analyzing population trends to support public health policy decisions.

**Anita (Patient)**
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
