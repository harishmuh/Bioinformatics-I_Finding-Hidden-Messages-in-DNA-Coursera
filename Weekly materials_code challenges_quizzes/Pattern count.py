# Defining pattern_count function
def pattern_count(text, pattern):
    """Counts the number of times a pattern appears in a given text, including overlapping occurrences."""
    count = 0
    pattern_length = len(pattern)

    for i in range(len(text) - pattern_length + 1):  # Slide over the text
        if text[i:i + pattern_length] == pattern:  # Check substring match
            count += 1

    return count


# Example usage 1
text1 = "ACAACTATGCATACTATCGGGAACTATCCT"
pattern1 = "ACTAT"
print(pattern_count(text1, pattern1))  # Output: 3

# Example usage 2
text2 = "CGATATATCCATAG"
pattern2 = "ATA"
print(pattern_count(text2, pattern2))  # Output: 3
