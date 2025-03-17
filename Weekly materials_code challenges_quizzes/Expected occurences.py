'''

Quiz
Section: Motif finding is more difficult than you think

Exercise Break: 
What is the expected number of occurrences of a 9-mer in 500 random DNA strings, each of length 1000? 
Assume that the sequences are formed by selecting each nucleotide (A, C, G, T) with the same probability (0.25).

*Note: Express your answer as a decimal; allowable error = 0.0001.

'''

# Function to calculate expected occurrences of a k-mer in a single string
def expected_occurrences(string_length, kmer_length, probability):
    return (string_length - kmer_length + 1) * probability

string_length = 1000  # Length of each string
kmer_length = 9  # Length of the k-mer
probability = 0.25 ** 9  # Probability of a specific 9-mer occurring at any position

# Expected occurrences in one string
expected_per_string = expected_occurrences(string_length, kmer_length, probability)

# Expected occurrences across 500 strings
expected_per_500_strings = expected_per_string * 500

# Print results
print(f'Expected occurrences per string: {expected_per_string:.4f}') # Output: Expected occurrences per string: 0.0038
print(f'Expected occurrences per 500 strings: {expected_per_500_strings:.4f}') # Output: Expected occurrences per 500 strings: 1.8921
