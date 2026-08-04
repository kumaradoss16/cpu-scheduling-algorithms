# Shortest Job First (SJF) Scheduling Algorithm

## Definition

**Shortest Job First (SJF)** is a CPU scheduling algorithm that selects the process with the **smallest CPU burst time** for execution.

It aims to minimize the **average waiting time** and **average turnaround time**.

> **Simple Definition:**  
> The process with the **shortest burst time** is executed first.

---

# Characteristics

- Can be **Non-Preemptive** or **Preemptive**
- Selection is based on **Burst Time**
- Produces the minimum average waiting time (when burst times are known)
- Efficient for batch processing
- May cause starvation for long processes

---

# Types of SJF

## 1. Non-Preemptive SJF

- Once a process starts execution, it continues until completion.
- The CPU cannot interrupt the running process.

### Example

```text
Ready Queue

P1 (6 ms)
P2 (2 ms)
P3 (4 ms)

Execution Order

P2 → P3 → P1
```

---

## 2. Preemptive SJF (Shortest Remaining Time First - SRTF)

- The CPU always executes the process with the **shortest remaining burst time**.
- If a new process arrives with a shorter remaining time, the current process is interrupted.

Example:

```text
Time 0

P1 (8 ms)

↓

Time 1

P2 (4 ms) arrives

↓

P1 is interrupted

↓

CPU executes P2
```

---

# Working Principle

1. Processes enter the Ready Queue.
2. Scheduler selects the process with the smallest burst time.
3. Dispatcher assigns the CPU.
4. Process executes.
5. After completion, scheduler again selects the shortest available process.

---

# Flow Diagram

```text
             New Processes
                   │
                   ▼
             Ready Queue
                   │
                   ▼
     Sort by Burst Time (Smallest First)
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
       Next Shortest Process
```

---

# Algorithm (Non-Preemptive SJF)

```
Start

Read Number of Processes

Read Process ID

Read Arrival Time

Read Burst Time

Sort processes by Arrival Time

Current_Time = 0

While all processes are not completed

    Select arrived process having
    minimum Burst Time

    If no process has arrived

        Current_Time++

    Else

        Start_Time = Current_Time

        Current_Time += Burst_Time

        Completion_Time = Current_Time

        Mark Process as Completed

End While

Calculate TAT

Calculate WT

Display Result

Stop
```

---

# Example

## Process Table

| Process | Arrival Time (AT) | Burst Time (BT) |
|----------|------------------:|----------------:|
| P1 | 0 | 6 |
| P2 | 1 | 2 |
| P3 | 2 | 8 |
| P4 | 3 | 3 |

---

# Step-by-Step Execution

### Time = 0

Only P1 has arrived.

```text
Ready Queue

P1
```

CPU executes **P1**.

---

### Time = 6

Ready Queue

```text
P2 (2)

P3 (8)

P4 (3)
```

Smallest Burst Time = **P2**

CPU executes **P2**.

---

### Time = 8

Ready Queue

```text
P3 (8)

P4 (3)
```

Smallest Burst Time = **P4**

CPU executes **P4**.

---

### Time = 11

Only P3 remains.

CPU executes **P3**.

---

# Gantt Chart

```text
0        6      8      11          19
|---P1---|--P2--|--P4--|----P3-----|
```

---

# Completion Time (CT)

| Process | CT |
|----------|---:|
| P1 | 6 |
| P2 | 8 |
| P4 | 11 |
| P3 | 19 |

---

# Turnaround Time (TAT)

## Formula

```
TAT = Completion Time − Arrival Time
```

| Process | Calculation | TAT |
|----------|-------------|----:|
| P1 | 6 − 0 | 6 |
| P2 | 8 − 1 | 7 |
| P3 | 19 − 2 | 17 |
| P4 | 11 − 3 | 8 |

---

# Waiting Time (WT)

## Formula

```
WT = Turnaround Time − Burst Time
```

| Process | Calculation | WT |
|----------|-------------|---:|
| P1 | 6 − 6 | 0 |
| P2 | 7 − 2 | 5 |
| P3 | 17 − 8 | 9 |
| P4 | 8 − 3 | 5 |

---

# Response Time (RT)

## Formula

```
RT = Start Time − Arrival Time
```

| Process | Start Time | RT |
|----------|-----------:|---:|
| P1 | 0 | 0 |
| P2 | 6 | 5 |
| P3 | 11 | 9 |
| P4 | 8 | 5 |

