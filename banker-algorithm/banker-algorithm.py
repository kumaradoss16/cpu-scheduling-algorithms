class BankerAlgorithm:
    def __init__(self, allocation, max_demand, available):
        self.allocation = allocation
        self.max_demand = max_demand
        self.available = available[:]
        self.num_processes = len(allocation)
        self.num_resources = len(available)

        # need[i][j] = max_demand[i][j] - allocation[i][j]
        self.need = [
            [max_demand[i][j] - allocation[i][j] for j in range(self.num_resources)]
            for i in range(self.num_processes)
        ]


    def is_safe_state(self):
        work = self.available[:]
        finish = [False] * self.num_processes
        safe_sequence = []

        progress_made = True
        while progress_made:
            progress_made = False
            for i in range(self.num_processes):
                if finish[i]:
                    continue

                # Check if need[i][j] <= work for every resource type
                if all(self.need[i][j] <= work[j] for j in range(self.num_resources)):
                    for j in range(self.num_resources):
                        work[j] += self.allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    progress_made = True

        if all(finish):
            return True, safe_sequence
        return False, []


    def request_resources(self, process_id, request):
        if any(request[j] > self.need[process_id][j] for j in range(self.num_resources)):
            print(f"Error: Process {process_id} exceed its maximum claim.")
            return False

        if any(request[j] > self.available[j] for j in range(self.num_resources)):
            print(f"Process {process_id} must wait - resources not available.")
            return False

        old_available = self.available[:]
        old_allocation = self.allocation[:]
        old_need = self.need[:]

        for j in range(self.num_resources):
            self.available[j] -= request[j]
            self.allocation[process_id][j] += request[j]
            self.need[process_id][j] -= request[j]

        safe, sequence = self.is_safe_state()

        if safe:
            print(f"Request granted for Process {process_id}. Safe sequence: {sequence}")
            return True
        else:
            self.available = old_available
            self.allocation = old_allocation
            self.need = old_need
            print(f"Request denied for Process {process_id} - would lead to unsafe state.")
            return False


    def display_state(self):
        print(f"\nProcess | Allocation |    {'Max':<6} |    Need")
        for i in range(self.num_processes):
            print(f"  P{i}    | {self.allocation[i]}  | {self.max_demand[i]} | {self.need[i]}")
        print(f"Available: {self.available}\n")


if __name__ == "__main__":
    allocation = [
        [0, 1, 0],   # P0
        [2, 0, 0],   # P1
        [3, 0, 2],   # P2
        [2, 1, 1],   # P3
        [0, 0, 2],   # P4
    ]

    max_demand = [
        [7, 5, 3],  # P0
        [3, 2, 2],  # P1
        [9, 0, 2],  # P2
        [2, 2, 2],  # P3
        [4, 3, 3],  # P4
    ]

    available = [3, 3, 2]

    banker = BankerAlgorithm(allocation, max_demand, available)
    banker.display_state()

    # Test 1 : check initial safety
    safe, sequence = banker.is_safe_state()
    if safe:
        print(f"System is in a SAFE state. Safe sequence: {sequence}")
    else:
        print("System is in an UNSAFE state.")

    # Test 2: Process 1 requests (1, 0, 2)
    print("\n--- Process 1 requests (1, 0, 2) ---")
    banker.request_resources(1, [1, 0, 2])

    print("\n--- Process 4 requests (3, 3, 0) ---")
    banker.request_resources(4, [3, 3, 0])

    print("\n--- Process 0 requests (0, 2, 0) ---")
    banker.request_resources(0, [0, 2, 0])


