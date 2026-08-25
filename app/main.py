import joblib
import numpy as np
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Load model
model = joblib.load("../model/car_price_model.pkl")

YEAR_MEDIAN = 2015
MAX_POWER_MEDIAN = 82.85

# Set up to serve static files (HTML files)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Data structure to receive from web (fields are optional to support skipping)
class CarData(BaseModel):
    year: Optional[int] = None
    max_power: Optional[float] = None

@app.get("/")
def read_root():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict_price(data: CarData):
    # imputation: If a field is missing, replace it with the median from the training data
    year = data.year if data.year is not None else YEAR_MEDIAN
    max_power = data.max_power if data.max_power is not None else MAX_POWER_MEDIAN

    input_features = np.array([[max_power, year]])
    pred_log = model.predict(input_features)
    final_price = float(np.exp(pred_log[0]))

    print("input features:", input_features)
    print("predicted price:", final_price)
    return {"predicted_price": round(final_price, 2)}