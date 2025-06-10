from prometheus_client import start_http_server, Counter, Gauge, Histogram
import time
import random
import requests
import json
import psutil  # Install: pip install psutil
import numpy as np

# Inisialisasi metrik
request_count = Counter('model_requests_total', 'Total requests to model')
prediction_latency = Histogram('model_prediction_latency_seconds', 'Prediction latency in seconds')
error_count = Counter('model_errors_total', 'Total errors in predictions')
success_rate = Gauge('model_success_rate', 'Success rate of predictions')
cpu_usage = Gauge('model_cpu_usage_percent', 'CPU usage percentage')
memory_usage = Gauge('model_memory_usage_percent', 'Memory usage percentage')
prediction_value = Gauge('model_prediction_value', 'Predicted productivity ratio')
study_hours_mean = Gauge('model_study_hours_mean', 'Mean study hours per day from input')
sleep_hours_mean = Gauge('model_sleep_hours_mean', 'Mean sleep hours from input')
response_time = Histogram('model_response_time_seconds', 'Response time in seconds')

# Fungsi buat kirim request ke model
def send_request_to_model():
    url = "http://127.0.0.1:5000/invocations"
    # Simulasi input mirip serving_input_example.json
    data = {
        "dataframe_split": {
            "columns": [
                "age", "gender", "study_hours_per_day", "social_media_hours", "netflix_hours",
                "part_time_job", "attendance_percentage", "sleep_hours", "diet_quality",
                "exercise_frequency", "parental_education_level", "internet_quality",
                "mental_health_rating", "extracurricular_participation", "productivity_ratio",
                "sleep_category"
            ],
            "data": [
                [
                    random.uniform(-2, 2),  # age (normalized)
                    random.choice([0, 1]),  # gender
                    random.uniform(-2, 2),  # study_hours_per_day (normalized)
                    random.uniform(-2, 2),  # social_media_hours
                    random.uniform(-2, 2),  # netflix_hours
                    random.choice([0, 1]),  # part_time_job
                    random.uniform(-2, 2),  # attendance_percentage
                    random.uniform(-2, 2),  # sleep_hours
                    random.choice([-1, 0, 1]),  # diet_quality
                    random.uniform(-2, 2),  # exercise_frequency
                    random.choice([0, 1, 2]),  # parental_education_level
                    random.choice([0, 1, 2]),  # internet_quality
                    random.uniform(-2, 2),  # mental_health_rating
                    random.choice([0, 1]),  # extracurricular_participation
                    random.uniform(0, 1),  # productivity_ratio
                    random.choice([0, 1, 2])  # sleep_category
                ]
            ]
        }
    }
    start_time = time.time()
    try:
        response = requests.post(url, json=data)
        latency = time.time() - start_time
        response_time.observe(latency)
        prediction_latency.observe(latency)
        request_count.inc()
        if response.status_code == 200:
            success_rate.set(1.0)
            prediction = response.json().get('predictions', [0])[0]
            prediction_value.set(prediction)
            study_hours_mean.set(data['dataframe_split']['data'][0][2])  # study_hours_per_day
            sleep_hours_mean.set(data['dataframe_split']['data'][0][7])  # sleep_hours
        else:
            error_count.inc()
            success_rate.set(0.0)
    except:
        error_count.inc()
        success_rate.set(0.0)

# Fungsi buat metrik sistem
def collect_system_metrics():
    cpu_usage.set(psutil.cpu_percent())
    memory_usage.set(psutil.virtual_memory().percent)

# Main loop
if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus metrics server running on port 8000")
    while True:
        send_request_to_model()
        collect_system_metrics()
        time.sleep(1)