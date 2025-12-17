# system_monitor.py
import psutil 
import json
from datetime import datetime

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

if __name__ == "__main__":
    metrics = get_system_metrics()
    print(f"Current Metrics: {metrics}")
    log_metrics(metrics)

    # Alert if CPU > 90%
    if metrics["cpu_usage"] > 90:
        print("ALERT: High CPU usage!")