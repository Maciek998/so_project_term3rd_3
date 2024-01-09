import schedulers
import page_replacement
import data_generator
import experiments
import reporting

def get_simulation_parameters():
    """ Pobiera od użytkownika parametry do symulacji. """
    num_processes = int(input("Podaj liczbę procesów: "))
    num_requests = int(input("Podaj liczbę żądań stron: "))
    frame_count = int(input("Podaj liczbę ramek w pamięci: "))
    return num_processes, num_requests, frame_count

def main():
    print("Witaj w symulatorze algorytmów planowania i zastępowania stron.")
    mode = input("Wybierz tryb: 'symulacja' lub 'wykresy': ").strip().lower()

    if mode == 'symulacja':
        num_processes, num_requests, frame_count = get_simulation_parameters()
        
        # Generowanie danych
        processes = data_generator.generate_processes(num_processes)
        requests = data_generator.generate_page_requests(num_requests)

        # Uruchamianie symulacji dla każdego algorytmu
        fcfs_results = experiments.run_fcfs(processes)
        lcfs_results = experiments.run_lcfs(processes)
        fifo_results = experiments.run_fifo(requests, frame_count)
        lru_results = experiments.run_lru(requests, frame_count)

        # Zapisywanie wyników do pliku CSV
        reporting.save_results_to_csv('results.csv', fcfs_results, lcfs_results, fifo_results, lru_results)
        print("Symulacja zakończona. Wyniki zapisane do 'results.csv'.")

    elif mode == 'wykresy':
        file_name = input("Podaj nazwę pliku CSV z wynikami: ")
        reporting.generate_charts_from_csv(file_name)
        print("Wykresy zostały wygenerowane na podstawie danych z pliku", file_name)

    else:
        print("Niepoprawny tryb. Proszę uruchomić program ponownie i wybrać 'symulacja' lub 'wykresy'.")

if __name__ == "__main__":
    main()
