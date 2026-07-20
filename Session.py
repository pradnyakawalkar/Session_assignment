# ==========================
# HEART DISEASE PREDICTION
# ==========================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

# -------------------------
# Q1. Load Dataset
# -------------------------

df = pd.read_csv("heart.csv")

print("First 5 Rows")
print(df.head())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Values:", df.duplicated().sum())

df = df.drop_duplicates()

# Features and Target
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Encoding
X = pd.get_dummies(X, drop_first=True)



X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nShapes")
print("X_train :", X_train.shape)
print("X_test :", X_test.shape)
print("y_train :", y_train.shape)
print("y_test :", y_test.shape)

# -------------------------
# Q3. Standard Scaler
# -------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -------------------------
# Logistic Regression
# -------------------------

model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# -------------------------
# Q4. Prediction
# -------------------------

# Make predictions 
y_pred = model.predict(X_test) 
 
# Print first 10 actual and predicted values 
print("Actual Values:") 
print(y_test.head(10)) 
 
print("\nPredicted Values:")
print(y_pred[:10]) 

# -------------------------
# Q5. Confusion Matrix
# -------------------------

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix")
print(cm)

TN = cm[0][0]
FP = cm[0][1]
FN = cm[1][0]
TP = cm[1][1]

print("\nTrue Negative :", TN)
print("False Positive :", FP)
print("False Negative :", FN)
print("True Positive :", TP)

# -------------------------
# Q6. Evaluation
# -------------------------

print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("Precision :", precision_score(y_test, y_pred))
print("Recall :", recall_score(y_test, y_pred))
print("F1 Score :", f1_score(y_test, y_pred))

print("\nClassification Report")
print(classification_report(y_test, y_pred))

# -------------------------
# Q7. Save Model
# -------------------------

joblib.dump(model, "heart_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(X.columns.tolist(), "columns.pkl")

print("\nModel Saved Successfully")

loaded_model = joblib.load("heart_model.pkl")
loaded_scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

sample = X.iloc[[0]]

sample = loaded_scaler.transform(sample)

prediction = loaded_model.predict(sample)

print("\nPrediction for Sample Record")

if prediction[0] == 1:
    print("Heart Disease : Yes")
else:
    print("Heart Disease : No")

import streamlit as st

st.title("Heart Disease Prediction")

# Input Fields
age = st.number_input("Age", min_value=1, max_value=100, value=40)
restingbp = st.number_input("RestingBP", value=120)
cholesterol = st.number_input("Cholesterol", value=200)
fastingbs = st.selectbox("FastingBS", [0, 1])
maxhr = st.number_input("MaxHR", value=150)
oldpeak = st.number_input("Oldpeak", value=0.0)

sex = st.selectbox("Sex", ["F", "M"])
chestpain = st.selectbox("ChestPainType", ["ATA", "NAP", "TA", "ASY"]) 
restingecg = st.selectbox("RestingECG", ["Normal", "ST", "LVH"])
exerciseangina = st.selectbox("ExerciseAngina", ["N", "Y"]) 
stslope = st.selectbox("ST_Slope", ["Up", "Flat", "Down"]) 

# Predict Button 
if st.button("Predict"):

    input_data = pd.DataFrame({
    "Age": [age],
    "RestingBP": [restingbp],
    "Cholesterol": [cholesterol],
    "FastingBS": [fastingbs],
    "MaxHR": [maxhr],
    "Oldpeak": [oldpeak],
    "Sex": [sex],
    "ChestPainType": [chestpain],
    "RestingECG": [restingecg],
    "ExerciseAngina": [exerciseangina],
    "ST_Slope": [stslope]
})

    input_data = pd.get_dummies(input_data)

    input_data = input_data.reindex(columns=columns, fill_value=0)

    input_data = scaler.transform(input_data)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Heart Disease : Yes")
    else:
        st.success("Heart Disease : No")