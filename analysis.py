import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import warnings
warnings.filterwarnings('ignore')

print("Starting Heart Disease Analysis...")

# 1. Load Data
df = pd.read_csv('Heart_new2.csv')
print(f"Dataset Loaded. Shape: {df.shape}")

# 2. Basic Exploration & Cleaning
# (Assuming data is mostly clean based on structure, just checking for nulls)
if df.isnull().sum().any():
    print("Missing values found. Dropping...")
    df = df.dropna()

# 3. Exploratory Data Analysis (EDA)
sns.set_theme(style="whitegrid")

# Plot 1: Heart Disease Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x='HeartDisease', data=df, palette='Set2')
plt.title('Distribution of Heart Disease Cases')
plt.savefig('heart_disease_distribution.png')
print("Saved heart_disease_distribution.png")
plt.close()

# Plot 2: BMI by Heart Disease
plt.figure(figsize=(8, 6))
sns.boxplot(x='HeartDisease', y='BMI', data=df, palette='Set1')
plt.title('BMI vs Heart Disease')
plt.savefig('bmi_vs_heart_disease.png')
print("Saved bmi_vs_heart_disease.png")
plt.close()

# 4. Data Preprocessing for Machine Learning
# Encode categorical variables
le = LabelEncoder()
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# Separate Features (X) and Target (y)
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

# 5. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Model Training (Random Forest)
print("Training Random Forest Classifier...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 7. Model Evaluation
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print(f"Accuracy: {accuracy:.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("------------------------")
print("Analysis complete.")
