import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, median_absolute_error, max_error, explained_variance_score
from xgboost import XGBRegressor
import mlflow
import mlflow.sklearn
import mlflow.xgboost
import matplotlib.pyplot as plt
import seaborn as sns
import os
import time

def mean_absolute_percentage_error(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / (y_true + 1e-10))) * 100

def max_absolute_error(y_true, y_pred):
    return np.max(np.abs(y_true - y_pred))

def train_and_log_model(model, model_name, X_train, X_test, y_train, y_test, feature_names, params=None):
    with mlflow.start_run(run_name=model_name):
        start = time.time()
        end = time.time()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))
        mae = mean_absolute_error(y_test, y_pred)
        mape = mean_absolute_percentage_error(y_test, y_pred)
        explained_var = explained_variance_score(y_test, y_pred)
        medae = median_absolute_error(y_test, y_pred)
        maxae = max_absolute_error(y_test, y_pred)
        max_err = max_error(y_test, y_pred)
        training_time = end - start
        
        
        mlflow.log_param("model_type", model_name)
        if params:
            for key, value in params.items():
                mlflow.log_param(key, value)
        
        mlflow.log_metric("r2_score", r2)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("mae", mae)
        mlflow.log_metric("mape", mape)
        mlflow.log_metric("explained_variance", explained_var)
        mlflow.log_metric("median_absolute_error", medae)
        mlflow.log_metric("max_absolute_error", maxae)
        mlflow.log_metric("Max_Error", max_err)
        mlflow.log_metric("Training_Time", training_time)
        
        # Prepare input example for model signature
        input_example = X_train[:5]
        
        if model_name.startswith("XGBoost"):
            mlflow.xgboost.log_model(model, model_name, input_example=input_example)
        else:
            mlflow.sklearn.log_model(model, model_name, input_example=input_example)
        
        plot_dir = "Membangun_model/Actual VS Predicted Graph"
        os.makedirs(plot_dir, exist_ok=True)
        plot_path = os.path.join(plot_dir, f"{model_name}_prediksi.png")
        
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=y_test, y=y_pred)
        plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
        plt.xlabel('Actual')
        plt.ylabel('Predicted')
        plt.title(f'Predicted vs Actual ({model_name})')
        plt.savefig(plot_path)
        mlflow.log_artifact(plot_path)
        plt.close()
        
        if model_name in ["Random Forest Tuned", "XGBoost Tuned"]:
            plt.figure(figsize=(10, 6))
            importances = model.feature_importances_
            indices = np.argsort(importances)[::-1]
            sns.barplot(x=importances[indices], y=np.array(feature_names)[indices])
            plt.title(f'Feature Importance ({model_name})')
            plt.tight_layout()
            feat_imp_path = os.path.join(plot_dir, f"{model_name}_feature_importance.png")
            plt.savefig(feat_imp_path)
            mlflow.log_artifact(feat_imp_path)
            plt.close()
        
        print(f"{model_name} - R²: {r2:.4f}, RMSE: {rmse:.4f}, MAE: {mae:.4f}, MAPE: {mape:.4f}, Explained Variance: {explained_var:.4f}, MedAE: {medae:.4f}, MaxAE: {maxae:.4f}")

def main():
    # Setup DagsHub MLflow tracking
    tracking_uri = 'https://dagshub.com/covryzne/Eksperimen_SML_ShendiTeukuMaulanaEfendi.mlflow'
    username = 'covryzne'
    token = os.getenv('DAGSHUB_TOKEN')
    
    if not token:
        raise ValueError("DAGSHUB_TOKEN environment variable is not set. Please set it in GitHub Secrets or environment.")
    
    os.environ['MLFLOW_TRACKING_URI'] = tracking_uri
    os.environ['MLFLOW_TRACKING_USERNAME'] = username
    os.environ['MLFLOW_TRACKING_PASSWORD'] = token
    
    mlflow.set_tracking_uri(tracking_uri)
    
    # For local testing, uncomment below and comment DagsHub settings
    # mlflow.set_tracking_uri("http://localhost:5000")
    
    mlflow.set_experiment("Student_Performance_Prediction")
    
    df = pd.read_csv('Membangun_model/student_habits_preprocessing.csv')
    
    X = df.drop('exam_score', axis=1)
    y = df['exam_score']
    feature_names = X.columns.tolist()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    lr_model = LinearRegression()
    train_and_log_model(lr_model, "Linear Regression", X_train, X_test, y_train, y_test, feature_names)
    
    rf_param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [5, 10, None]
    }
    rf_model = RandomForestRegressor(random_state=42)
    rf_grid = GridSearchCV(rf_model, rf_param_grid, cv=5, scoring='r2')
    rf_grid.fit(X_train, y_train)
    train_and_log_model(rf_grid.best_estimator_, "Random Forest Tuned", X_train, X_test, y_train, y_test, feature_names, rf_grid.best_params_)
    
    xgb_param_grid = {
        'n_estimators': [50, 100, 200],
        'learning_rate': [0.01, 0.1, 0.3]
    }
    xgb_model = XGBRegressor(random_state=42)
    xgb_grid = GridSearchCV(xgb_model, xgb_param_grid, cv=5, scoring='r2')
    xgb_grid.fit(X_train, y_train)
    train_and_log_model(xgb_grid.best_estimator_, "XGBoost Tuned", X_train, X_test, y_train, y_test, feature_names, xgb_grid.best_params_)

if __name__ == "__main__":
    main()