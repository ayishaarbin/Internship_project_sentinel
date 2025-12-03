src/analytics/anomaly_detector.py

import os
import time
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from alerts.slack_alert import send_slack_alert

def load_model():
    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(_file_))))
    return joblib.load(os.path.join(base, "models", "log_anomaly_model.pkl"))

def preprocess(df):
    enc = LabelEncoder()
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = enc.fit_transform(df[col])
    return df

def monitor_logs():
    print("🔍 Monitoring logs for anomalies...")

    base = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(_file_))))
    log_file = os.path.join(base, "data", "sample_logs.txt")
    data_file = os.path.join(base, "data", "processed_logs.csv")

    model = load_model()
    last_size = 0

    while True:
        if os.path.exists(log_file):
            current_size = os.path.getsize(log_file)

            if current_size > last_size:
                print("📥 New log entries detected!")

                df = pd.read_csv(data_file)
                df_processed = preprocess(df)

                predictions = model.predict(df_processed)
                anomalies = df[predictions == -1]

                if not anomalies.empty:
                    print("⚠ ANOMALIES DETECTED!")
                    print(anomalies)

                    send_slack_alert(anomalies)

                last_size = current_size

        time.sleep(5)

if _name_ == "_main_":
    monitor_logs()
