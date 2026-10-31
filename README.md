# MLflow Model Deployment — House Price Prediction

## Project Overview

An end-to-end Machine Learning and MLOps project demonstrating experiment tracking, model evaluation, model registration, and REST API deployment using MLflow.

The project predicts California housing prices using machine learning models and provides a Streamlit dashboard for making predictions.

## Technologies Used

- Python
- Scikit-learn
- MLflow Tracking
- MLflow Model Registry
- MLflow Model Serving
- Streamlit
- Jupyter Notebook
- SQLite
- REST API

## Machine Learning Models

Three regression models were trained and evaluated:

| Model | RMSE | MAE | R² |
|---|---:|---:|---:|
| Linear Regression | 70,059 | 50,670 | 0.63 |
| Random Forest | 49,379 | 32,187 | 0.81 |
| Gradient Boosting | 47,388 | 31,379 | 0.83 |

**Best Model:** Gradient Boosting

The selected model was registered in MLflow as `house-price-model` with the alias `champion`.

## Project Workflow

1. Load and preprocess the California Housing dataset.
2. Split the dataset into training and testing sets.
3. Train and evaluate three regression models.
4. Track experiments, parameters, metrics, and artifacts using MLflow.
5. Register the best-performing model in the MLflow Model Registry.
6. Serve the registered model using MLflow's REST API.
7. Make predictions through a Streamlit dashboard.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/swayamsv/mlflow-house-price-prediction.git
cd mlflow-house-price-prediction
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Train and register the model

Open `House_Price_Deployment_Project.ipynb` in Jupyter or VS Code and execute the training and registration cells.

### 5. Start MLflow Tracking UI

```bash
mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5000 --workers 1
```

Open `http://127.0.0.1:5000`.

### 6. Start MLflow Model Serving

```bash
mlflow models serve -m "models:/house-price-model@champion" -p 5001 --env-manager local
```

### 7. Launch the Streamlit Dashboard

In another terminal:

```bash
streamlit run app.py
```

Open `http://localhost:8501`.

### 8. Test the API

```bash
python test_api.py
```

## Results

Gradient Boosting achieved the best performance, with an R² score of approximately 0.83 and an RMSE of approximately $47,388.

## Team

**Group 1 — MBA Tech (Data Science), NMIMS University**

- Swayam Vishwakarma
- Pashin Irani
- Anant Shukla

## Future Scope

- Deploy the application to a cloud platform.
- Containerize the model using Docker.
- Introduce automated model retraining and monitoring.