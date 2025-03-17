# Pattern with mismatches

# Hamming distance function
def hamming_distance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count


# Pattern with mismatches pattern
def patternWithMisMatches(pattern, genome, d):
    positions = []
    for i in range(len(genome)-len(pattern)+1):
        if hamming_distance(pattern, genome[i:i+len(pattern)]) <= d:
            positions.append(i)
    return positions


pattern_with_mismatches = len(patternWithMisMatches("AAAAA", "AACAAGCTGATAAACATTTAAAGAG", 2)) 
print('The number of pattern with mismatches pattern',pattern_with_mismatches) # Output: 11
