import os
from flask import Flask, jsonify, request
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = Flask(__name__)
VERSION = os.getenv("APP_VERSION", "dev")
REQUESTS = Counter("http_requests_total", "Total HTTP requests", ["path", "status"])

@app.after_request
def count_request(response):
    if request.path != "/metrics":
        REQUESTS.labels(request.path, str(response.status_code)).inc()
    return response

@app.get("/")
def index():
    return jsonify(message="hello", version=VERSION)

@app.get("/healthz")
def healthz():
    return jsonify(status="ok")

@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}
