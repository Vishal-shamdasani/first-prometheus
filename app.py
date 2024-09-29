from flask import Flask
from prometheus_client import start_http_server, Counter

app = Flask(__name__)

REQUESTS = Counter('app_requests_total', 'Total web app requests')

@app.route('/')
def homepage():
    REQUESTS.inc()  
    return "Hello, Prometheus!"

if __name__ == '__main__':
    start_http_server(8081)  
    app.run(host='0.0.0.0', port=5000,debug=True) 