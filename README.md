# 🚗 Car Price Predictor

An AI-powered web application that predicts the resale price of used cars in the Indian market. Built with Flask and Machine Learning.

## 🔗 Live Demo
👉 [Click here to try the app](https://huggingface.co/spaces/shai-yad/car-price-predictor)

---

## ✨ Features

- 🤖 **AI-Powered Predictions** — Random Forest model with 92.27% accuracy
- 🚘 **15,000+ car records** trained from CarDekho dataset
- 💰 **Smart price formatting** — shows Thousand / Lakh / Crore automatically
- 🎨 **Modern dark UI** — responsive design for mobile and desktop
- ⚡ **Instant predictions** — results in under a second
- 🏷️ **Covers all price ranges** — from ₹50,000 budget cars to ₹1 Crore+ luxury cars

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| ML Model | Random Forest (scikit-learn) |
| Data | Pandas, NumPy |
| Dataset | CarDekho (15,392 records) |
| Deployment | Hugging Face Spaces |
| Version Control | GitHub |

---

## 📂 Project Structure
Car_Price_Predictor/
├── application.py          ← Flask backend
├── RandomForestModel.pkl   ← Trained ML model
├── Cleaned_car_new.csv     ← Cleaned dataset
├── requirements.txt        ← Python dependencies
├── Dockerfile              ← Container configuration
├── .gitignore
├── static/
│   └── css/
│       └── style.css       ← Custom dark theme styles
└── templates/
└── index.html          ← Frontend UI

---

## 🧠 ML Model Details

| Property | Details |
|---|---|
| Algorithm | Random Forest Regressor |
| Dataset | CarDekho Used Cars |
| Training rows | 12,313 |
| Testing rows | 3,079 |
| Accuracy (R² Score) | **92.27%** |
| Features used | Company, Model, Year, KM Driven, Fuel Type |

### Model Comparison

| Model | Dataset Size | Accuracy |
|---|---|---|
| Linear Regression | 800 rows | 84% |
| Linear Regression | 15,392 rows | 78% |
| **Random Forest** | **15,392 rows** | **92.27% ✅** |

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/ShaileshY7/Car-Price-Predictor.git
cd Car-Price-Predictor
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
python application.py
```

### 5. Open in browser
http://127.0.0.1:7860

---

## 📊 Sample Predictions

| Company | Model | Year | Fuel | KM | Predicted Price |
|---|---|---|---|---|---|
| Maruti | Alto | 2017 | Petrol | 80,000 | ₹2.38 Lakh |
| Honda | City | 2020 | Diesel | 60,000 | ₹5.85 Lakh |
| Toyota | Fortuner | 2021 | Diesel | 20,000 | ₹28.65 Lakh |
| Audi | A4 | 2022 | Petrol | 60,000 | ₹30.82 Lakh |

---

## 📦 Dependencies
Flask==3.1.3
flask-cors==6.0.2
pandas==2.2.2
scikit-learn==1.5.2
numpy==1.26.4
joblib==1.5.3
gunicorn

---

## 🌐 Deployment

This app is deployed on **Hugging Face Spaces** (free tier) using Docker.

> ✅ Always on — no cold starts or sleep delays!

---

## 👨‍💻 Author

**Shailesh Yadav**
- GitHub: [@ShaileshY7](https://github.com/ShaileshY7)
- Hugging Face: [@shai-yad](https://huggingface.co/shai-yad)

---

## 📄 License

This project is open source and available under the MIT License.
