n = int(input("Enter the number of processes: "))

processes = []

for i in range(n):
    pid = input(f"Enter Process ID for Process {i+1}: ")
    at = int(input(f"Enter Arrival Time for P{pid}: "))
    bt = int(input(f"Enter Burst Time for P{pid}: "))

    processes.append(
        {
            "pid": f"P{pid}",
            "at": at,
            "bt": bt,
            "rt": bt
        }
    )

# Records the process executing at each CPU time unit
execution_timeline = []
# Records the order in which processes complete
completion_order = []
current_time = 0
completed = 0
idle_time = 0

while completed < n:
    index = -1
    minimum_rt = float('inf')
    for i in range(n):
        """
        Check whether the process:
        1. Has already arrived and
        2. Still has remaining execution time and
        3. Has the shortest remaining time among all available processes
        """
        if (processes[i]["at"] <= current_time and 
            processes[i]["rt"] > 0 and
            processes[i]["rt"] < minimum_rt
            ):

            minimum_rt = processes[i]["rt"]
            index = i  # Store the currently selected process

    # CPU Idle
    if index == -1:
        idle_time += 1
        current_time += 1
        continue

    execution_timeline.append(processes[index]["pid"])

    processes[index]["rt"] -= 1
    current_time += 1

    # Process completed
    if processes[index]["rt"] == 0:
        completed += 1

        ct = current_time
        tat = ct - processes[index]["at"]
        wt = tat - processes[index]["bt"]

        processes[index]["ct"] = ct
        processes[index]["tat"] = tat
        processes[index]["wt"] = wt
        completion_order.append(processes[index]["pid"])

# Output
print("\nSRJF Scheduling Result")
print("-" * 46)
print(f"{'PID':<10}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<10}{'WT':<8}")
print("-" * 46)
schedule_length = max(process["ct"] for process in processes) - min(process["at"] for process in processes)

total_tat = 0
total_wt = 0

for process in processes:
    total_tat += process["tat"]
    total_wt += process["wt"]
    

    print(f"{process['pid']:<10}{process['at']:<8}{process['bt']:<8}{process['ct']:<8}{process['tat']:<10}{process['wt']:<8}")
    
print("-" * 46)

print("\nExecution Timeline:")

for process in execution_timeline:
    print(process, end=" -> ")

print("END\n")

print("\nCompletion Order:")

for process in completion_order:
    print(process, end=" -> ")

print("END\n")


print(f"Average Turnaround Time: {total_tat / n:.2f}")
print(f"Average Waiting Time: {total_wt / n:.2f}")
print(f"Schedule Length = {schedule_length:.2f}")
print(f"Total CPU Idle Time : {idle_time}")
