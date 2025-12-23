# system_monitor.py
import psutil 
import json
from datetime import datetime
import requests

def get_system_metrics():
    return{
        "timestamp": str(datetime.now()),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent
    }

def log_metrics(metrics, filename = "system_metrics.log"):
    with open(filename, 'a') as f:
        f.write(json.dumps(metrics) + "\n")

def send_slack_alert(message):
    webhook_url = "https://hooks.slack.com/services/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"
    payload = {"text": message}
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    metrics = get_system_metrics()
    print(f"Current Metrics: {metrics}")
    log_metrics(metrics)

    # Alert message sent to Slack if CPU > 90%
    if metrics["cpu_usage"] > 90:
        send_slack_alert(f"🚨🚨 HIGH CPU : {metrics['cpu_usage']}%")