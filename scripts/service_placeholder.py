import os
import time

service_name = os.getenv("SERVICE_NAME", "unknown")
print(f"Tapetum Sentinel placeholder service started: {service_name}", flush=True)
while True:
    time.sleep(3600)
