def fifo(pages, frame_count):
    """
    Implementacja algorytmu FIFO (First-In-First-Out) do zastępowania stron.

    :param pages: Lista odwołań do stron.
    :param frame_count: Liczba dostępnych ramek.
    :return: Całkowita liczba błędów stron (page faults).
    """
    frame = []  # Lista reprezentująca ramki pamięci.
    faults = 0  # Licznik błędów stron.

    for page in pages:  # Iteracja przez każdą stronę.
        if page not in frame:  # Sprawdza, czy strona nie znajduje się już w ramce.
            if len(frame) == frame_count:  # Jeśli ramki są pełne,
                frame.pop(0)  # Usuwa najstarszą stronę (pierwszą dodaną).
            frame.append(page)  # Dodaje nową stronę do ramek.
            faults += 1  # Zwiększa licznik błędów stron.
    return faults  # Zwraca całkowitą liczbę błędów stron.

def lru(pages, frame_count):
    """
    Implementacja algorytmu LRU (Least Recently Used) do zastępowania stron.

    :param pages: Lista odwołań do stron.
    :param frame_count: Liczba dostępnych ramek.
    :return: Całkowita liczba błędów stron (page faults).
    """
    frame = []  # Lista reprezentująca ramki pamięci.
    recent = []  # Lista przechowująca kolejność ostatniego użycia stron.
    faults = 0  # Licznik błędów stron.

    for page in pages:  # Iteracja przez każdą stronę.
        if page not in frame:  # Sprawdza, czy strona nie znajduje się już w ramce.
            if len(frame) == frame_count:  # Jeśli ramki są pełne,
                # Usuwa najmniej niedawno używaną stronę (LRU).
                frame.remove(recent.pop(0))
            frame.append(page)  # Dodaje nową stronę do ramek.
            faults += 1  # Zwiększa licznik błędów stron.
        else:
            recent.remove(page)  # Usuwa stronę z listy ostatnio użytych.
        recent.append(page)  # Dodaje stronę na koniec listy ostatnio użytych.
    return faults  # Zwraca całkowitą liczbę błędów stron.
