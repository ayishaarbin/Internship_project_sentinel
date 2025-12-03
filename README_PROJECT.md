Sentinel – System Log Anomaly Detection with Slack Alerts

A lightweight Python-based system that continuously monitors log files and detects anomalies using rule-based logic. When an anomaly occurs, an instant alert is sent to a Slack channel.

---

## 🚀 Features
- Real-time log monitoring
- Rule-based anomaly detection
- Automatic Slack alerts
- Configurable log path
- Clean project structure
- Easy to deploy

---

## 📁 Project Structure

Internship_Project_Sentinel/ ├── README.md ├── requirements.txt ├── config/ │   └── config.yaml ├── data/ │   └── sample_log.txt ├── logs/ │   └── app.log ├── src/ │   ├── main.py │   ├── log_reader.py │   ├── anomaly_detector.py │   ├── slack_alert.py │   └── utils.py └── tests/ └── slack_test.py

---

## 🛠 Tech Stack
- *Python*
- *Slack API (Incoming Webhooks)*
- Logging module
- YAML config handling

---

## 📦 Installation

python -m venv venv venv\Scripts\activate pip install -r requirements.txt

---

## ▶ How to Run

python src/main.py

This will start reading log files and send Slack alerts for anomalies.

---

## 🧪 Test Slack Integration

python tests/slack_test.py

---

## 📝 Sample Output

[INFO] Monitoring logs... [ANOMALY] Suspicious activity detected! Slack Alert Sent ✔

---

## 🔮 Future Enhancements
- ML-based anomaly detection
- Dashboard for visual logs
- Multiple-channel notifications (Email/SMS)
- Docker deployment

---

## 🏁 Conclusion
Sentinel is a simple, reliable, and extensible system that automates anomaly detection and provides instant alerts, helping teams respond faster to system incidents.
