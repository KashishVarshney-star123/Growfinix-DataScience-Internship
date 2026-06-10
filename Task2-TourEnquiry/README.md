# 🎯 Task 2: Tour Enquiry Conversion Prediction

## 📌 Objective
Build a classification model to predict whether an incoming tour enquiry will convert into a paid booking.

## 🛠️ Tech Stack
- Python
- Scikit-Learn
- Random Forest Classifier
- Imbalanced-Learn (SMOTE)
- Pandas & Numpy

## 📊 Dataset
- **Type:** Synthetic Dataset
- **Records:** 1000 enquiries
- **Features:** Text Length, Hour of Submission, Age, Budget, Demographics

## 🔧 Steps Performed
1. Synthetic Dataset Creation
2. Data Preprocessing (Label Encoding)
3. Class Imbalance Handling (SMOTE)
4. Train-Test Split (80-20)
5. Random Forest Model Training
6. Model Evaluation (Accuracy, Classification Report)
7. Confusion Matrix Visualization
8. Model Saving (.pkl)

## 📈 Results
| Metric | Score |
|--------|-------|
| Accuracy | 67.78% |
| Conversion Probability (Sample) | 71.00% |

## 📁 Files
- `Untitled.ipynb` - Main Jupyter Notebook
- `tour_enquiry_model.pkl` - Trained Model
- `scaler.pkl` - Standard Scaler
- `confusion_matrix.png` - Confusion Matrix
- `feature_importance.png` - Feature Importance Plot

## 🚀 How to Run
```bash
pip install pandas numpy scikit-learn imbalanced-learn matplotlib seaborn
jupyter notebook Untitled.ipynb
```