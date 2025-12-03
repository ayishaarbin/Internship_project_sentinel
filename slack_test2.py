import requests

WEBHOOK_URL = "YOUR_WEBHOOK_URL"

data = {"text": "Test message from project"}

response = requests.post(WEBHOOK_URL, json=data)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
