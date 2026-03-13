# Heart Disease SQL & Machine Learning Analysis

## Overview
This project presents a comprehensive analysis of heart disease data using **SQL** for exploratory data extraction, and **Python (Pandas, Scikit-Learn, Streamlit)** for deeper Exploratory Data Analysis (EDA) and predictive modeling. The goal is to uncover patterns and risk factors associated with heart disease, build a machine learning model, and serve it via an interactive web application.

## Live Demo
Check out the live running application here: **[Link to be Added after Deployment]**

## Tools & Technologies
- **SQL**: Used for querying and aggregating the dataset.
- **Python**: 
  - `pandas` for data manipulation.
  - `scikit-learn` for training a Random Forest classification model.
  - `streamlit` for creating an interactive web interface.
  - `joblib` for saving and loading the trained model state.
- **GitHub**: Version control and project showcasing.

## Repository Contents
- `app.py` - The interactive **Streamlit web application** that accepts user health data and predicts heart disease risk in real-time.
- `analysis.py` - The Python script responsible for cleaning the data, generating EDA plots, and training the predictive Machine Learning model. Running this outputs the `.pkl` files.
- `heart_disease_model.pkl` & `label_encoders.pkl` - Saved model states allowing the Streamlit app to run instantly.
- `Heart_new2.csv` - The primary dataset.
- `queries.sql` - SQL scripts containing data analysis queries.
- `requirements.txt` - Python package dependencies needed to run the analysis and the app.

## How to Run the App Locally
To run the interactive demonstration on your own machine:

1. Clone the repository and install dependencies:
```bash
pip install -r requirements.txt
```

2. Generate the trained model files (if not already present):
```bash
python analysis.py
```

3. Launch the Streamlit Web Application:
```bash
streamlit run app.py
```
This will open a new tab in your web browser where you can interact with the Heart Disease prediction model.
