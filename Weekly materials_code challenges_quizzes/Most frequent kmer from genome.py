# Most frequent 9-mers with 1 mismatch and reverse complement

# Importing libraries
from collections import defaultdict
from itertools import product
import requests

# Function to compute the Hamming distance
def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

# Function to generate all k-mers with at most d mismatches
def generate_neighbors(pattern, d):
    """Generate all k-mers with at most d mismatches from pattern."""
    nucleotides = "ACGT"
    pattern_list = list(pattern)
    neighbors = set()

    # Generate all possible positions to mutate
    for positions in product(range(len(pattern)), repeat=d):
        mutated = pattern_list[:]
        for pos in positions:
            for nucleotide in nucleotides:
                if mutated[pos] != nucleotide:
                    temp = mutated[:]
                    temp[pos] = nucleotide
                    neighbors.add("".join(temp))

    neighbors.add(pattern)  # Include the original pattern
    return neighbors

# Function to compute the reverse complement
def reverse_complement(seq):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in reversed(seq))

# Function to find the most frequent k-mers with mismatches and reverse complements
def frequent_words_with_mismatches_and_rc(text, k, d):
    """Find the most frequent k-mers with up to d mismatches and their reverse complements."""
    freq_map = defaultdict(int)
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i+k]
        neighborhood = generate_neighbors(pattern, d)

        for neighbor in neighborhood:
            rc = reverse_complement(neighbor)
            freq_map[neighbor] += 1
            freq_map[rc] += 1  # Count reverse complement as well

    max_freq = max(freq_map.values())
    most_frequent_kmers = [key for key, val in freq_map.items() if val == max_freq]

    return most_frequent_kmers

# Example usage

# Requesting E coli genome (txt) from website
ecoli_genome = requests.get("https://bioinformaticsalgorithms.com/data/realdatasets/Replication/E_coli.txt").text

# Parameters
k = 9  # K-mer length
d = 1  # Allowed mismatches

# Find the most frequent 9-mers with 1 mismatch and reverse complement
result = frequent_words_with_mismatches_and_rc(ecoli_genome, k, d)

print("Most frequent 9-mers with 1 mismatch and reverse complement:")
print(" ".join(result))

# Output Most frequent 9-mers with 1 mismatch and reverse complement: GCGCTGGCG CGCCAGCGC
