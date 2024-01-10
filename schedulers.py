class Process:
    def __init__(self, id, arrival_time, burst_time):
        """
        Konstruktor klasy Process, inicjalizujący proces.
        
        :param id: Unikalny identyfikator procesu.
        :param arrival_time: Czas przybycia procesu.
        :param burst_time: Czas wykonania procesu.
        """
        self.id = id  # Unikalny identyfikator procesu
        self.arrival_time = arrival_time  # Czas przybycia procesu
        self.burst_time = burst_time  # Czas wykonania procesu
        self.start_time = None  # Czas rozpoczęcia procesu, początkowo nieustawiony
        self.finish_time = None  # Czas zakończenia procesu, początkowo nieustawiony

def fcfs(processes):
    """
    Implementacja algorytmu FCFS (First Come First Serve).

    :param processes: Lista procesów do obsłużenia.
    :return: Lista procesów z ustawionymi czasami startu i końca.
    """
    time = 0  # Aktualny czas symulacji
    results = []  # Lista procesów po obsłużeniu

    for process in sorted(processes, key=lambda x: x.arrival_time):
        # Sprawdzenie czy bieżący czas symulacji jest mniejszy niż czas przybycia procesu
        if time < process.arrival_time:
            time = process.arrival_time  # Aktualizacja czasu symulacji do czasu przybycia procesu
        process.start_time = time  # Ustawienie czasu startu procesu
        process.finish_time = time + process.burst_time  # Obliczenie i ustawienie czasu zakończenia procesu
        time += process.burst_time  # Aktualizacja czasu symulacji
        results.append(process)  # Dodanie procesu do listy wyników

    return results  # Zwrócenie listy procesów po obsłużeniu

def lcfs(processes):
    """
    Implementacja algorytmu LCFS (Last Come First Serve).

    :param processes: Lista procesów do obsłużenia.
    :return: Lista procesów z ustawionymi czasami startu i końca.
    """
    time = 0  # Aktualny czas symulacji
    finished_processes = []  # Lista procesów po obsłużeniu

    while processes:
        # Wybór procesu, który przybył jako ostatni przed obecnym czasem
        eligible_processes = [p for p in processes if p.arrival_time <= time]
        if not eligible_processes:
            # Jeśli nie ma procesów, które mogłyby być teraz obsłużone
            time = min(p.arrival_time for p in processes if p not in finished_processes)  # Znalezienie najbliższego czasu przybycia procesu
            continue

        process = max(eligible_processes, key=lambda p: p.arrival_time)  # Wybór procesu, który przybył jako ostatni
        process.start_time = time  # Ustawienie czasu startu procesu
        time += process.burst_time  # Obliczenie i ustawienie czasu zakończenia procesu
        process.finish_time = time
        finished_processes.append(process)  # Dodanie procesu do listy wyników
        processes.remove(process)  # Usunięcie procesu z listy do obsłużenia

    return finished_processes  # Zwrócenie listy procesów po obsłużeniu
