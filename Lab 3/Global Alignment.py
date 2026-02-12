from Bio import pairwise2

sequences = [
    "AGTACGCA",
    "TATGC",
    "ATGCGT",
    "AGTGC"
]

match_score = 1
mismatch_penalty = -1
global_gap_penalty = -1
local_gap_penalty = -1


for i in range(len(sequences)):
    for j in range(i+1, len(sequences)):
        print(f'Alignment bw sequences {sequences[i]}, {sequences[j]}, is: {pairwise2.align.globalxx(sequences[i], sequences[j], score_only = True)}')