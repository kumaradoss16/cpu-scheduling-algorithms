# Priority Scheduling (Non-Preemptive)

n = int(input("Enter the number of processes: "))

processes = []

for i in range(n):
    pid = input(f"\nEnter Process ID for Process {i + 1}: ")
    at = int(input(f"Enter Arrival Time for {pid}: "))
    bt = int(input(f"Enter Burst Time for {pid}: "))
    pr = int(input("Priority (Smaller number = Higher Priority): "))

    processes.append({
        "pid": pid,
        "at": at,
        "bt": bt,
        "priority": pr
    })

current_time = 0
completed = 0
idle_time = 0
execution_order = []

while completed < n:
    # Find all processes that have arrived and are not completed
    ready_queue = [
        p for p in processes
        if p["at"] <= current_time and "completed" not in p
    ]

    if ready_queue:

        # Select highest priority process
        ready_queue.sort(key=lambda x: (x["priority"], x["at"]))

        process = ready_queue[0]

        process["start"] = current_time
        process["ct"] = current_time + process["bt"]
        process["tat"] = process["ct"] - process["at"]
        process["wt"] = process["tat"] - process["bt"]

        current_time = process["ct"]
        process["completed"] = True
        completed += 1

        execution_order.append(process["pid"])
    else:
        idle_time += 1
        current_time += 1

print("\nExecution Order")
print("-" * 55)
print(" -> ".join(execution_order))


print("\nPriority Scheduling Results:")
print("-" * 55)

print(
    f"{'PID':<8}{'AT':<8}{'BT':<8}{'PR':<8}{'CT':<8}{'TAT':<8}{'WT':<8}"
)

print("-" * 55)

total_tat = 0
total_wt = 0

for p in sorted(processes, key=lambda x: x["ct"]):
    total_tat += p["tat"]
    total_wt += p["wt"]

    print(
        f"{p['pid']:<8}{p['at']:<8}{p['bt']:<8}{p['priority']:<8}{p['ct']:<8}{p['tat']:<8}{p['wt']:<8}"
    )

print("-" * 55)

print(f"Average Turnaround Time: {total_tat / n:.2f}")
print(f"Average Waiting Time: {total_wt / n:.2f}")
print(f"CPU Idle Time: {idle_time}")
