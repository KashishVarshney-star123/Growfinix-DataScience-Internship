from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# App initialize karo
app = FastAPI(title="Real Estate Price Prediction API")

# Model load karo
model = joblib.load("real_estate_model.pkl")

# Input schema define karo
class PropertyFeatures(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus: int

# Root endpoint
@app.get("/")
def home():
    return {"message": "🏠 Real Estate Price Prediction API is running!"}

# Prediction endpoint
@app.post("/predict")
def predict_price(features: PropertyFeatures):
    data = np.array([[
        features.area,
        features.bedrooms,
        features.bathrooms,
        features.stories,
        features.mainroad,
        features.guestroom,
        features.basement,
        features.hotwaterheating,
        features.airconditioning,
        features.parking,
        features.prefarea,
        features.furnishingstatus
    ]])
    
    predicted_price = model.predict(data)[0]
    
    return {
        "predicted_price": f"₹{predicted_price:,.2f}",
        "status": "success"
    }