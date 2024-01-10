import csv
import matplotlib.pyplot as plt

def save_results_to_csv(filename, fcfs_results, lcfs_results, fifo_results, lru_results):
    """
    Zapisuje wyniki symulacji do pliku CSV.

    :param filename: Nazwa pliku, do którego zapisywane są wyniki.
    :param fcfs_results: Wyniki symulacji dla algorytmu FCFS.
    :param lcfs_results: Wyniki symulacji dla algorytmu LCFS.
    :param fifo_results: Wyniki symulacji dla algorytmu FIFO.
    :param lru_results: Wyniki symulacji dla algorytmu LRU.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Algorithm', 'Average Waiting Time', 'Average Turnaround Time', 'Faults'])

        # Zapisanie wyników dla algorytmów planowania procesora
        for algorithm, results in [('FCFS', fcfs_results), ('LCFS', lcfs_results)]:
            # Obliczanie średniego czasu oczekiwania i średniego czasu cyklu
            avg_waiting_time = sum(p.start_time - p.arrival_time for p in results) / len(results)
            avg_turnaround_time = sum(p.finish_time - p.arrival_time for p in results) / len(results)
            writer.writerow([algorithm, avg_waiting_time, avg_turnaround_time, 'N/A'])

        # Zapisanie wyników dla algorytmów zastępowania stron
        for algorithm, faults in [('FIFO', fifo_results), ('LRU', lru_results)]:
            # Zapisywanie liczby błędów stron dla każdego algorytmu
            writer.writerow([algorithm, 'N/A', 'N/A', faults])


def generate_charts_from_csv(filename):
    """
    Generuje wykresy na podstawie danych z pliku CSV.

    :param filename: Nazwa pliku CSV, z którego wczytywane są dane.
    """
    algorithms = []
    waiting_times = []
    turnaround_times = []
    faults = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pominięcie nagłówka

        for row in reader:
            # Zbieranie danych z pliku CSV
            algorithms.append(row[0])
            waiting_times.append(float(row[1]) if row[1] != 'N/A' else 0)
            turnaround_times.append(float(row[2]) if row[2] != 'N/A' else 0)
            faults.append(int(row[3]) if row[3] != 'N/A' else 0)

    plt.figure(figsize=(12, 6))

    # Wykres 1: FIFO i LRU
    plt.subplot(1, 2, 1)
    # Rysowanie wykresu słupkowego dla liczby błędów stron dla FIFO i LRU
    plt.bar(['FIFO', 'LRU'], [faults[algorithms.index('FIFO')], faults[algorithms.index('LRU')]], color='red', label='Faults')
    plt.xlabel('Algorithms')
    plt.ylabel('Faults')
    plt.title('Page Replacement Algorithms (FIFO and LRU)')
    plt.legend()

    # Wykres 2: FCFS i LCFS
    plt.subplot(1, 2, 2)
    # Rysowanie wykresu słupkowego dla średniego czasu oczekiwania i średniego czasu cyklu dla FCFS i LCFS
    fcfs_index = algorithms.index('FCFS')
    lcfs_index = algorithms.index('LCFS')
    plt.bar(['FCFS', 'LCFS'], [waiting_times[fcfs_index], waiting_times[lcfs_index]], color='blue', label='Average Waiting Time')
    plt.bar(['FCFS', 'LCFS'], [turnaround_times[fcfs_index], turnaround_times[lcfs_index]], color='green', label='Average Turnaround Time', bottom=[waiting_times[fcfs_index], waiting_times[lcfs_index]])
    plt.xlabel('Algorithms')
    plt.ylabel('Metrics')
    plt.title('Scheduling Algorithms (FCFS and LCFS)')
    plt.legend()

    plt.tight_layout()  # Zapewnienie odpowiedniego rozmieszczenia wykresów
    plt.show()
