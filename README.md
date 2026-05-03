# 📰 Fake News Detector (Machine Learning + Streamlit)

A **Machine Learning web app** that detects whether a given news article is **FAKE** or **REAL**.  
Users can paste a news article into the app and instantly get a prediction result — built using **Python**, **Scikit-learn**, and **Streamlit**.

🔗 **GitHub Repository:** [https://github.com/shk365/fake_news_detector](https://github.com/shk365/fake_news_detector)

---

## 🚀 Features

- 🧠 Detects fake or real news using **TF-IDF Vectorization** and **Passive Aggressive Classifier**  
- ⚡ Real-time text input through an **interactive Streamlit web interface**  
- 📊 Includes **model evaluation metrics** — accuracy score and confusion matrix  
- 🧾 Detailed **project report** and **flowcharts** for documentation  
- 💾 Trained model and vectorizer saved for instant prediction  

---

## 🧠 Tech Stack

| Category | Tools / Libraries |
|-----------|------------------|
| **Frontend** | Streamlit |
| **Backend** | Python, Scikit-learn |
| **ML Model** | Passive Aggressive Classifier |
| **Feature Extraction** | TF-IDF Vectorizer |
| **Data Handling** | Pandas, NumPy |
| **Visualization** | Matplotlib, Seaborn |

---

## 🧾 Dataset

- Dataset contains 3 columns:
  - `title` – Headline of the news  
  - `text` – Full news content  
  - `label` – Target output (“FAKE” or “REAL”)  
- Example:

| title | text | label |
|-------|------|--------|
| "Breaking: New policy announced..." | "The government today..." | REAL |
| "Shocking! You won’t believe this..." | "A viral post claims..." | FAKE |

---

## ⚙️ How It Works

1. Load dataset and clean the text  
2. Split data into **training (80%)** and **testing (20%)**  
3. Convert text into numerical features using **TF-IDF Vectorizer**  
4. Train **Passive Aggressive Classifier** on the training data  
5. Evaluate model using accuracy and confusion matrix  
6. Build **Streamlit UI** for user input and real-time prediction  

---

## 💻 Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/shk365/fake_news_detector.git
cd fake_news_detector
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the Model (optional)
```bash
python train_model.py
```

### 4. Run the Web App
```bash
streamlit run app.py
```

### 5. Open in Browser  
➡️ Go to **http://localhost:8501**

---

## 📊 Model Evaluation

| Metric | Value |
|---------|--------|
| Accuracy | ~94% |
| Precision | 0.93 |
| Recall | 0.95 |
| F1 Score | 0.94 |

**Confusion Matrix:**
```
[[888   45]
 [ 62 1023]]
```

---

## 🌐 Streamlit Web App  
![System Architecture](screenshot.png)

---

## 📚 References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Fake News Detection Dataset – Kaggle](https://www.kaggle.com/)
- [Python Official Docs](https://docs.python.org/3/)

---

## 👨‍💻 Author

**shk365**  

🌐 [github.com/shk365](https://github.com/shk365)

---

## 🏁 License
This project is licensed under the **MIT License** – feel free to use, modify, and share it with credit.
