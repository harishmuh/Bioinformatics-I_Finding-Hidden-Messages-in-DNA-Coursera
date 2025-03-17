# Defining function for finding similar pattern location
def PatternLocation(Pattern,Genome):
    positions=[]
    Genome_length=len(Genome)
    Pattern_length=len(Pattern)
    for i in range(Genome_length - Pattern_length+1):
        if Genome[i:i+Pattern_length]==Pattern:
            positions.append([i])
    return positions

# Function to get neat output (according to expected output format)
def FlattenIndices(starting_list):
    flattened = ' '.join(map(str, [i[0] for i in starting_list]))
    return flattened

# Example usage
Pattern = 'ATAT'
Genome = 'GATATATGCATATACTT'
starting_list = PatternLocation(Pattern,Genome)
print(FlattenIndices(starting_list)) # Output: 1 3 9
