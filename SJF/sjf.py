n = int(input("Enter the number of Processes: "))
processes = []

for i in range(n):
    pid = input(f"Enter Process ID for Process {i+1}: ")
    arrival_time = int(input(f"Enter Arrival Time for P{pid}: "))
    burst_time = int(input(f"Enter Burst Time for P{pid}: "))
    processes.append(
        {
            "pid": pid,
            "at": arrival_time,
            "bt": burst_time
        }
    )

execution_order = []
current_time = 0  # CPU Time
completed = 0   # Count the finished Processes
visited = [False] * n   # Keep track of completed Processes
idle_time = 0

while completed < n:
    index = -1   # Assume no process selected
    minimum_bt = float('inf')

    for i in range(n):
        # process already arrived and must not already finished and choose shortest BT
        if(processes[i]["at"] <= current_time and not visited[i] and processes[i]["bt"] < minimum_bt):
            minimum_bt = processes[i]["bt"]
            index = i


    # CPU Idle
    if index == -1:
        idle_time += 1
        current_time += 1
        continue

    visited[index] = True


    start_time = current_time
    current_time += processes[index]["bt"]
    completion_time = current_time

    turnaround_time = completion_time - processes[index]["at"]
    waiting_time = turnaround_time - processes[index]["bt"]
    #Store Results
    processes[index]["ct"] = completion_time
    processes[index]["tat"] = turnaround_time
    processes[index]["wt"] = waiting_time
    execution_order.append(processes[index])

    completed += 1


print("\nSJF Scheduling Result")
print("-" * n * (n+2))
print(f"{'PID':<10}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<10}{'WT':<8}")
print("-" * n * (n+2))
schedule_length = max(process["ct"] for process in processes) - min(process["at"] for process in processes)

total_tat = 0
total_wt = 0

for process in execution_order:
    total_tat += process["tat"]
    total_wt += process["wt"]
    

    print(f"{process['pid']:<10}{process['at']:<8}{process['bt']:<8}{process['ct']:<8}{process['tat']:<10}{process['wt']:<8}")
    
print("-" * n * (n+2))

print("\nExecution Order:")

for process in execution_order:
    print(process["pid"], end=" -> ")

print("END\n")

print(f"Average Turnaround Time: {total_tat / n:.2f}")
print(f"Average Waiting Time: {total_wt / n:.2f}")
print(f"Schedule Length = {schedule_length:.2f}")
print(f"Total CPU Idle Time : {idle_time}")

        
