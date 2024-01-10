import schedulers
import page_replacement
import data_generator

def run_fcfs(num_processes):
    """
    Uruchamia symulację algorytmu First-Come, First-Served (FCFS).

    :param num_processes: Liczba procesów do symulacji.
    :return: Lista procesów po zastosowaniu algorytmu FCFS.
    """
    # Generuje procesy specyficznie dla FCFS i uruchamia algorytm FCFS
    fcfs_processes, _ = data_generator.generate_processes(num_processes)
    return schedulers.fcfs(fcfs_processes)

def run_lcfs(num_processes):
    """
    Uruchamia symulację algorytmu Last-Come, First-Served (LCFS).

    :param num_processes: Liczba procesów do symulacji.
    :return: Lista procesów po zastosowaniu algorytmu LCFS.
    """
    # Generuje procesy specyficznie dla LCFS i uruchamia algorytm LCFS
    _, lcfs_processes = data_generator.generate_processes(num_processes)
    return schedulers.lcfs(lcfs_processes)

def run_fifo(num_requests, frame_count):
    """
    Uruchamia symulację algorytmu zastępowania stron FIFO.

    :param num_requests: Liczba odwołań do stron.
    :param frame_count: Liczba ramek w pamięci.
    :return: Liczba błędów stron po zastosowaniu algorytmu FIFO.
    """
    # Generuje odwołania do stron korzystne dla algorytmu FIFO i uruchamia algorytm FIFO
    pages = data_generator.generate_page_requests_fifo(num_requests)
    return page_replacement.fifo(pages, frame_count)

def run_lru(num_requests, frame_count):
    """
    Uruchamia symulację algorytmu zastępowania stron LRU.

    :param num_requests: Liczba odwołań do stron.
    :param frame_count: Liczba ramek w pamięci.
    :return: Liczba błędów stron po zastosowaniu algorytmu LRU.
    """
    # Generuje odwołania do stron korzystne dla algorytmu LRU i uruchamia algorytm LRU
    pages = data_generator.generate_page_requests_lru(num_requests)
    return page_replacement.lru(pages, frame_count)


def analyze_results(processes):
    """
    Analizuje i zwraca podstawowe statystyki z listy procesów.

    :param processes: Lista procesów do analizy.
    :return: Słownik zawierający średni czas oczekiwania i średni czas cyklu dla listy procesów.
    """
    # Oblicza całkowity czas oczekiwania i całkowity czas cyklu dla wszystkich procesów
    total_waiting_time = sum(p.start_time - p.arrival_time for p in processes)
    total_turnaround_time = sum(p.finish_time - p.arrival_time for p in processes)
    num_processes = len(processes)

    # Zwraca średni czas oczekiwania i średni czas cyklu
    return {
        'Average Waiting Time': total_waiting_time / num_processes,
        'Average Turnaround Time': total_turnaround_time / num_processes
    }
