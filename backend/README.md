---
title: Diabetes Risk Prediction API
emoji: 🩺
colorFrom: teal
colorTo: blue
sdk: docker
app_port: 7860
---

# Diabetes Risk Prediction API

FastAPI backend serving a trained XGBoost model (ROC-AUC 0.975, Recall 0.88 on the
diabetic class) for the Complex Engineering Project: *Comparative Analysis of Machine
Learning Algorithms for Early Diabetes Prediction*.

## Endpoints

- `GET /` — health check
- `POST /predict` — returns diabetes risk probability for a patient

### Example request

```bash
curl -X POST https://YOUR-SPACE-URL.hf.space/predict \
  -H "Content-Type: application/json" \
  -d '{
    "gender": 0,
    "age": 67,
    "hypertension": 1,
    "heart_disease": 0,
    "bmi": 31.2,
    "hba1c": 7.8,
    "glucose": 220,
    "smoking_history": "former"
  }'
```

### Example response

```json
{"probability": 0.97, "prediction": 1}
```

This API is called by `diabetes_risk_instrument.html`, a standalone frontend that can be
opened on any machine with internet access — see that file for the live-demo UI.
