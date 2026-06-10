# 🏠 Task 1: Real Estate Price Prediction

## 📌 Objective
Build a regression model to predict property prices based on features like square footage, location, and amenities.

## 🛠️ Tech Stack
- Python
- Scikit-Learn
- XGBoost
- Pandas
- Matplotlib & Seaborn

## 📊 Dataset
- **Source:** Kaggle - Housing Prices Dataset
- **Records:** 545 properties
- **Features:** Area, Bedrooms, Bathrooms, Stories, Amenities

## 🔧 Steps Performed
1. Data Loading & Exploration
2. Data Preprocessing (Label Encoding)
3. Train-Test Split (80-20)
4. XGBoost Model Training
5. Model Evaluation (RMSE & R² Score)
6. Feature Importance Visualization
7. Model Saving (.pkl)

## 📈 Results
| Metric | Score |
|--------|-------|
| RMSE | 1,446,910.78 |
| R² Score | 0.5858 |

## 📁 Files
- `Untitled.ipynb` - Main Jupyter Notebook
- `Housing.csv` - Dataset
- `real_estate_model.pkl` - Trained Model
- `actual_vs_predicted.png` - Visualization
- `feature_importance.png` - Feature Importance Plot

## 🚀 How to Run
```bash
pip install pandas numpy scikit-learn xgboost matplotlib seaborn
jupyter notebook Untitled.ipynb
```