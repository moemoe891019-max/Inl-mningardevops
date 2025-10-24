import psutil


class Monitor:
    """Läser systemvärden från datorn"""

    def get_all_values(self):
        """Returnerar alla systemvärden - procent och GB"""
        mem = psutil.virtual_memory()
        disk = psutil.disk_usage("/")

        return {
            # För alarmen
            "cpu": psutil.cpu_percent(interval=1),
            "memory": mem.percent,
            "disk": disk.percent,
            # För VAL 2 visning
            "memory_used_gb": mem.used / (1024**3),
            "memory_total_gb": mem.total / (1024**3),
            "disk_used_gb": disk.used / (1024**3),
            "disk_total_gb": disk.total / (1024**3),
        }


if __name__ == "__main__":
    monitor = Monitor()
    values = monitor.get_all_values()
    print(values)
