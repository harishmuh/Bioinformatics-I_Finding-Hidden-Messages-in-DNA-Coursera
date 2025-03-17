# Find minimum skew
# Function to find the positions of the minimum skew in DNA sequence
def find_minimum_skew_positions(sequence):
    # Compute skew values
    skew_values = compute_skew(sequence)
    # Find the minimum skew value
    min_skew = min(skew_values)
    # Find all positions where the skew value equals the minimum
    min_positions = [i for i, value in enumerate(skew_values) if value == min_skew]
    return min_positions

# Example usage
# Given DNA sequence for the problem
genome = "TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"

# Find positions where skew is minimized
min_skew_positions = find_minimum_skew_positions(genome)
min_skew_positions # Output: [11, 24]
