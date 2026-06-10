# 🚀 Task 5: Model Deployment via FastAPI

## 📌 Objective
Deploy the trained Real Estate Price Prediction model as a REST API using FastAPI so clients can send property features and receive predicted prices.

## 🛠️ Tech Stack
- Python
- FastAPI
- Uvicorn
- Joblib
- Pydantic

## 🔧 Steps Performed
1. FastAPI App Setup
2. Real Estate Model Loading
3. Input Schema Definition (Pydantic)
4. REST API Endpoints Creation
5. API Testing via Swagger UI

## 🌐 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API Health Check |
| POST | /predict | Predict Property Price |

## 📥 Sample Request
```json
{
  "area": 5000,
  "bedrooms": 3,
  "bathrooms": 2,
  "stories": 2,
  "mainroad": 1,
  "guestroom": 0,
  "basement": 0,
  "hotwaterheating": 0,
  "airconditioning": 1,
  "parking": 2,
  "prefarea": 1,
  "furnishingstatus": 1
}
```

## 📤 Sample Response
```json
{
  "predicted_price": "₹7,631,618.50",
  "status": "success"
}
```

## 📁 Files
- `main.py` - FastAPI Application
- `real_estate_model.pkl` - Trained Model

## 🚀 How to Run
```bash
pip install fastapi uvicorn joblib
uvicorn main:app --reload
```
Visit: http://127.0.0.1:8000/docs