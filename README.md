# Diabetes Risk Prediction

A machine learning project for early diabetes risk detection.

**Live demo:** [diabetes.fardeen-pranto.online](https://diabetes.fardeen-pranto.online)

## What's in here

- **Model** — an XGBoost classifier (ROC-AUC 0.975, Recall 0.88 on the diabetic class),
  trained on ~96k patient records (`diabetes_prediction_dataset.csv`). Training and
  evaluation are in `diabetes_prediction_project.ipynb`.
- **Backend** (`backend/`) — a FastAPI service that loads the trained model and serves
  predictions.
- **Frontend** (`diabetes_risk_instrument_api.html`) — a standalone HTML page with a
  live risk gauge. No build step, no dependencies — open it in a browser and point it
  at any running instance of the API.
- **Deploy configs** (`deploy/`) — the Docker Compose and nginx configs used to run
  this in production, kept here for reference.

## API

| Method | Endpoint    | Description                          |
|--------|-------------|---------------------------------------|
| GET    | `/`         | Health check                          |
| POST   | `/predict`  | Returns diabetes risk probability     |

**Request body:**
```json
{
  "gender": 0,
  "age": 67,
  "hypertension": 1,
  "heart_disease": 0,
  "bmi": 31.2,
  "hba1c": 7.8,
  "glucose": 220,
  "smoking_history": "former"
}
```
`gender`: `0` or `1`. `hypertension` / `heart_disease`: `0` (no) or `1` (yes).
`smoking_history`: one of `never`, `former`, `current`, `ever`, `not current`.

**Response:**
```json
{ "probability": 0.97, "prediction": 1 }
```

Try it against the live API:
```bash
curl -X POST https://diabetes.fardeen-pranto.online/api/predict \
  -H "Content-Type: application/json" \
  -d '{"gender":0,"age":67,"hypertension":1,"heart_disease":0,"bmi":31.2,"hba1c":7.8,"glucose":220,"smoking_history":"former"}'
```

## Running locally

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

The API will be at `http://localhost:8000`. Open `diabetes_risk_instrument_api.html`
in a browser and enter `http://localhost:8000` as the API URL to test against it.

Or with Docker:
```bash
cd backend
docker build -t diabetes-api .
docker run -p 7860:7860 diabetes-api
```

## Tech stack

FastAPI · XGBoost · scikit-learn · pandas · Docker · nginx

## Disclaimer

This tool is for educational and demonstration purposes only. It is not a medical
device and should not be used for actual diagnosis or treatment decisions.