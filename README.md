# Heart Disease Analysis Platform

This project is a web-based analytics platform for analyzing heart disease data. It has been built using **Flask** and embeds interactive **Tableau Dashboards** to cater to various user scenarios (Clinical, Policy, and Personal).

## Tech Stack
- **Backend:** Python, Flask
- **Data Visualization:** Tableau
- **Frontend:** HTML, CSS (Premium Glassmorphism Dark Theme)
- **Machine Learning (Optional Expansion):** scikit-learn, joblib

## Scenarios Addressed
1. **Dr. Sharma (Cardiologist):** Identifying high-risk middle-aged patients and lifestyle correlations.
2. **Ramesh (Policy Maker):** Analyzing regional trends to form public health policies.
3. **Anita (Patient):** Monitoring personal health metrics against benchmarks to make lifestyle choices.

## How to Run the App

1. **Install requirements:**
   `pip install -r requirements.txt`
   
2. **Run the Flask application:**
   `flask --app app.py run` (or simply `python app.py`)

3. **View the Application:**
   Open a browser and navigate to `http://127.0.0.1:5000`

## Updating Tableau Dashboards

Currently, `app.py` uses placeholder Tableau Public URLs. To connect your own Tableau workbooks:

1. Open `dashboard.twbx` in Tableau Desktop or Tableau Public.
2. Publish the workbook to Tableau Public or your own Tableau Server.
3. Click the "Share" button on your published visualization and copy the embed link.
4. Replace the `tableau_url` strings in the `SCENARIOS` dictionary within `app.py`.

## Files
- `app.py` → Main Flask application and routing
- `templates/` → HTML templates for the UI
- `static/` → CSS styling assets
- `dataset.csv` → Raw dataset used for analysis
- `queries.sql` → SQL queries for data insights
- `dashboard.twbx` → The original Tableau workbook
