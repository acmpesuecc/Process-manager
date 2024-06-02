import psutil

def list_processes():
    print(f"{'PID':<10}{'Name':<25}{'CPU Usage (%)':<15}{'Memory Usage (%)':<15}")
    print("-" * 65)

    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent"]):
        try:

            pid = process.info["pid"]
            name = process.info["name"]
            cpu_usage = process.info["cpu_percent"]
            memory_usage = process.info["memory_percent"]

            print(f"{pid:<10}{name:<25}{cpu_usage:<15}{memory_usage:<15}")

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

list_processes()





