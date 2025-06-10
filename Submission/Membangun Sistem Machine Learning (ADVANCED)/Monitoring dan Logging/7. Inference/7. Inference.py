import requests
import json

url = "http://127.0.0.1:5000/invocations"
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
                1.08466511356851485, 1, -0.034124455322227, -0.3460384652906983, -0.3905712449640047,
                0, -0.2056193139364664, 1.0033746874766687, 0, -1.0086889326553974, 1, 1,
                -0.8566176328503455, 0, 0.0691763150071329, 1
            ]
        ]
    }
}

response = requests.post(url, json=data)
print(response.json())