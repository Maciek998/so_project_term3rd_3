import csv
import matplotlib.pyplot as plt

def save_results_to_csv(filename, fcfs_results, lcfs_results, fifo_results, lru_results):
    """
    Zapisuje wyniki symulacji do pliku CSV.
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Algorithm', 'Average Waiting Time', 'Average Turnaround Time', 'Faults'])

        # Zapisanie wyników dla algorytmów planowania procesora
        for algorithm, results in [('FCFS', fcfs_results), ('LCFS', lcfs_results)]:
            avg_waiting_time = sum(p.start_time - p.arrival_time for p in results) / len(results)
            avg_turnaround_time = sum(p.finish_time - p.arrival_time for p in results) / len(results)
            writer.writerow([algorithm, avg_waiting_time, avg_turnaround_time, 'N/A'])

        # Zapisanie wyników dla algorytmów zastępowania stron
        for algorithm, faults in [('FIFO', fifo_results), ('LRU', lru_results)]:
            writer.writerow([algorithm, 'N/A', 'N/A', faults])


def generate_charts_from_csv(filename):
    """
    Generuje wykresy na podstawie danych z pliku CSV.
    """
    algorithms = []
    waiting_times = []
    turnaround_times = []
    faults = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Pomiń nagłówek
        for row in reader:
            algorithms.append(row[0])
            waiting_times.append(float(row[1]) if row[1] != 'N/A' else 0)
            turnaround_times.append(float(row[2]) if row[2] != 'N/A' else 0)
            faults.append(int(row[3]) if row[3] != 'N/A' else 0)

    # Tworzenie wykresów
    plt.figure(figsize=(10, 6))

    # Dodajemy warunek, aby uniknąć dodawania None do wykresu
    if any(waiting_times):
        plt.bar(algorithms, waiting_times, color='blue', label='Average Waiting Time')
    if any(turnaround_times):
        plt.bar(algorithms, turnaround_times, color='green', label='Average Turnaround Time', bottom=waiting_times)
    if any(faults):
        plt.bar(algorithms, faults, color='red', label='Faults')

    plt.xlabel('Algorithms')
    plt.ylabel('Metrics')
    plt.title('Comparison of Algorithm Performance')
    plt.legend()
    plt.show()
