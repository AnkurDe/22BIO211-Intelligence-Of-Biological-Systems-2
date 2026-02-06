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
print(transcription(dna.replace('\n', ''))[:30])
