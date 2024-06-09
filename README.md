> Rare Diseases Hackathon 2024 (https://www.rarediseaseaihackathon.org/)

# Team_Intronic_HPP

#### Download ALPL gene structure (exons/introns) [hg38] in FASTA from
   
https://genome.ucsc.edu/cgi-bin/hgGene?hgg_gene=ENST00000374840.8&hgg_chrom=chr1&hgg_start=21509422&hgg_end=21578410&hgg_type=knownGene&db=hg38#rnaStructure

- one FASTA file for all exons (with 100 bp upstream and 100 bp downstream)

- one FASTA file for all introns (with 100 bp upstream and 100 bp downstream)

Then split those multiple-FASTA into multiple FASTAs (one FASTA per exon / intron):

for exons FASTA: `awk '/^>/{s="ALPL_exon"++d".fasta"} {print > s}' ALPL_exons_flank100bp.fasta`

for introns FASTA: `awk '/^>/{s="ALPL_intron"++d".fasta"} {print > s}' ALPL_introns_flank100bp.fasta`

Note : useful https://github.com/stephenturner/oneliners


#### Download ClinVar results for ALPL gene in tabular from

https://www.ncbi.nlm.nih.gov/clinvar/?term=ALPL%5Bgene%5D&redir=gene

Create clinvar_results_trimmed.txt with columns [Name, Gene(s), Accession, GRCh38Location, Variant type]

Use `parse_clinvar.ipynb` to:
1. Parse ClinVar results - filter for ( Name = NM_00047, Gene(s) = ALPL, Variant type = single nucleotide variant ).
2. Create a FASTA file per intron / exon variant.
