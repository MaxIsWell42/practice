# DNA = A,C,G,T
# RNA = A,C,G,U

# https://exercism.io/my/solutions/30f5d04e2bba4f08a0bb350a29c9d8bc
# Given a DNA strand, return its RNA complement (per RNA transcription).


rna = []
def DNAConvert(dna):
    dna_upper = dna.upper()
    convert = {
        'G':'C',
        'C':'G',
        'T':'A',
        'A':'U'
    }
    for letter in dna_upper:
        letter = convert[letter]
        rna.extend(letter)
    return rna

if __name__ == "__main__":
    # We should get back ['A', 'C', 'U', 'G', 'C', 'U', 'G', 'A']
    test_input = "TGACGACT"
    print(DNAConvert(test_input))
    
    # Bad inputs
    # test_input = "321"
    # test_input = "LMAO"
    
    # Edge cases?
    # test_input = ""