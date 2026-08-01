# Round Robin Scheduling Algorithm

n = int(input("Enter the number of processes: "))

processes = []

for i in range(n):
    pid = input(f"\nEnter Process ID for Process {i + 1}: ")
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))

    processes.append(
        {
            "pid": pid,
            "at": at,
            "bt": bt,
            "remaining": bt
        }
    )

time_quantum = int(input("\nEnter Time Quantum: "))

current_time = 0
completed = 0
idle_time = 0

execution_order = []
completion_order = []

ready_queue = []
visited = set()


while completed < n:
    # Add newly arrived processes
    for p in processes:
        if p["at"] <= current_time and p["pid"] not in visited:
            ready_queue.append(p)
            visited.add(p["pid"])

    if ready_queue:
        process = ready_queue.pop(0)
        execution_order.append(process["pid"])
        execute = min(time_quantum, process["remaining"])
        process["remaining"] -= execute
        current_time += execute

        # Add newly arrived process during execution
        for p in processes:
            if p["at"] <= current_time and p["pid"] not in visited:
                ready_queue.append(p)
                visited.add(p["pid"])

        if process["remaining"] > 0:
            ready_queue.append(process)
        else:
            process["ct"] = current_time
            process["tat"] = process["ct"] - process["at"]
            process["wt"] = process["tat"] - process["bt"]

            completed += 1
            completion_order.append(process["pid"])
    else:
        current_time += 1
        idle_time += 1

print("\nExecution Order")
print("-" * 45)
print(" -> ".join(execution_order))


print("\nCompletion Order")
print("-" * 45)
print(" -> ".join(completion_order))


print("\nRound Robin Scheduling Result")
print("-" * 45)

print(
    f"{'PID':<8}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<10}{'WT':<8}"
)

print("-" * 45)

total_tat = 0
total_wt = 0

for p in sorted(processes, key=lambda x: x["ct"]):

    total_tat += p["tat"]
    total_wt += p["wt"]

    print(f"{p['pid']:<8}{p['at']:<8}{p['bt']:<8}{p['ct']:<8}{p['tat']:<10}{p['wt']:<8}")


print("-" * 45)

print(f"Average Turnaround Time: {total_tat / n:.2f}")
print(f"Average Waiting Time: {total_wt / n:.2f}")
print(f"CPU Idle Time: {idle_time}")