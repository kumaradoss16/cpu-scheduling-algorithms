n = int(input("Enter the number of processes = "))
processes = []
arrival_time = []
burst_time = []

#Input process details
for i in range(n):
    process = int(input(f"Enter Process ID (e.g., P{i+1}): "))
    at = int(input(f"Enter Arrival Time for Process {process}: "))
    bt = int(input(f"Enter Burst Time for Process {process}: "))
    processes.append(process)
    arrival_time.append(at)
    burst_time.append(bt)


combined = list(zip(processes, arrival_time, burst_time))    # [('P2', 2, 3), ('P1', 0, 5), ('P3', 1, 4)]
combined.sort(key=lambda x: x[1])   # Sort According to Arrival time     [('P1', 0, 5),  ('P3', 1, 4), ('P2', 2, 3)]
processes, arrival_time, burst_time = zip(*combined)   # Separate the List Again   processes = [P1, P2, P3], arrival_time = [0, 1, 2], burst_time = [5, 4, 3]

completion_time = []
turnaround_time = []
waiting_time = []
start_time = []
total_idle = 0

current_time = 0

# Calculate Start and Completion Time
for i in range(n):
    # CPU idle
    if current_time < arrival_time[i]:
        total_idle += arrival_time[i] - current_time
        current_time = arrival_time[i]

    # Execute Process
    current_time += burst_time[i]
    #Store Completion Time
    completion_time.append(current_time)

# Calculate TAT, WT and its Average
for i in range(n):
    tat = completion_time[i] - arrival_time[i]
    wt = tat - burst_time[i]
    turnaround_time.append(tat)
    waiting_time.append(wt)

avg_tat = sum(turnaround_time) / n
avg_wt = sum(waiting_time) / n
schedule_length = max(completion_time) - min(arrival_time)


print("\nFSFC Scheduling Result")
print("-" * 45)
print(f"{'Process':<10}{'AT':<8}{'BT':<8}{'CT':<8}{'TAT':<8}{'WT':<8}")
print("-" * 45)

for i in range(n):
    print(f"{processes[i]:<10}{arrival_time[i]:<8}{burst_time[i]:<8}{completion_time[i]:<8}{turnaround_time[i]:<8}{waiting_time[i]:<8}")

print("-" *45)
print(f"Average Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")
print(f"Total CPU Idle Time: {total_idle:.2f}")
print(f"Schedule Length = {schedule_length:.2f}")

