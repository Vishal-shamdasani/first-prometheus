# Flask Prometheus App

## Overview

This Flask application serves as a demonstration of integrating Flask with Prometheus for monitoring and metrics collection. It provides basic endpoints and exposes metrics for monitoring application performance and behavior.

## Features

- **Flask Framework**: A lightweight WSGI web application framework.
- **Prometheus Integration**: Collect and expose metrics to Prometheus.
- **Sample Endpoints**: Demonstrates how to create basic API endpoints.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher
- Flask
- Prometheus Client

You can install the required packages using the following command:

```bash
pip install Flask prometheus_client
```
Installation
Clone the repository:

```bash
git clone https://github.com/Vishal-shamdasani/first-prometheus.git
cd flask-prometheus-app
```
Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```
Install the dependencies:

```bash
pip install Flask prometheus_client
```
Configuration
Prometheus Configuration
A sample Prometheus configuration file (prometheus.yml) is included in this repository. Make sure to configure Prometheus to scrape metrics from your Flask application by adding the following configuration to your prometheus.yml file:

```yaml
scrape_configs:
  - job_name: 'flask-prometheus-app'
    static_configs:
      - targets: ['localhost:8081']
```
Usage
Run the application:

```bash
python app.py
```
Access the application:

Open your web browser and navigate to http://localhost:5000.

Access the Prometheus metrics:

The metrics can be accessed at http://localhost:8081/metrics.

Endpoints
GET /: Returns a simple greeting message.
GET /metrics: Exposes application metrics for Prometheus.
Example Metrics
Once Prometheus scrapes the metrics, you can expect to see metrics like:

flask_http_requests_total: Total number of HTTP requests.
flask_http_request_duration_seconds: Duration of HTTP requests.
Running Prometheus
To run Prometheus, follow these steps:

Download Prometheus from the official website.

Unzip and navigate to the directory.

Run Prometheus with the provided configuration:

```bash
./prometheus --config.file=prometheus.yml
```
Open your web browser and navigate to http://localhost:9090 to view the Prometheus dashboard.

Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request.
