# Find clumps and total number of clumps

# Defining function to find clumps without duplicate and calculate the number of clumps
def find_clumps(text, k, L, t):
    """
    Finds (k, L, t)-clumps in a given genome sequence.

    Parameters:
        text (str): Genome sequence.
        k (int): Length of the k-mer.
        L (int): Length of the window.
        t (int): Minimum occurrences of the k-mer in the window.

    Returns:
        set: Unique k-mers that form clumps.
        int: Number of unique clumps found.
    """
    clumps = set()  # Use a set to store unique k-mers forming clumps
    n = len(text)

    for i in range(n - L + 1):  # Slide window across text
        window = text[i:i + L]  # Extract L-length substring
        freq_map = {}  # Dictionary to store frequency of k-mers

        # Compute frequency of k-mers in the window
        for j in range(L - k + 1):
            kmer = window[j:j + k]
            freq_map[kmer] = freq_map.get(kmer, 0) + 1

        # Find k-mers that meet the threshold t
        for kmer, count in freq_map.items():
            if count >= t:
                clumps.add(kmer)  # Add unique k-mer to the set

    return clumps, len(clumps)  # Return unique k-mers and their count

# Example usage
genome = "ACGTACGTACGTACGT"
k = 3  # Length of k-mer
L = 10  # Length of window
t = 2  # Minimum frequency

clumps, num_clumps = find_clumps(genome, k, L, t)

print("Unique Clumps Found:", clumps) # Output: Unique Clumps Found: {'TAC', 'CGT', 'ACG', 'GTA'}
print("Number of Unique Clumps:", num_clumps) # Output: 4
