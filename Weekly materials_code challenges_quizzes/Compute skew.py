# Computing genome skew
def compute_skew(genome):
    skew = [0]  # Initialize Skew0(Genome) = 0
    for nucleotide in genome:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)  # Increase for G
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)  # Decrease for C
        else:
            skew.append(skew[-1])  # No change for A or T
    return skew

# Example usage:
genome = "CATGGGCATCGGCCATACGCC"  # Input DNA sequence
skew_values = compute_skew(genome)
print(" ".join(map(str, skew_values)))
# Expected answer should be: 0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
