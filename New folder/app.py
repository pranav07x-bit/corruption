from flask import Flask, render_template

from ai.anomaly_detector import detect_anomalies
from ai.network_analysis import build_network, find_suspicious_nodes

app = Flask(__name__)

@app.route("/")

def dashboard():

    contracts = detect_anomalies()

    build_network()

    suspicious = find_suspicious_nodes()

    return render_template(
        "dashboard.html",
        tables=[contracts.to_html(classes="data")],
        suspicious=suspicious
    )


if __name__ == "__main__":
    app.run(debug=True)