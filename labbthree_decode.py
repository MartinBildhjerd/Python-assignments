#AUTHOR: Martin C. Bildhjerd

import random
from heapq import heappush, heappop, heapify
from collections import defaultdict

code_dict = {
    'b': '00000000',
    'd': '00000001',
    'g': '00000010',
    'i': '00000011',
    'k': '00000100',
    'l': '00000101',
    'j': '00000110',
    'n': '00000111',
    'f': '00001000',
    'h': '00001001',
    'a': '00001010',
    'e': '00001011',
    'm': '00001100',
    'c': '00001101',
    'o': '00001110',
    'p': '00001111'
}

# Define the Huffman decoding function
def huffman_decoding(encoded_string, codes):
    # Create a mapping from codes to symbols by reversing the codes dictionary
    reverse_codes = {v: k for k, v in codes.items()}
    # Initialize a variable to accumulate bits into valid Huffman codes
    current_code = ""
    # Initialize a list to hold the decoded symbols
    decoded_output = []

    # Iterate over each bit in the encoded string
    for bit in encoded_string:
        # Add the current bit to the accumulating code string
        current_code += bit
        # Check if the accumulated string matches a code in the dictionary
        if current_code in reverse_codes:
            # If a match is found, append the corresponding symbol to the output
            decoded_output.append(reverse_codes[current_code])
            # Reset the accumulating string to start decoding the next set of bits
            current_code = ""

    return decoded_output  # Return the list of decoded symbols

# Suppose we have an encoded string obtained from the Huffman coding process
encoded_string = "01010101110011001111110111101111000"

# Use the Huffman code dictionary generated earlier
decoded_symbols = huffman_decoding(encoded_string, code_dict)

# Print the decoded result
print("Decoded symbols:", decoded_symbols)