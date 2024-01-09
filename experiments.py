import schedulers
import page_replacement

def run_fcfs(processes):
    """ Uruchomienie symulacji algorytmu FCFS. """
    return schedulers.fcfs(processes)

def run_lcfs(processes):
    """ Uruchomienie symulacji algorytmu LCFS. """
    return schedulers.lcfs(processes)

def run_fifo(pages, frame_count):
    """ Uruchomienie symulacji algorytmu FIFO. """
    return page_replacement.fifo(pages, frame_count)

def run_lru(pages, frame_count):
    """ Uruchomienie symulacji algorytmu LRU. """
    return page_replacement.lru(pages, frame_count)

def analyze_results(processes):
    """ Analiza i zwrócenie podstawowych statystyk z listy procesów. """
    total_waiting_time = sum(p.start_time - p.arrival_time for p in processes)
    total_turnaround_time = sum(p.finish_time - p.arrival_time for p in processes)
    num_processes = len(processes)
    return {
        'Average Waiting Time': total_waiting_time / num_processes,
        'Average Turnaround Time': total_turnaround_time / num_processes
    }
