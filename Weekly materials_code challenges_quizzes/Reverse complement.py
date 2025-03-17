# Defining Reverse Complement function
def ReverseComplement(strand):
    Reverse_Complement=[]
    reverse_strand=strand[::-1]
    for i in reverse_strand:
        if i == 'A':
            Reverse_Complement.append('T')
        if i =='T':
            Reverse_Complement.append('A')
        if i=='G':
            Reverse_Complement.append('C')
        if i=='C':
            Reverse_Complement.append('G')
    return ''.join(Reverse_Complement)

# Example usage
strand = 'AAAACCCGGT'
print(ReverseComplement(strand) # Output: ACCGGGTTTT
