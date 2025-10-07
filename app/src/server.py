from flask import Flask, request
import os
# NEW
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQ_COUNT = Counter("web_requests_total","Total HTTP requests",["path","method","code"])
REQ_LATENCY = Histogram("web_request_latency_seconds","Request latency seconds",["path"])

@app.get("/")
def root():
    color = os.getenv("APP_COLOR", "blue")
    return f"Hello from {color} deployment!"

# NEW: expose metrics
@app.get("/metrics")
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

# Basic per-request metrics hook
@app.after_request
def after(resp):
    try:
        path = request.path
        method = request.method
        code = resp.status_code
        REQ_COUNT.labels(path=path, method=method, code=code).inc()
    finally:
        return resp
