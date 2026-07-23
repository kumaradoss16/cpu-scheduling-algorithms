# First Come First Served (FCFS) Scheduling Algorithm

## Definition

**First Come First Served (FCFS)** is the simplest CPU scheduling algorithm in which the process that **arrives first in the Ready Queue is executed first**.

It follows the **FIFO (First In, First Out)** principle.

> **Simple Definition:**  
> The process that arrives first gets the CPU first.

---

# Characteristics

- Non-Preemptive Scheduling Algorithm
- Follows FIFO (Queue) order
- Simple to implement
- Fair because processes are executed in arrival order
- No starvation

---

# Working Principle

1. Processes enter the **Ready Queue**.
2. The CPU Scheduler selects the process that arrived first.
3. The Dispatcher assigns the CPU to the selected process.
4. The process runs until it completes or requests I/O.
5. After completion, the next process in the queue gets the CPU.

---

# FCFS Flow Diagram

```text
              New Process
                   │
                   ▼
              Ready Queue
        ┌─────────────────────┐
        │ P1 │ P2 │ P3 │ P4 │
        └─────────────────────┘
                   │
                   ▼
        Short-Term Scheduler
                   │
                   ▼
             Dispatcher
                   │
                   ▼
              CPU Executes
                   │
                   ▼
           Process Completes
                   │
                   ▼
          Next Process Executes
```

---

# Algorithm

```
Start

Read Number of Processes

Read Process ID, Arrival Time and Burst Time

Sort Processes according to Arrival Time

Current_Time = 0

For each Process

    If Current_Time < Arrival_Time

        Current_Time = Arrival_Time

    Start_Time = Current_Time

    Current_Time = Current_Time + Burst_Time

    Completion_Time = Current_Time

    Turnaround_Time = Completion_Time - Arrival_Time

    Waiting_Time = Turnaround_Time - Burst_Time

End For

Calculate Average Waiting Time

Calculate Average Turnaround Time

Display Result

Stop
```

---

# Example

## Process Table

| Process | Arrival Time (AT) | Burst Time (BT) |
|----------|------------------:|----------------:|
| P1 | 0 | 5 |
| P2 | 1 | 3 |
| P3 | 2 | 4 |

---

# Step 1

Processes arrive in the Ready Queue.

```text
Ready Queue

P1 → P2 → P3
```

---

# Step 2

Scheduler selects **P1** because it arrived first.

```text
CPU

↓

P1 Running
```

---

# Step 3

P1 completes.

```text
Time

0 -------- 5
```

---

# Step 4

Scheduler selects P2.

```text
Time

5 -------- 8
```

---

# Step 5

Scheduler selects P3.

```text
Time

8 -------- 12
```

---

# Gantt Chart

```text
0          5          8          12
|----------|----------|-----------|
    P1         P2          P3
```

---

# Completion Time (CT)

| Process | CT |
|----------|---:|
| P1 | 5 |
| P2 | 8 |
| P3 | 12 |

---

# Turnaround Time (TAT)

## Formula

```
TAT = Completion Time − Arrival Time
```

| Process | Calculation | TAT |
|----------|-------------|----:|
| P1 | 5 − 0 | 5 |
| P2 | 8 − 1 | 7 |
| P3 | 12 − 2 | 10 |

---

# Waiting Time (WT)

## Formula

```
WT = Turnaround Time − Burst Time
```

| Process | Calculation | WT |
|----------|-------------|---:|
| P1 | 5 − 5 | 0 |
| P2 | 7 − 3 | 4 |
| P3 | 10 − 4 | 6 |

---

# Response Time (RT)

## Formula

```
RT = Start Time − Arrival Time
```

| Process | Start Time | RT |
|----------|-----------:|---:|
| P1 | 0 | 0 |
| P2 | 5 | 4 |
| P3 | 8 | 6 |

> **Note:** In FCFS, **Response Time = Waiting Time** because the process is never preempted.

---

# Average Waiting Time

## Formula

```
Average WT = (Σ Waiting Time) / Number of Processes
```

Example:

```
= (0 + 4 + 6) / 3

= 10 / 3

= 3.33 ms
```

---

# Average Turnaround Time

## Formula

```
Average TAT = (Σ Turnaround Time) / Number of Processes
```

Example:

```
= (5 + 7 + 10) / 3

= 22 / 3

= 7.33 ms
```

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Sorting Processes | O(n log n) |
| Calculate CT | O(n) |
| Calculate TAT | O(n) |
| Calculate WT | O(n) |
| Overall | **O(n log n)** |

---

# Space Complexity

```
O(n)
```

---

# Advantages

- Simple and easy to implement.
- Fair scheduling based on arrival order.
- No starvation.
- Low scheduling overhead.

---

# Disadvantages

- High average waiting time.
- Long processes delay short processes.
- Suffers from the **Convoy Effect**.
- Poor response time for interactive systems.

---

# Convoy Effect

Suppose:

| Process | Burst Time |
|----------|-----------:|
| P1 | 20 |
| P2 | 2 |
| P3 | 1 |

Gantt Chart:

```text
0               20      22     23
|------P1-------|--P2---|--P3--|
```

The long process (**P1**) forces all short processes to wait.

This phenomenon is called the **Convoy Effect**.

---

# Real-Life Example

Imagine a ticket counter.

People arrive in this order:

```text
A → B → C → D
```

The ticket clerk serves them in exactly the same order.

No one can skip ahead.

This is exactly how **FCFS Scheduling** works.

---

# FCFS vs SJF

| Feature | FCFS | SJF |
|----------|------|-----|
| Selection | Arrival Time | Burst Time |
| Type | Non-Preemptive | Preemptive or Non-Preemptive |
| Waiting Time | Higher | Lower |
| Starvation | No | Possible |
| Complexity | Simple | Moderate |

---

# Applications

- Batch Processing Systems
- Print Queue Management
- Customer Service Queue
- Ticket Booking Systems
- Basic Operating System Scheduling

---

# Interview Questions

## 1. What is FCFS Scheduling?

**Answer:**  
FCFS (First Come First Served) is a non-preemptive CPU scheduling algorithm that executes processes in the order of their arrival.

---

## 2. Why is FCFS called FIFO?

**Answer:**  
Because the first process entering the Ready Queue is the first process to leave it for execution.

---

## 3. Is FCFS preemptive?

**Answer:**  
No. FCFS is a **non-preemptive** scheduling algorithm.

---

## 4. What is the biggest disadvantage of FCFS?

**Answer:**  
The **Convoy Effect**, where a long process delays all shorter processes behind it, increasing the average waiting time.

---

## 5. Does FCFS cause starvation?

**Answer:**  
No. Every process eventually gets CPU time because execution strictly follows the order of arrival.

---

# Summary

| Feature | Description |
|----------|-------------|
| Full Form | First Come First Served |
| Scheduling Type | Non-Preemptive |
| Queue Type | FIFO (First In, First Out) |
| Selection Criteria | Arrival Time |
| Starvation | No |
| Convoy Effect | Yes |
| Time Complexity | O(n log n) (with sorting) |
| Space Complexity | O(n) |
| Best For | Batch Processing Systems |
