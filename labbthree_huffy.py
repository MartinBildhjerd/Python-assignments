#AUTHOR: Martin C. Bildhjerd

import random
from heapq import heappush, heappop, heapify
from collections import defaultdict

# heappush -> Add element to heap, makes them in order small TO large
# heappop -> Removes the smallest element in heap
# heapify -> Making a list a heap, basically rearrangement

probabilities = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16
}

def transformation(probabilities):
    heap = [[weight, [symbol, ""]] for symbol, weight in probabilities.items()]
    heapify(heap)

    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heappop(heap)[1:], key=lambda p: (len(p[1]), p))

codes = transformation(probabilities)

for letter, code in codes:
    print(f"{letter}: {code}")