def to_protein(sequence: str) -> str:
    # Has the one dictionary that stores conversion
    rna_ammino = {
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "UGU": "C", "UGC": "C",
        "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E",
        "UUU": "F", "UUC": "F",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
        "CAU": "H", "CAC": "H",
        "AUU": "I", "AUC": "I", "AUA": "I",
        "AAA": "K", "AAG": "K",
        "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "AUG": "M",
        "AAU": "N", "AAC": "N",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "UGA": "Stop", "UGG": "W",
        "UAU": "Y", "UAC": "Y",
        "UAA": "Stop", "UAG": "Stop",
    }

    ammino=str()

    while sequence:
        try:
            a, b, c, *sequence = sequence
        except Exception as E:
            break
        ammino = ammino + rna_ammino.get(a+b+c, 'X')

    return ammino+'*'

def transcription(dna: str):
    dct = {
        'A': 'T',
        'T': 'U',
        'G': 'C',
        'C': 'G'
    }
    temp = ''
    for c in dna:
        temp = temp + dct[c]

    return temp


with open('gene.fna', 'r', encoding='utf-8') as output_file:
    lines = output_file.readlines()

dna = ''
for line in lines:
    if not line.startswith('>'):
        dna += line

# print(dna)
print(to_protein(transcription(dna.replace('\n', ''))))
