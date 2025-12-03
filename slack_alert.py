import requests
import json

WEBHOOK_URL = "YOUR_WEBHOOK_URL"

def send_slack_alert(data):
    message = {
        "text": f"🚨 Anomaly Detected in Logs!\n{data}"
    }

    response = requests.post(WEBHOOK_URL, json=message)

    if response.status_code == 200:
        print("🚨 Slack Alert Sent Successfully!")
    else:
        print("❌ Failed to send alert:", response.text)
