from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def root():
    color = os.getenv("APP_COLOR", "blue")
    return f"Hello from {color} deployment!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
