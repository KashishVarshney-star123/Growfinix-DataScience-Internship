# 🔤 Task 4: NLP for Tour Enquiry Text Analysis

## 📌 Objective
Use NLP techniques on tour enquiry text descriptions to tokenize, remove stopwords, and perform sentiment analysis to categorize urgency or tone of enquiries.

## 🛠️ Tech Stack
- Python
- NLTK
- Scikit-Learn
- TF-IDF Vectorizer
- Logistic Regression
- Matplotlib

## 📊 Dataset
- **Type:** Synthetic Tour Enquiry Dataset
- **Records:** 200 enquiries
- **Categories:** Urgent & Normal

## 🔧 Steps Performed
1. Text Data Creation
2. Text Preprocessing (Lowercase, Special Char Removal)
3. Tokenization & Stopword Removal
4. TF-IDF Vectorization
5. Logistic Regression Model Training
6. Model Evaluation
7. Word Frequency Visualization
8. Sample Predictions

## 📈 Results
| Metric | Score |
|--------|-------|
| Accuracy | 100% |
| Urgent Detection | 86.53% Confidence |
| Normal Detection | 82.02% Confidence |

## 📁 Files
- `Untitled.ipynb` - Main Jupyter Notebook
- `nlp_model.pkl` - Trained Model
- `tfidf_vectorizer.pkl` - TF-IDF Vectorizer
- `word_frequency.png` - Word Frequency Plot

## 🚀 How to Run
```bash
pip install pandas numpy scikit-learn nltk matplotlib
jupyter notebook Untitled.ipynb
```