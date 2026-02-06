from Bio.Seq import Seq

with open('cftr.fna', 'r') as f:
    fl=f.read()

my_dna = Seq(fl)
print(my_dna.transcribe())