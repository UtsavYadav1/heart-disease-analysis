import streamlit as st
import pandas as pd
import joblib

# Load the trained model and label encoders
try:
    rf_model = joblib.load('heart_disease_model.pkl')
    label_encoders = joblib.load('label_encoders.pkl')
except FileNotFoundError:
    st.error("Error: Model files not found. Please run 'analysis.py' first to generate them.")
    st.stop()

# Set page config
st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")

# Custom CSS for styling
st.markdown("""
<style>
    div.stButton > button:first-child {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff3333;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("❤️ Heart Disease Prediction App")
st.markdown("Enter the patient's health metrics below to predict the likelihood of heart disease using our Random Forest model.")

st.divider()

# Organize inputs into columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("Physical Metrics")
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=80.0, value=25.0, help="Weight in kg / (Height in meters)^2")
    physical_health = st.number_input("Physical Health (Poor Days / Month)", min_value=0, max_value=30, value=0)
    mental_health = st.number_input("Mental Health (Poor Days / Month)", min_value=0, max_value=30, value=0)
    sleep_time = st.number_input("Sleep Time (Hours / Night)", min_value=1, max_value=24, value=7)
    
    st.subheader("Lifestyle")
    smoking = st.selectbox("Smoking?", ["Yes", "No"])
    alcohol_drinking = st.selectbox("Alcohol Drinking?", ["Yes", "No"])
    physical_activity = st.selectbox("Physical Activity (Last 30 Days)?", ["Yes", "No"])

with col2:
    st.subheader("Demographics")
    age_category = st.selectbox("Age Category", sorted(list(label_encoders['AgeCategory'].classes_)))
    sex = st.selectbox("Sex", sorted(list(label_encoders['Sex'].classes_)))
    race = st.selectbox("Race", sorted(list(label_encoders['Race'].classes_)))
    
    st.subheader("Existing Medical Conditions")
    diff_walking = st.selectbox("Difficulty Walking?", ["Yes", "No"])
    stroke = st.selectbox("History of Stroke?", ["Yes", "No"])
    diabetic = st.selectbox("Diabetic?", sorted(list(label_encoders['Diabetic'].classes_)))
    asthma = st.selectbox("Asthma?", ["Yes", "No"])
    kidney_disease = st.selectbox("Kidney Disease?", ["Yes", "No"])
    skin_cancer = st.selectbox("Skin Cancer?", ["Yes", "No"])
    gen_health = st.selectbox("General Health Assessment", ["Excellent", "Very good", "Good", "Fair", "Poor"])

st.divider()

# Create a dictionary for prediction
input_data = {
    'BMI': [bmi],
    'Smoking': [smoking],
    'AlcoholDrinking': [alcohol_drinking],
    'Stroke': [stroke],
    'PhysicalHealth': [physical_health],
    'MentalHealth': [mental_health],
    'DiffWalking': [diff_walking],
    'Sex': [sex],
    'AgeCategory': [age_category],
    'Race': [race],
    'Diabetic': [diabetic],
    'PhysicalActivity': [physical_activity],
    'GenHealth': [gen_health],
    'SleepTime': [sleep_time],
    'Asthma': [asthma],
    'KidneyDisease': [kidney_disease],
    'SkinCancer': [skin_cancer]
}

# Convert to DataFrame
input_df = pd.DataFrame(input_data)

# Prediction Button
if st.button("Predict Heart Disease Risk", use_container_width=True):
    with st.spinner("Analyzing..."):
        # Apply the exact same encoding used during training
        encoded_df = input_df.copy()
        
        # We need to make sure we encode columns in the exact order the model expects.
        # It's safer to loop through the encoders dictionary logic
        for col, le in label_encoders.items():
            if col in encoded_df.columns:
                # Handle potential unseen values gracefully if needed, though UI restricts to known classes
                encoded_df[col] = le.transform(encoded_df[col])
        
        # Ensure column order matches exactly how it was trained
        # (Assuming the list of features is everything except 'HeartDisease' from original df)
        try:
             # The model feature names are stored in rf_model.feature_names_in_ (if scikit-learn >= 1.0)
             expected_features = rf_model.feature_names_in_
             encoded_df = encoded_df[expected_features]
        except AttributeError:
             # Fallback if scikit-learn version doesn't have feature_names_in_
             pass
        
        # Make Prediction
        prediction_encoded = rf_model.predict(encoded_df)
        prediction_proba = rf_model.predict_proba(encoded_df)
        
        # Decode the prediction
        # The target was 'HeartDisease' so it's handled by a label encoder in analysis.py
        # Actually analysis.py did fit_transform on target too. Let's find its encoder.
        target_encoder = label_encoders.get('HeartDisease')
        
        if target_encoder:
            prediction_label = target_encoder.inverse_transform(prediction_encoded)[0]
        else:
            # Fallback (usually 1=Yes, 0=No based on alphabetical Label Encoding of No/Yes)
            prediction_label = "Yes" if prediction_encoded[0] == 1 else "No"
            
        probability_yes = prediction_proba[0][1] if len(prediction_proba[0]) > 1 else 0.0

    # Display Results
    st.markdown("### Prediction Results")
    if prediction_label == "No":
        st.success(f"✅ **Low Risk.** The model predicts the patient DOES NOT currently have heart disease.")
    else:
        st.error(f"⚠️ **High Risk.** The model predicts the patient is AT RISK for heart disease.")
        
    st.info(f"**Model Confidence:** {probability_yes*100:.1f}% probability of Heart Disease.")
    
    st.caption("Disclaimer: This is a basic machine learning model created for educational purposes and should not be used for actual medical diagnosis.")
