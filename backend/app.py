from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(title="Diabetes Risk Prediction API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("diabetes_model.joblib")
COLUMNS = joblib.load("diabetes_columns.joblib")


class PatientInput(BaseModel):
    gender: int            
    age: float
    hypertension: int     
    heart_disease: int     
    bmi: float
    hba1c: float
    glucose: float
    smoking_history: str   


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Diabetes Risk Prediction API is running."}


@app.post("/predict")
def predict(patient: PatientInput):
    row = {
        "gender": patient.gender,
        "age": patient.age,
        "hypertension": patient.hypertension,
        "heart_disease": patient.heart_disease,
        "bmi": patient.bmi,
        "HbA1c_level": patient.hba1c,
        "blood_glucose_level": patient.glucose,
    }
    for col in COLUMNS:
        if col.startswith("smoke_"):
            label = col.replace("smoke_", "")
            row[col] = 1 if patient.smoking_history == label else 0

    input_df = pd.DataFrame([row])
    for col in COLUMNS:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[COLUMNS]

    proba = float(model.predict_proba(input_df)[0, 1])
    prediction = int(model.predict(input_df)[0])

    return {"probability": proba, "prediction": prediction}
