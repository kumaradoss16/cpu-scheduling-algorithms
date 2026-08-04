class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time

        self.waiting_time = 0
        self.turnaround_time = 0
        self.completion_time = 0
        self.response_ratio = 0


def hrrn(processes):
    current_time = 0
    completed = 0
    n = len(processes)

    execution_order = []
    completion_order = []

    cpu_idle_time = 0

    print("-" * 45)
    print(f"{'Time':<8}{'Process':<10}{'Response Ratio'}")
    print("-" * 45)

    while completed < n:
        ready_queue = []

        # Find all ready processes
        for process in processes:
            if process.arrival_time <= current_time and process.completion_time == 0:
                waiting_time = current_time - process.arrival_time
                process.response_ratio = (waiting_time + process.burst_time) / process.burst_time
                ready_queue.append(process)

        # CPU Idle
        if not ready_queue:
            execution_order.append(f"Idle({current_time} - {current_time + 1}")
            cpu_idle_time += 1
            current_time += 1
            continue

        # Select Highest Response Ratio
        selected = max(ready_queue, key=lambda p: p.response_ratio)

        print(f"{current_time:<8} {selected.pid:10} {selected.response_ratio:.2f}")

        execution_order.append(f"{selected.pid}({current_time}-{current_time + selected.burst_time})")

        current_time += selected.burst_time

        selected.completion_time = current_time
        selected.turnaround_time = (selected.completion_time - selected.arrival_time)
        selected.waiting_time = (selected.turnaround_time - selected.burst_time)
        completion_order.append(selected.pid)

        completed += 1

    print("\nFinal Result")
    print("-" * 45)
    print(f"{'PID':<6}{'AT':<6}{'BT':<6}{'CT':<6}{'TAT':<8}{'WT':<8}")
    print("-" * 45)

    total_wt = 0
    total_tat = 0

    for process in sorted(processes, key=lambda p: p.pid):
        total_wt += process.waiting_time
        total_tat += process.turnaround_time

        print(f"{process.pid:<6}"
              f"{process.arrival_time:<6}"
              f"{process.burst_time:<6}"
              f"{process.completion_time:<6}"
              f"{process.turnaround_time:<8}"
              f"{process.waiting_time:<8}")
    print("-" * 45)

    print(f"Average Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")

    print(f"\nExecution Order: {' -> '.join(execution_order)}")
    print(f"Completion Order: {' -> '.join(completion_order)}")
    print(f"CPU Idle Time: {cpu_idle_time}")

    total_time = max(p.completion_time for p in processes)

    cpu_utilization = ((total_time - cpu_idle_time) / total_time) * 100
    print(f"CPU Utilization: {cpu_utilization:.2f}%")

# -----------------------
# Driver Code
# -----------------------

processes = [
    Process("P1", 0, 3),
    Process("P2", 2, 6),
    Process("P3", 4, 4),
    Process("P4", 6, 5),
    Process("P5", 8, 2),
]

hrrn(processes)
