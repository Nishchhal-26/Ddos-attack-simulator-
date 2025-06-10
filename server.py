from flask import Flask, request
import time
import logging

app = Flask(__name__)

# Logging setup (logs to file)
logging.basicConfig(filename="logs/server_log.txt", level=logging.INFO)

@app.route("/")
def home():
    ip = request.remote_addr
    timestamp = time.ctime()
    logging.info(f"Request from {ip} at {timestamp}")
    return "Server is running"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
