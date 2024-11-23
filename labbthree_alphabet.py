#AUTHOR: Martin C. Bildhjerd

import random 
from heapq import heappush, heappop, heapify
from collections import defaultdict

#heappush -> Add element to heap, makes them in order small TO large
#heappop -> Removes the smallest element in heap
#heapify -> Makinga list a heap, basicly rearangement

##STEP ONE, CREATING 16 ALPHABET
letters = [chr(i) for i in range(ord('a'), ord ('p')+1)] #FROM EXAMPLE
random_probs = [random.random() for _ in range(16)] #FROM EXAMPLE, BUT WE DO TIL 16
total_prob = sum(random_probs) #FROM EXAMPLE
probabilities =  {letters[i]: random_probs[i]/total_prob for i in range(16)} ##FROM EXAMPLE, BUT WE DO TIL 16 
###

print(probabilities)
