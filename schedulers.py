class Process:
    def __init__(self, arrival_time, burst_time):
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = None
        self.finish_time = None

def fcfs(processes):
    """ Implementacja algorytmu FCFS. """
    time = 0
    results = []

    for process in sorted(processes, key=lambda x: x.arrival_time):
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        process.finish_time = time + process.burst_time
        time += process.burst_time
        results.append(process)

    return results

def lcfs(processes):
    """ Implementacja algorytmu LCFS. """
    time = 0
    process_stack = []
    results = []

    for process in sorted(processes, key=lambda x: x.arrival_time, reverse=True):
        process_stack.append(process)

    while process_stack:
        process = process_stack.pop()
        if time < process.arrival_time:
            time = process.arrival_time
        process.start_time = time
        process.finish_time = time + process.burst_time
        time += process.burst_time
        results.append(process)

    return results