> **Note:** In **Non-Preemptive SJF**, **Response Time = Waiting Time** because a process starts only once.

---

# Average Waiting Time

## Formula

```
Average WT = ΣWT / Number of Processes
```

Example

```
= (0 + 5 + 9 + 5) / 4

= 19 / 4

= 4.75 ms
```

---

# Average Turnaround Time

## Formula

```
Average TAT = ΣTAT / Number of Processes
```

Example

```
= (6 + 7 + 17 + 8) / 4

= 38 / 4

= 9.5 ms
```

---

# Estimated Burst Time

Since the operating system usually **does not know the actual burst time**, it predicts the next CPU burst using **Exponential Averaging**.

## Formula

```
τ(n+1) = α × tn + (1 − α) × τn
```

Where

- τ(n+1) = New estimated burst time
- tn = Actual previous burst time
- τn = Previous estimated burst time
- α = Weight factor (0 ≤ α ≤ 1)

---

# Advantages

- Minimum average waiting time.
- Minimum average turnaround time.
- Better CPU utilization.
- Efficient for batch systems.

---

# Disadvantages

- Difficult to know the actual burst time.
- Long processes may suffer starvation.
- More complex than FCFS.

---

# Starvation

SJF always selects the process with the **shortest burst time**.

If short processes continue arriving, long processes may wait indefinitely.

Example

```text
Ready Queue

P1 (20)

P2 (2)

P3 (1)

P4 (2)

P5 (1)

Execution

P3 → P5 → P2 → P4

↓

P1 keeps waiting
```

This is called **Starvation**.

---

# Solution to Starvation

Use **Aging**.

The priority of a waiting process gradually increases over time until it eventually gets CPU time.

---

# Time Complexity

| Operation | Complexity |
|------------|------------|
| Sorting | O(n log n) |
| Selecting Shortest Process | O(n²) (simple implementation) |
| Using Priority Queue | O(n log n) |

---

# Space Complexity

```
O(n)
```

---

# Real-Life Example

Imagine customers waiting at a billing counter.

| Customer | Items |
|----------|------:|
| A | 15 |
| B | 2 |
| C | 5 |
| D | 1 |

The cashier serves customers with the fewest items first.

Execution

```text
D → B → C → A
```

This is exactly how SJF works.

---

# FCFS vs SJF

| Feature | FCFS | SJF |
|----------|------|-----|
| Selection | Arrival Time | Burst Time |
| Type | Non-Preemptive | Preemptive / Non-Preemptive |
| Waiting Time | Higher | Lower |
| Starvation | No | Yes |
| Complexity | Simple | Moderate |

---

# SJF vs SRTF

| Feature | SJF | SRTF |
|----------|-----|------|
| Type | Non-Preemptive | Preemptive |
| Interrupt Running Process | No | Yes |
| Selection | Shortest Burst Time | Shortest Remaining Time |
| Context Switching | Less | More |
| Waiting Time | Low | Usually Lower |
| Starvation | Possible | More Likely |

---

# Applications

- Batch Processing Systems
- Scientific Computing
- CPU-intensive workloads with predictable burst times
- Embedded systems with known execution times

---

# Interview Questions

## 1. What is SJF Scheduling?

**Answer:**  
SJF (Shortest Job First) is a CPU scheduling algorithm that selects the process with the smallest CPU burst time for execution.

---

## 2. Is SJF preemptive?

**Answer:**  
SJF can be either **Non-Preemptive** or **Preemptive**. The preemptive version is called **Shortest Remaining Time First (SRTF)**.

---

## 3. What is the major disadvantage of SJF?

**Answer:**  
The operating system usually does not know the exact burst time, and long processes may suffer from starvation.

---

## 4. Why does SJF give minimum average waiting time?

**Answer:**  
Executing shorter processes first prevents them from waiting behind long processes, reducing the overall average waiting time.

---

## 5. How is burst time estimated in SJF?

**Answer:**  
Burst time is commonly estimated using **Exponential Averaging** based on previous CPU bursts.

---

# Summary

| Feature | Description |
|----------|-------------|
| Full Form | Shortest Job First |
| Scheduling Type | Non-Preemptive or Preemptive |
| Selection Criteria | Smallest Burst Time |
| Starvation | Yes |
| Solution | Aging |
| Preemptive Version | SRTF |
| Time Complexity | O(n²) or O(n log n) |
| Space Complexity | O(n) |
| Best For | Batch Processing with predictable burst times |
