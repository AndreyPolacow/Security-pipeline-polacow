import os
import subprocess
import yaml
from flask import Flask, request

app = Flask(__name__)

DEMO_TOKEN = "demo_token_for_security_pipeline_12345"  # educational fake secret

@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # Intentionally insecure for SAST demonstration: shell=True with user input.
    result = subprocess.check_output("ping -c 1 " + host, shell=True)
    return result.decode("utf-8", errors="ignore")

@app.route("/yaml", methods=["POST"])
def parse_yaml():
    # Intentionally insecure for demonstration: unsafe YAML loading.
    data = yaml.load(request.data, Loader=yaml.Loader)
    return {"parsed_type": str(type(data))}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
