# Better most frequent pattern function

from collections import Counter

def frequency_table(text, k):
    """Builds a frequency table for k-mers in the given text."""
    return Counter(text[i:i+k] for i in range(len(text) - k + 1))

def max_map(freq_map):
    """Returns the maximum value in the frequency map."""
    return max(freq_map.values(), default=0)

def better_frequent_words(text, k):
    """Finds the most frequent k-mers in the given text."""
    freq_map = frequency_table(text, k)
    max_count = max_map(freq_map)
    return [kmer for kmer, count in freq_map.items() if count == max_count]

# Example usage
text4 = "ACGTTTCACGTTTTACGG"
k = 3
print(better_frequent_words(text4, k)) # Output: ['ACG', 'TTT']

# Example usage
text5 = "atcaatgatcaacgtaagcttctaagcatgatcaaggtgctcacacagtttatccacaacctgagtggatgacatcaagataggtcgttgtatctccttcctctcgtactctcatgaccacggaaagatgatcaagagaggatgatttcttggccatatcgcaatgaatacttgtgacttgtgcttccaattgacatcttcagcgccatattgcgctggccaaggtgacggagcgggattacgaaagcatgatcatggctgttgttctgtttatcttgttttgactgagacttgttaggatagacggtttttcatcactgactagccaaagccttactctgcctgacatcgaccgtaaattgataatgaatttacatgcttccgcgacgatttacctcttgatcatcgatccgattgaagatcttcaattgttaattctcttgcctcgactcatagccatgatgagctcttgatcatgtttccttaaccctctattttttacggaagaatgatcaagctgctgctcttgatcatcgtttc"
k = 9
print(better_frequent_words(text5, k)) # Output: ['atgatcaag', 'ctcttgatc', 'tcttgatca', 'cttgatcat']
