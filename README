Download ALPL gene structure (exons/introns) [hg38] in FASTA from
https://genome.ucsc.edu/cgi-bin/hgGene?hgg_gene=ENST00000374840.8&hgg_chrom=chr1&hgg_start=21509422&hgg_end=21578410&hgg_type=knownGene&db=hg38#rnaStructure
one FASTA record per region (exon, intron, etc.) with 100 bp upstream and 100 bp downstream

# split multiple-FASTA into multiple FASTAs
# awk '/^>/{s="ALPL_exon"++d".fasta"} {print > s}' ALPL_exons_flank100bp.fasta
# useful: https://github.com/stephenturner/oneliners


Download ClinVar results for ALPL gene in tabular from
https://www.ncbi.nlm.nih.gov/clinvar/?term=ALPL%5Bgene%5D&redir=gene

Create clinvar_results_trimmed.txt with columns [Name, Gene(s), Accession, GRCh38Location, Variant type]

Parse clinvar_results_trimmed.txt using parse_clinvar.ipynb, filter for: 
1. Name = NM_00047
2. Gene(s) = ALPL
3. Variant type = single nucleotide variant