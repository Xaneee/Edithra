import psutil
import time
import logging

logging.basicConfig(
    filename="Edithra/logs/system_monitor.log",
    filemode="a",
    format="%(asctime)s - CPU: %(cpu)s%% - RAM: %(ram)s%%",
    level=logging.INFO
)

def monitor_system():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent
        logging.info(f"CPU: {cpu_usage}% - RAM: {ram_usage}%")
        time.sleep(5)


