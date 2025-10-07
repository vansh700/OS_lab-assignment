import os
import time
import subprocess
from multiprocessing import Process
import platform
import psutil
import sys

# ------------------- OUTPUT REDIRECTION -------------------
output_file = os.path.join(os.path.dirname(__file__), "output.txt")
f = open(output_file, "w")
sys.stdout = f  # redirect prints to file

# ------------------- TASK 1 -------------------
def child_task(index):
    print(f"[Child {index}] PID={os.getpid()}, PPID={os.getppid()}")
    time.sleep(1)

def task1_process_creation(n=3):
    print("\n--- Task 1: Process Creation ---")
    processes = []
    for i in range(n):
        p = Process(target=child_task, args=(i+1,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print("All child processes completed.\n")

# ------------------- TASK 2 -------------------
def task2_exec_commands():
    print("\n--- Task 2: Command Execution ---")

    if platform.system() == "Windows":
        commands = ["dir", "date /T", "whoami"]
    else:
        commands = ["ls", "date", "whoami"]

    for cmd in commands:
        print(f"\nExecuting: {cmd}")
        subprocess.run(cmd, shell=True)

    print("\nAll commands executed.\n")

# ------------------- TASK 3 -------------------
def child_sim():
    """Top-level function for Windows multiprocessing"""
    print(f"[Child Sim] PID={os.getpid()} running...")
    time.sleep(2)
    print("[Child Sim] Finished execution.")

def task3_simulate_zombie_orphan():
    print("\n--- Task 3: Simulated Zombie & Orphan Processes ---")
    
    if platform.system() != "Windows":
        pid = os.fork()
        if pid > 0:
            print(f"[Parent] PID={os.getpid()} (child PID={pid}) sleeping...")
            time.sleep(3)
            os.wait()
            print("[Parent] Collected child process, zombie cleared.")
        else:
            print(f"[Child] PID={os.getpid()} running...")
            time.sleep(2)
            print("[Child] Finished execution.")
    else:
        p = Process(target=child_sim)
        p.start()
        print("[Parent Sim] Sleeping while child runs (simulating zombie/orphan)...")
        time.sleep(2)
        p.join()
        print("[Parent Sim] Child process finished.\n")

# ------------------- TASK 4 -------------------
def task4_process_info():
    print("\n--- Task 4: Process Information ---")
    print(f"Current PID : {os.getpid()}")
    print(f"Parent PID  : {os.getppid()}")
    print(f"Platform    : {platform.system()}")
    print(f"Executable  : {os.path.basename(__file__)}")

    try:
        proc = psutil.Process(os.getpid())
        print(f"Memory Usage: {proc.memory_info().rss / 1024 ** 2:.2f} MB")
        print(f"CPU Times   : {proc.cpu_times()}")
    except:
        pass
    print()

# ------------------- TASK 5 -------------------
def task5_simulate_priority():
    print("\n--- Task 5: Simulated Process Prioritization ---")
    priorities = ["High Priority", "Normal Priority", "Low Priority"]
    for p in priorities:
        print(f"Running process with {p}...")
        time.sleep(1 if p=="High Priority" else 2 if p=="Normal Priority" else 3)
    print("All processes executed in simulated priority order.\n")

# ------------------- MAIN -------------------
if __name__ == "__main__":
    print("\n=== PROCESS MANAGEMENT LAB (Cross-Platform Version) ===")

    task1_process_creation()
    task2_exec_commands()
    task3_simulate_zombie_orphan()
    task4_process_info()
    task5_simulate_priority()

    print("=== LAB EXECUTION COMPLETED SUCCESSFULLY ===\n")

    f.close()  # close file
    sys.stdout = sys.__stdout__  # reset stdout
    print(f"Output written to {output_file}")