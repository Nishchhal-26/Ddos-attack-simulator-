import psutil
import time

print("Monitoring system performance...")
for _ in range(10):
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"CPU: {cpu}% | Memory: {memory}%")
