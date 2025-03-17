# Find the most frequent pattern in sequence

# Defining function to count patterns
def PatternCount(Text, Pattern):
    """Counts occurrences of Pattern in Text."""
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

# Find the most frequent pattern
def FrequentWords(Text, k):
    """Finds the most frequent k-mers in a string Text."""
    FrequentPatterns = set()
    Count = []

    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        Count.append(PatternCount(Text, Pattern))

    maxCount = max(Count)

    for i in range(len(Text) - k + 1):
        if Count[i] == maxCount:
            FrequentPatterns.add(Text[i:i+k])  # Using a set to avoid duplicates

    return list(FrequentPatterns)

# Example usage
Text = "ACTGACTCCCACCCC"
k = 3
print(FrequentWords(Text, k)) # Output: 'CCC'
