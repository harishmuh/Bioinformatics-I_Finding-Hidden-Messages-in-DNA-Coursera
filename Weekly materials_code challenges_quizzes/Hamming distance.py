# Hamming distance function
def hamming_distance(p, q):
    """Computes the Hamming distance between two equal-length strings p and q."""
    if len(p) != len(q):
        raise ValueError("Strings must be of equal length")

    return sum(1 for x, y in zip(p, q) if x != y)

# Example usage:
p = "GGGCCGTTGGT"
q = "GGACCGTTGAC"
print(hamming_distance(p, q))  # Output: 3

# Quiz
p = 'TCGTTGTCGATAGACTCTTCGTGTCTGAGTTGAGGAATCATCTAGTTGAAAACAAAAAACGCGCGACCCGCCCTAGATCAGGCGCCCTTGCAAATTATACCTTCTGATTTATCGTGACACACACGAATAACTATACCGAGCCTATGGCGGGGTAGTACCCGCGTGGGCGTACCCCAGGGGGTTAGGACGGAGGCTCCTTCGTGTATTTTCGTATTGCCATTCTTGGACGCTCACGGAGTCTGAAGTATAAACACGTGAGTTGACATTAAAACGCTAATCCAAGTGATTCCGGCACTACGAATACTGTATAATCTATTACAGGCAAGCGATTATTAATATCTCTCTTCTGGGTCTCTGGGACTCTAGGCGACACTTTCGATCGCTGTCACAGTCCTACCTCTAACATTTGCGAGTATCATCCAGGCGCGTGGAGTTCGACGGTAATCGCTGAACCTCGGTGGAGGCGGAAGCTTCCTTCTGCGACATGCTTTTGAGCATCTGATCGGTGGTGCGCCGCGAGAATAGGACATACCTCTTCTCGTTATAACGAGGATAGCACAAACGCTCAAAACACCCAACTAGTTTTTCCTGGAGATATTTCGTTAGAAGCAACCCAGGAGGCTACGGTGCTCATTACAACCCGTGAGCATGGATATGGATAAGATTTGCGTCCCTACAATTTCCCTCATCAGAAATTTATTGTCAGGTATCAAGCCACGCTCACCGGTCGATCTGTGAGACATGTCACGATCCCGTGATAGGTAAAATAGTTTTCTAGTAGGCAGCCGTAGGTGGATTATGATTCACGATAAGCAATTGACGTTATGTAGGCCACACAGATGTGCGTCAGTTATGAGTAATCGTGTCTAGGCACCTGTGGGTGCTATACCTACAAGTGCCTTGTGTTATACATTATAGAAGGGAAAATAGTCCGGCGGCTATTTAAGTTCCAAAAGGTAATTAGGACCATTATGTAAGTAGGCGTGCGGCCAACGGCCGAAACGGTTTTTTCGTATGCTGCCGTATCTGATTATGATAACTGGTTGAGGTTCTCCTCGTTCAAGATTGGGAGAGTATACGATGCAGATCATAACATG'
q = 'GAACTCTGTTCGACTAGGAGCGTGTAATAGTCCTTTGTGCAACATCCATGTACTTTCCTTCGCTCAACTTTGGAGCGTATCATCTGCTCCGTAGTAGGGCACGGGCGCAGTCGCGTTAACTGTTATTTAACCGGATGCACTTGCAGTTCTCTCAAGAAGATCGCAGTGTTAGCCACCTCTCGAACAGTAAGAGGACGTAATAAGGGGGACCTCGACGGAAAGCCTCCTGTGCTGCAGTCCGGGTGCAGGCGACCCGGGGTAGGTGAGAGCTGGTACTGGGAATCGGATGTGCCCGTAAAATGTCGTTCAGCCTTGCATGGAACTAACGGACTAAAAGTACTTCCTGTTTGTGGGGGTCCCACAACATGATAGATAGCGTTTTTAATACATCTAAAGCATTTCTAGGTTTTCCTCGTGATCCTAAGTAATGGGTTACTCTCCTCCGGCGCTCGAGGTATCCTAACTGATATTGGAAGGAGCCGTCCCATCTAGTTAGGCCTCGTATAGTCTTGCGGAAACAGGGATCGCACATTCCTAAGCGAGATTGGTGTTCTCGACGTGATCACATAAACGCTCGCCTGCGCTCAGGGCAATGGGAGATTGACCATCAGAACGTTGATTATGAGTCACTTACTGACTGCAGACGCGGTACCCGGTGAACGATAGCCCCCTTGGGTGTCGTTGCCTTGCCGACCATGTTGGTGCGCATCTCCCCAGGTCTTACAGGGCCCGAAATGTATGTATTCTGGACTTGCGTATTACGACACCGACCGCCCGATTACGTATTGCAGCATAAGGCCTGGGATCAGACGCATGGGAATGAAATACATCACAACGTAAATGGCAGAGGTTAGGATAGCCTACACAATTAAAAACATTCTGCCGGCGAAAAGACTCAAAGGTCACAAAGAGGTTTCTACGGTTGCCCACATCAAGATTTATGTTTGCGGTTGCGGGCCCGGCGTGCGTTCAAGCCCCAAATCGCACTGTCAGCCTTACAATTGATTGAATGACGTGTATATACAAACTGCACTGCTACGTCATTTTCTAGACTTTTCCTTTTTCCGTATTCACGATCAGTTCACTACACTTCTGTT'

print(hamming_distance(p, q)) # Output: 837
