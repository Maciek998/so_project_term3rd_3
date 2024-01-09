def fifo(pages, frame_count):
    """ Implementacja algorytmu FIFO. """
    frame = []
    faults = 0
    for page in pages:
        if page not in frame:
            if len(frame) == frame_count:
                frame.pop(0)
            frame.append(page)
            faults += 1
    return faults

def lru(pages, frame_count):
    """ Implementacja algorytmu LRU. """
    frame = []
    recent = []
    faults = 0
    for page in pages:
        if page not in frame:
            if len(frame) == frame_count:
                frame.remove(recent.pop(0))
            frame.append(page)
            faults += 1
        else:
            recent.remove(page)
        recent.append(page)
    return faults
