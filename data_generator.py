import random
from schedulers import Process

def generate_processes(num_processes, max_arrival_time=100, max_burst_time=20):
    """
    Generuje dwie listy procesów dla algorytmów FCFS i LCFS.

    :param num_processes: Liczba procesów do wygenerowania.
    :param max_arrival_time: Maksymalny czas przybycia procesu.
    :param max_burst_time: Maksymalny czas wykonania (burst time) procesu.
    :return: Dwie listy procesów, jedna dla FCFS, druga dla LCFS.
    """
    processes_fcfs = []  # Lista dla procesów FCFS
    processes_lcfs = []  # Lista dla procesów LCFS

    for i in range(num_processes):
        # Generowanie czasu przybycia i czasu wykonania dla każdego procesu
        arrival_time = random.randint(0, max_arrival_time)
        burst_time_fcfs = random.randint(1, max_burst_time // 2)  # Krótszy czas wykonania dla FCFS
        burst_time_lcfs = random.randint(max_burst_time // 2, max_burst_time)  # Dłuższy czas wykonania dla LCFS

        # Tworzenie procesów i dodawanie ich do odpowiednich list
        processes_fcfs.append(Process(i, arrival_time, burst_time_fcfs))
        processes_lcfs.append(Process(i + num_processes, arrival_time, burst_time_lcfs))

    return processes_fcfs, processes_lcfs

def generate_page_requests_fifo(num_requests, page_range=(1, 10)):
    """
    Generuje listę odwołań do stron korzystną dla algorytmu FIFO.

    :param num_requests: Liczba odwołań do stron do wygenerowania.
    :param page_range: Zakres numerów stron (min, max).
    :return: Lista odwołań do stron.
    """
    # Generowanie losowej listy odwołań do stron
    requests = [random.randint(*page_range) for _ in range(num_requests)]
    return requests

def generate_page_requests_lru(num_requests, page_range=(1, 10)):
    """
    Generuje listę odwołań do stron korzystną dla algorytmu LRU.

    :param num_requests: Liczba odwołań do stron do wygenerowania.
    :param page_range: Zakres numerów stron (min, max).
    :return: Lista odwołań do stron.
    """
    requests = []
    # Generowanie listy odwołań z powtórkami (korzystne dla LRU)
    for _ in range(num_requests // 2):
        page = random.randint(*page_range)
        requests.extend([page, page])  # Dodanie dwóch takich samych stron

    # Dodanie pozostałych losowych odwołań do stron
    requests.extend([random.randint(*page_range) for _ in range(num_requests // 2)])
    return requests[:num_requests]
