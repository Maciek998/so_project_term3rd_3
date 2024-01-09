import random
from schedulers import Process

def generate_processes(num_processes, arrival_time_range=(0, 50), burst_time_range=(1, 10)):
    """
    Generuje listę procesów z losowymi czasami nadejścia (arrival_time) i wykonania (burst_time).
    :param num_processes: Liczba generowanych procesów.
    :param arrival_time_range: Zakres czasu nadejścia procesów (min, max).
    :param burst_time_range: Zakres czasu wykonania procesów (min, max).
    :return: Lista procesów.
    """
    processes = []
    for _ in range(num_processes):
        arrival_time = random.randint(*arrival_time_range)
        burst_time = random.randint(*burst_time_range)
        processes.append(Process(arrival_time, burst_time))
    return processes

def generate_page_requests(num_requests, page_range=(1, 10)):
    """
    Generuje listę żądań stron.
    :param num_requests: Liczba generowanych żądań stron.
    :param page_range: Zakres numerów stron (min, max).
    :return: Lista żądań stron.
    """
    return [random.randint(*page_range) for _ in range(num_requests)]
