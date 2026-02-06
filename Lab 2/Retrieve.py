# Importing the Entrez module from Biopython this helps in downloading the sequences from NCBI
from Bio import Entrez

Entrez.email='ankurde2005@gmail.com'  # Always tell NCBI who you are

search_results=Entrez.read(Entrez.esearch(db='nucleotide', term='Epidermal Growth factor receptor[Title]', retmax=10)) # If you put the term in NCBI the first 10 Id's should match

IDs = search_results['IdList']# Fetch retrieved ID's to ensure they were fetched correctly
print("Retrieved IDs: "+ str(IDs))# Print retrieved ID's to ensure they were fetched correctly

with open('egfr.fna', 'w') as output_file:
    for ID in IDs:
        try:
            sequence=Entrez.efetch(db='nucleotide', id=ID, rettype='fasta', retmode='text').read()
            output_file.write(sequence+'\n')
        except Exception as e:
            print(f"An error occurred with ID {ID}: {e}")


print("Sequence retrival and file writing complete")