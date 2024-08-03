from prometheus_client import start_http_server, Gauge
import psutil
import time

# Create a Gauge metric to track CPU usage
cpu_usage_gauge = Gauge('cpu_usage', 'CPU Usage in percentage')

def collect_cpu_usage():
    while True:
        # Get the current CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)
        # Set the Gauge metric to the current CPU usage
        cpu_usage_gauge.set(cpu_usage)
        # Sleep for a second before the next collection
        time.sleep(1)

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)
    # Start collecting CPU usage
    collect_cpu_usage()
