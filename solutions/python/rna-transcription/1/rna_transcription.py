def to_rna(dna_strand):
    # Define the translation table
    table = str.maketrans('GCTA', 'CGAU')

    # Apply the translation to a string
    return dna_strand.translate(table)
