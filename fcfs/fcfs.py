n = int(input("Enter the number of processes = "))
processes = []
arrival_time = []
burst_time = []

#Input process details
for i in range(n):
    process = int(input(f"Enter Process ID (e.g., {i+1}): "))
    at = int(input(f"Enter Arrival Time for {process}: "))
    bt = int(input("Enter Burst Time for {process}: "))
    processes.append(process)
    arrival_time.append(at)
    burst_time.append(bt)


combined = list(zip(processes, arrival_time, burst_time))    # [('P2', 2, 3), ('P1', 0, 5), ('P3', 1, 4)]
combined.sort(key=lambda x: x[1])   # Sort According to Arrival time     [('P1', 0, 5),  ('P3', 1, 4), ('P2', 2, 3)]
processes, arrival_time, burst_time = zip(*combined)   # Separate the List Again   processes = [P1, P2, P3], arrival_time = [0, 1, 2], burst_time = [5, 4, 3]

# Records the process executing at each CPU time unit
execution_timeline = []
# Records the order in which processes complete
completion_order = []
completion_time = []
turnaround_time = []
waiting_time = []
idle_time = 0
current_time = 0

# Calculate Completion Time
for i in range(n):
    # CPU Idle
    # Checks whether the CPU has reached the arrival time of the next process
    while current_time < arrival_time[i]:
        execution_timeline.append("Idle")
        idle_time += 1
        current_time += 1

    for _ in range(burst_time[i]):
        execution_timeline.append(f"P{processes[i]}")

    current_time += burst_time[i]
    completion_time.append(current_time)

    completion_order.append(f"P{processes[i]}")


# Calculate TAT, WT and its Average
for i in range(n):
    tat = completion_time[i] - arrival_time[i]
    wt = tat - burst_time[i]
    turnaround_time.append(tat)
    waiting_time.append(wt)

avg_tat = sum(turnaround_time) / n
avg_wt = sum(waiting_time) / n


print("\nFSFC Scheduling Result")
print("-" * 46)

schedule_length = max(completion_time) - min(arrival_time)
print(f"{'Process':<10}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<8}{'WT':<8}")
print("-" * 46)

for i in range(n):
    print(f"{processes[i]:<10}{arrival_time[i]:<8}{burst_time[i]:<8}{completion_time[i]:<8}{turnaround_time[i]:<8}{waiting_time[i]:<8}")

print("-" * 46)

print("\nExecution Timeline:")

for process in execution_timeline:
    print(process, end=" -> ")

print("END\n")

print("\nCompletion Order:")

for process in completion_order:
    print(process, end=" -> ")

print("END\n")

print(f"Average Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
print(f"Schedule Length = {schedule_length:.2f}")
print(f"Total CPU Idle Time : {idle_time}")
