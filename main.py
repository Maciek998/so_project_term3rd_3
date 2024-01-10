import schedulers
import page_replacement
import data_generator
import experiments
import reporting

def get_simulation_parameters():
    """
    Funkcja do pobrania parametrów symulacji od użytkownika.
    """
    num_processes = int(input("Podaj liczbę procesów: "))  # Pobiera liczbę procesów
    num_requests = int(input("Podaj liczbę żądań stron: "))  # Pobiera liczbę odwołań do stron
    frame_count = int(input("Podaj liczbę ramek w pamięci: "))  # Pobiera liczbę ramek pamięci
    return num_processes, num_requests, frame_count  # Zwraca pobrane parametry

def print_process_details(processes, algorithm_name):
    """
    Funkcja do wyświetlania szczegółów procesów po symulacji.

    :param processes: Lista procesów do wyświetlenia.
    :param algorithm_name: Nazwa algorytmu użytego do symulacji.
    """
    print(f"\nSzczegóły procesów dla {algorithm_name}:")
    for process in processes:
        # Wyświetla szczegóły każdego procesu (ID, czas przybycia, startu, zakończenia, oraz czas oczekiwania)
        print(f"ID: {process.id}, Arrival: {process.arrival_time}, Start: {process.start_time}, Finish: {process.finish_time}, Waiting: {process.start_time - process.arrival_time}")

def main():
    """
    Główna funkcja programu do symulacji algorytmów planowania procesów i zastępowania stron.
    """
    print("Witaj w symulatorze algorytmów planowania i zastępowania stron.")
    mode = input("Wybierz tryb: 'symulacja' lub 'wykresy': ").strip().lower()

    if mode == 'symulacja':
        # Pobiera parametry symulacji
        num_processes, num_requests, frame_count = get_simulation_parameters()
        
        # Uruchamia symulację dla różnych algorytmów
        fcfs_results = experiments.run_fcfs(num_processes)
        lcfs_results = experiments.run_lcfs(num_processes)
        fifo_results = experiments.run_fifo(num_requests, frame_count)
        lru_results = experiments.run_lru(num_requests, frame_count)

        # Wyświetla szczegółowe informacje o procesach
        print_process_details(fcfs_results, "FCFS")
        print_process_details(lcfs_results, "LCFS")

        # Analizuje i wyświetla wyniki symulacji
        fcfs_analysis = experiments.analyze_results(fcfs_results)
        lcfs_analysis = experiments.analyze_results(lcfs_results)
        print("Analiza FCFS:", fcfs_analysis)
        print("Analiza LCFS:", lcfs_analysis)

        # Zapisuje wyniki symulacji do pliku CSV
        reporting.save_results_to_csv('results.csv', fcfs_results, lcfs_results, fifo_results, lru_results)
        print("Symulacja zakończona. Wyniki zapisane do 'results.csv'.")

    elif mode == 'wykresy':
        # Generuje wykresy na podstawie wyników zapisanych w pliku CSV
        file_name = input("Podaj nazwę pliku CSV z wynikami: ")
        reporting.generate_charts_from_csv(file_name)
        print("Wykresy zostały wygenerowane na podstawie danych z pliku", file_name)

    else:
        # Informuje użytkownika o błędnym wyborze trybu
        print("Niepoprawny tryb. Proszę uruchomić program ponownie i wybrać 'symulacja' lub 'wykresy'.")

if __name__ == "__main__":
    main()
