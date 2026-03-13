# 🏏 IPL Win Predictor – Machine Learning Project

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white) 
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.25-orange?logo=scikitlearn&logoColor=white) 
![License](https://img.shields.io/badge/License-MIT-green)


## 🌐 Live Link
Try the live app here: [IPL Win Predictor](https://ipl-win-predictor-6wxd.onrender.com)

---

## 📌 Project Overview
**IPL Win Predictor** is a **machine learning project** that predicts the outcome of Indian Premier League matches **before they are played**. It leverages historical match data, toss outcomes, venue information, and team performance metrics to forecast the winning team with high accuracy.

---

## 🎯 Problem Statement
IPL matches are highly unpredictable due to dynamic team compositions, pitch conditions, and toss decisions. This project provides:  
- **Data-driven insights** for IPL match predictions  
- **Machine learning models** for accurate win forecasts  
- A **framework for future enhancements**, including player-level analysis and live match predictions  

---

## 🗂 Dataset
- **Source:** [Kaggle IPL Dataset](https://www.kaggle.com/) *(replace with actual dataset link)*  
- **Key Features:**

| Feature          | Description                               |
|-----------------|-------------------------------------------|
| `team1`         | First competing team                       |
| `team2`         | Second competing team                      |
| `toss_winner`   | Team that won the toss                     |
| `toss_decision` | Bat/Field decision                          |
| `venue`         | Match location                              |
| `date`          | Match date                                 |
| `team1_score`   | Score of team1 in previous matches        |
| `team2_score`   | Score of team2 in previous matches        |
| `winner`        | Target variable – predicted winner        |

---

## 🛠 Tech Stack
- **Languages:** Python 3.x  
- **Libraries:** pandas, numpy, scikit-learn, XGBoost, LightGBM, matplotlib, seaborn  
- **Tools:** Jupyter Notebook, VS Code, Git & GitHub  

---

## 🧠 Machine Learning Models & Performance

| Model                       | Accuracy  | Notes                                                       |
|------------------------------|-----------|-------------------------------------------------------------|
| Logistic Regression          | 79.85%    | Convergence warning – consider increasing `max_iter`       |
| Decision Tree Classifier     | 99.16%    | Simple tree, high accuracy; may overfit                    |
| Random Forest Classifier     | 99.92%    | Best model; deployed as `model.pkl`                        |
| K-Nearest Neighbors (KNN)    | 89.80%    | Sensitive to feature scaling                                |
| Gradient Boosting Classifier | 83.78%    | Handles non-linearities, less overfitting than Decision Tree |

**✅ Selected Model for Deployment:** `RandomForestClassifier`  
**Saved as:** `model.pkl`


## Live Link -->(https://ipl-win-predictor-6wxd.onrender.com)

---

## 🚀 How to Run Locally

1. Clone the repository:  
```bash
git clone https://github.com/username/ipl-win-predictor.git
