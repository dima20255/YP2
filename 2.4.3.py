import psutil
import time
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.data = []

    def get_cpu_usage(self):
        return psutil.cpu_percent()

    def get_memory_usage(self):
        return psutil.virtual_memory().percent

    def get_disk_usage(self):
        return psutil.disk_usage('/').percent

    def record_data(self):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        cpu = self.get_cpu_usage()
        memory = self.get_memory_usage()
        disk = self.get_disk_usage()
        self.data.append((timestamp, cpu, memory, disk))

    def display_info(self):

        print("Последние данные мониторинга:")
        for timestamp, cpu, memory, disk in self.data[-10:]:
            print(f"{timestamp} - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

monitor = SystemMonitor()
try:
    while True:
        monitor.record_data()
        monitor.display_info()
        time.sleep(1)

except KeyboardInterrupt:
    print("\nМониторинг остановлен.")
    monitor.display_info()
