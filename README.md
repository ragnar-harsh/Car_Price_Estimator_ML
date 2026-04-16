# 🚗 Car Price Estimator (Machine Learning + Flask)

An end-to-end **Machine Learning Web Application** that predicts the price of a used car based on user inputs such as company, model, year, fuel type, and kilometers driven.

This project demonstrates how to **build, train, and deploy an ML model** using a clean UI and a Flask backend.

---

# 🌟 Features

* 🔍 Predicts car price instantly based on user inputs
* 🎯 Machine Learning model trained on real-world dataset
* ⚡ Fast and interactive UI with dynamic dropdowns
* 🔄 No page reload prediction using AJAX
* 🎨 Modern responsive frontend design
* 🧠 Smart preprocessing using pipelines

---

# 🛠️ Tech Stack

### 👨‍💻 Backend

* **Python** – Core programming language
* **Flask** – Lightweight web framework for deployment

### 📊 Machine Learning

* **Jupyter Notebook** – Model building, experimentation, and training
* **Scikit-learn** – ML model training and preprocessing

### 🎨 Frontend

* HTML5
* CSS3 (Modern UI + Glassmorphism)
* JavaScript (Dynamic dropdown + AJAX)

---

# 🤖 Machine Learning Pipeline

The project uses a clean and efficient **ML pipeline approach**:

* Data preprocessing
* Encoding categorical variables
* Model training
* Prediction

---

# 📦 Libraries Used

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
```

### 📌 One-Line Description of Each Library

* **LinearRegression** → Used to build a regression model that predicts continuous car prices
* **r2_score** → Evaluates how well the model fits the data (accuracy metric)
* **OneHotEncoder** → Converts categorical features (like company, fuel type) into numerical format
* **make_column_transformer** → Applies different transformations to different columns efficiently
* **make_pipeline** → Combines preprocessing and model training into a single workflow

---

# ⚙️ How It Works

1. User selects:

   * Company
   * Model
   * Year
   * Fuel Type
   * Kilometers Driven

2. Data is sent to Flask backend

3. Backend:

   * Processes input
   * Applies preprocessing pipeline
   * Predicts price using trained model

4. Result is displayed instantly on UI

---

# 📁 Project Structure

```
Car-Price-Predictor/
│
├── templates/
│   └── index.html
│
├── static/
│   └── styles.css
│
├── Notebook/
│   └── LinearRegressionModel.pkl
|   └── Price_Predictor_Model.ipynb
│
├── app.py
└── README.md
```

---

# 🚀 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/car-price-predictor.git
cd car-price-predictor
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Flask app

```bash
python app.py
```

### 4️⃣ Open in browser

```
http://127.0.0.1:5000/
```

---

# 📊 Model Performance

* Model Used: **Linear Regression**
* Evaluation Metric: **R² Score**
* Achieves good accuracy for predicting used car prices

---

# 🔥 Future Enhancements

* 🚀 Use advanced models (Random Forest, XGBoost)
* 📈 Add model comparison dashboard
* 🌐 Deploy on cloud (AWS / Azure / Render)
* 📊 Add data visualization charts
* 🤖 Auto-fill dependent dropdowns (Company → Model → Fuel)

---

# ScreenShots (UI)
![alt text](<./static/Screenshot 2026-04-16 191023.png>) 

![alt text](<./static/Screenshot 2026-04-16 191006.png>)

---

# 🙌 Conclusion

This project showcases the complete lifecycle of a Machine Learning application:

➡ Data preprocessing
➡ Model training
➡ Development using Flask
➡ Interactive UI integration

It is a perfect example of combining **Data Science + Web Development** into a real-world application.

---

# ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!

---
