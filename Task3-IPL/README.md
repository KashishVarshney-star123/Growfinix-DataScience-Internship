# 🏏 Task 3: IPL Match Prediction

## 📌 Objective
Analyze historical IPL dataset and build a predictive model to forecast match outcomes, specifically analyzing team dynamics and historical win rates for Kolkata Knight Riders.

## 🛠️ Tech Stack
- Python
- Pandas
- Scikit-Learn
- Random Forest Classifier
- Matplotlib & Seaborn

## 📊 Dataset
- **Source:** Kaggle - IPL Complete Dataset 2008-2020
- **Matches:** 1095 matches
- **Deliveries:** 260920 deliveries

## 🔧 Steps Performed
1. Data Loading & Exploration
2. KKR Analysis (Win Rate & Season-wise Wins)
3. Data Preprocessing (Label Encoding)
4. Train-Test Split (80-20)
5. Random Forest Model Training
6. Toss Impact Analysis
7. Top Teams Visualization
8. Model Saving (.pkl)

## 📈 Results
| Metric | Value |
|--------|-------|
| Model Accuracy | 47.71% |
| KKR Total Matches | 251 |
| KKR Total Wins | 131 |
| KKR Win Rate | 52.19% |

## 📁 Files
- `Untitled.ipynb` - Main Jupyter Notebook
- `matches.csv` - Matches Dataset
- `deliveries.csv` - Deliveries Dataset
- `ipl_model.pkl` - Trained Model
- `kkr_season_wins.png` - KKR Season Wins Plot
- `toss_analysis.png` - Toss Impact Analysis
- `top_teams_wins.png` - Top Teams Visualization

## 🚀 How to Run
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
jupyter notebook Untitled.ipynb
```