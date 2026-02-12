# 2. Write a code to apply Brute Force algorithm using Leaderboard Approach for first 5 nucleotides of the selected sequence
# NRP 1 - Neurophilin 1

import itertools

# Standard integer amino acid masses
AA_MASS = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
    "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
    "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186
}

AMINO_ACIDS = list(AA_MASS.keys())


def read_fasta(filename):
    seq = ""
    with open(filename) as f:
        for line in f:
            if not line.startswith(">"):
                seq += line.strip()
    return seq


def linear_spectrum(peptide):
    prefix = [0]
    for aa in peptide:
        prefix.append(prefix[-1] + AA_MASS[aa])

    spectrum = [0]
    for i in range(len(peptide)):
        for j in range(i + 1, len(peptide) + 1):
            spectrum.append(prefix[j] - prefix[i])

    return sorted(spectrum)


def peptide_mass(peptide):
    return sum(AA_MASS[a] for a in peptide)


def score(peptide, spectrum):
    theo = linear_spectrum(peptide)
    s = spectrum.copy()
    sc = 0
    for m in theo:
        if m in s:
            sc += 1
            s.remove(m)
    return sc


def brute_force_reconstruction(spectrum, length):
    target_mass = max(spectrum)
    results = []

    for prod in itertools.product(AMINO_ACIDS, repeat=length):
        pep = "".join(prod)
        if peptide_mass(pep) == target_mass:
            if linear_spectrum(pep) == spectrum:
                results.append(pep)

    return results


def expand(peptides):
    out = []
    for p in peptides:
        for aa in AMINO_ACIDS:
            out.append(p + aa)
    return out


def trim(leaderboard, spectrum, N):
    scored = [(p, score(p, spectrum)) for p in leaderboard]
    scored.sort(key=lambda x: x[1], reverse=True)

    if len(scored) <= N:
        return [p for p, _ in scored]

    cutoff = scored[N - 1][1]
    return [p for p, s in scored if s >= cutoff]


def leaderboard_sequencing(spectrum, N=50):
    leaderboard = [""]
    leader = ""
    parent_mass = max(spectrum)

    while leaderboard:
        leaderboard = expand(leaderboard)
        new_board = []

        for p in leaderboard:
            m = peptide_mass(p)
            if m == parent_mass:
                if score(p, spectrum) > score(leader, spectrum):
                    leader = p
            if m <= parent_mass:
                new_board.append(p)

        leaderboard = trim(new_board, spectrum, N)

    return leader


if __name__ == "__main__":
    fasta_file = "gene.fna"

    sequence = read_fasta(fasta_file)
    length = 5
    first5 = sequence[:length]

    print("Original first 7 amino acids:", first5)

    spectrum = linear_spectrum(first5)
    print("\nGenerated spectrum:")
    print(spectrum)

    print("\nBrute force reconstruction:")
    brute = brute_force_reconstruction(spectrum, length)
    print(brute)

    print("\nLeaderboard reconstruction:")
    leader = leaderboard_sequencing(spectrum, N=length)
    print(leader)
