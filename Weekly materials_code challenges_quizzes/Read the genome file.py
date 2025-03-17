# Define a function to read the genome sequence from the file # Input only clean txt file
def read_genome(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and concatenate them
        genome = file.read().strip()
    return genome

# Define a function to read the genome sequence from the file
# Input may contain integers or others
import re

def read_genome_int(file_path):
    """
    Reads a genome sequence from a file and extracts only text (letters),
    removing numbers and special characters.

    Parameters:
        file_path (str): Path to the file containing the genome sequence.

    Returns:
        str: The cleaned genome sequence containing only letters (A, T, C, G, etc.).
    """
    with open(file_path, 'r') as file:
        genome = file.read().strip()

    # Remove non-alphabet characters using regex
    genome = re.sub(r'[^a-zA-Z]', '', genome)

    return genome

# Example usage:
# file_path = "genome.txt"
# genome_sequence = read_genome_int(file_path)
# print(genome_sequence)
