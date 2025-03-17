# Find clumps

# Defining function for creating frequency table
def frequency_table(text, k):
    """
    Creates a frequency table of all k-mers in a given text.

    Parameters:
        text (str): The input DNA sequence.
        k (int): The length of k-mers.

    Returns:
        dict: A dictionary with k-mers as keys and their counts as values.
    """
    freq_map = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i + k]
        freq_map[kmer] = freq_map.get(kmer, 0) + 1
    return freq_map

# Defining function for finding clumps
def find_clumps(text, k, L, t):
    """
    Finds (k, L, t)-clumps in the given DNA sequence.

    Parameters:
        text (str): The input DNA sequence.
        k (int): The length of k-mers.
        L (int): The length of the window.
        t (int): The minimum number of times a k-mer must appear in a window to be considered a clump.

    Returns:
        list: A list of k-mers that form (k, L, t)-clumps.
    """
    patterns = set()  # Use a set to automatically remove duplicates
    n = len(text)

    for i in range(n - L + 1):
        window = text[i:i + L]
        freq_map = frequency_table(window, k)

        for kmer, count in freq_map.items():
            if count >= t:
                patterns.add(kmer)

    return list(patterns)

# Example usage
sample_text = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k = 5
L = 50
t = 4
find_clumps(sample_text, k, L, t)
