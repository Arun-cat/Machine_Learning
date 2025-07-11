# ❤️ Heart Disease Prediction API

This project is a **FastAPI-based machine learning API** for predicting the likelihood of heart disease. It is backed by a trained **Support Vector Classifier (SVC)** model and containerized using **Docker** for easy deployment.

---

## 🧠 Model Development & Selection

I experimented with several supervised classification models using the Heart Disease dataset. The models tested included:

- ✅ Logistic Regression  
- ✅ Random Forest Classifier  
- ✅ XGBoost  
- ✅ K-Nearest Neighbors (KNN)  
- ✅ Decision Tree Classifier  
- ✅ Support Vector Classifier (SVC)

Each model was evaluated using cross-validation, accuracy, precision, recall, and F1-score. After analysis, the **SVC model** outperformed others with better generalization and consistency across folds.

---

## 📊 Final Model Details

- **Model:** `Support Vector Classifier (SVC)`
- **Preprocessing:** Feature scaling (StandardScaler), categorical encoding (if any), cleaned data
- **Target:** Binary output (`1` = heart disease, `0` = no heart disease)

The trained model is saved using `joblib` and loaded inside the FastAPI app for inference.

---

## 📥 Expected Input Features

| Feature      | Description                                  |
|--------------|----------------------------------------------|
| `age`        | Age of the patient                           |
| `sex`        | Sex (1 = male; 0 = female)                   |
| `cp`         | Chest pain type (0–3)                        |
| `trestbps`   | Resting blood pressure                       |
| `chol`       | Serum cholesterol                            |
| `fbs`        | Fasting blood sugar > 120 mg/dl (1 = true)   |
| `restecg`    | Resting electrocardiographic results         |
| `thalach`    | Maximum heart rate achieved                  |
| `exang`      | Exercise-induced angina (1 = yes; 0 = no)    |
| `oldpeak`    | ST depression induced by exercise            |
| `slope`      | Slope of the ST segment                      |
| `ca`         | Number of major vessels (0–3)                |
| `thal`       | Thalassemia type (0 = normal, 1 = fixed, 2 = reversible) |

---

## ⚙️ How It Works

- POST your input features to the `/predict` endpoint.
- FastAPI validates your input using Pydantic.
- The API sends your data to the trained SVC model.
- The model returns whether you're at **risk of heart disease or not**.

---

## 🔗 API Endpoints

| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| GET    | `/`            | Health check              |
| POST   | `/predict`     | Predict heart disease     |

### 🧪 Sample Input:
```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 230,
  "fbs": 0,
  "restecg": 1,
  "thalach": 172,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 0,
  "thal": 1
}
