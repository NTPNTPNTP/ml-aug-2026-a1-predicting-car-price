# Car Price Prediction App

Web application that predicts the resale price of a used car based on its **manufacturing year** and **maximum power (bhp)**, using a Random Forest model trained on the Cars.csv dataset.

## Features

- Simple web form for entering car year and max power
- Missing fields can be left blank — filled in automatically using median imputation from the training data
- Prediction served via a FastAPI backend and displayed on the same page

## Tech Stack

- **Backend**: FastAPI + Uvicorn
- **Frontend**: Static HTML/CSS/JS (served by FastAPI)
- **Model**: scikit-learn Random Forest Regressor (`model/car_price_model.pkl`)
- **Package manager**: uv
- **Containerization**: Docker + Docker Compose

## Project Structure
```
.
├── app/
│   ├── main.py          # FastAPI app + /predict endpoint
│   └── static/
│       └── index.html   # Frontend form + result display
├── model/
│   └── car_price_model.pkl
├── data/
│   └── Cars.csv
├── experiments.ipynb    # EDA, feature engineering, model comparison
├── Dockerfile
├── docker-compose.yaml
├── pyproject.toml
└── uv.lock
```

## Running Locally (without Docker)
```
uv sync
cd app
uv run uvicorn main:app --reload
```
Then open http://localhost:8000

## Running with Docker
```
docker compose up --build
```
Then open http://localhost:8000

## Model Info

- **Features used**: `year`, `max_power`
- **Target**: `selling_price` (log-transformed during training)
- **Algorithm**: Random Forest Regressor (tuned via GridSearchCV)
- **Test R²**: ~0.936–0.938

## Deployment

This app is deployed on [Render](https://render.com) as a Docker-based web service.

- Render builds and runs the app directly from the `Dockerfile` at the repository root
- Every push to the `main` branch triggers an automatic redeploy
- Environment: **Region** = Singapore (Southeast Asia)

**Live demo**: [https://ml-aug-2026-a1-predicting-car-price.onrender.com](https://ml-aug-2026-a1-predicting-car-price.onrender.com)
