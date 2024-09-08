import psutil

def list_processes():
    print(f"{'PID':<10}{'Name':<25}{'CPU Usage (%)':<15}{'Memory Usage (%)':<15}")
    print("-" * 65)

    system_paths = ['C:\\Windows\\System32', 'C:\\Windows\\']

    current_user = psutil.Process().username()

    processes = []

    for process in psutil.process_iter(["pid", "name", "cpu_percent", "memory_percent", "exe", "username",  "status"]):
        try:
            name = process.info["name"]
            exe_path = process.info["exe"] if process.info["exe"] else ""
            username = process.info.get("username", "")
            if process.info["status"] == psutil.STATUS_RUNNING and username == current_user and not any(exe_path.startswith(path) for path in system_paths):
                processes.append({
                    "pid": process.info["pid"],
                    "name": process.info["name"],
                    "cpu_usage": process.info["cpu_percent"],
                    "memory_usage": process.info["memory_percent"]
                })

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    processes = sorted(processes, key=lambda p: p['memory_usage'], reverse=True)

    for process in processes:
        print(f"{process['pid']:<10}{process['name']:<25}{process['cpu_usage']:<15}{process['memory_usage']:<15}")

def kill_process(pid):
    try:
        process = psutil.Process(pid)
        print(f"Terminating process {pid} ({process.name()})...");
        process.terminate()
        process.wait(timeout=3)
        print(f"Process {pid} ({process.name()}) has been terminated.")
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} does not exist.")
    except psutil.AccessDenied:
        print(f"Permission denied to terminate process with PID {pid}.")
    except psutil.TimeoutExpired:
        print(f"Process with PID {pid} did not terminate in time.")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    list_processes()
    kill_pid = int(input("Enter the PID of the process you want to terminate: "))
    kill_process(kill_pid)
except KeyboardInterrupt:
    print("\nOops! There is some interruption, this is awkward XD.")
except ValueError:
    print("Invalid PID entered. Please enter a valid PID.")
