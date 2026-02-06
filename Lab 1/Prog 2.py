from Bio.Seq import Seq

with open('APOE.fna', 'r') as f:
    fl=f.read()

my_dna = Seq(fl)

complement_dna = my_dna.complement()

print(f"Original DNA: {my_dna}")
print(f"Complement DNA: {complement_dna}")
