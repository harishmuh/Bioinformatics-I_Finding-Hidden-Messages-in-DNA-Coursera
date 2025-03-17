# Approximate Pattern Matching Problem
# Find all approximate occurences of text with at most d mistmatches

def hamming_distance(p, q):
    """Computes the Hamming distance between two equal-length strings p and q."""
    return sum(1 for x, y in zip(p, q) if x != y)

def approximate_pattern_matching(pattern, text, d):
    """Finds all starting positions where pattern appears in text with at most d mismatches."""
    pattern_length = len(pattern)
    text_length = len(text)
    positions = []

    # Slide over the text to check all substrings of length k
    for i in range(text_length - pattern_length + 1):
        substring = text[i:i + pattern_length]  # Extract substring of length k
        if hamming_distance(pattern, substring) <= d:
            positions.append(i)

    return positions

# Example usage:
pattern = "ATTCTGGA"
text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"
d = 3

# Get positions and print them space-separated
positions = approximate_pattern_matching(pattern, text, d)
print(" ".join(map(str, positions))) # Expected output: 6 7 26 27
