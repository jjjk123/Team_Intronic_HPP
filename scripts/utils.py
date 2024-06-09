def read_fasta(file_name):
    '''
    arguments:
    - file_name: path to input FASTA file, type=str

    returns:
    - header: input FASTA header, type=str
    - sequence: input FASTA sequence, type=str
    '''
    sequence = ""

    with open(file_name, 'r') as f_fasta:
        header = f_fasta.readline()

        for line in f_fasta:
            sequence += line.replace('\n', '')
    
    return header, sequence   


def write_fasta(file_name, header, sequence):
    '''
    arguments:
    - file_name: type=str,
    - header: output FASTA header, type=str,
    - sequence: output FASTA sequence, type=str
    '''
    with open(file_name, 'w+') as f:
        f.write(header)
        f.write(sequence)


def find_struct(pos, struct_pos):
    '''
    arguments:
    - pos: genomic position, type=int
    - struct_pos: list of ALPL-specific genomic structures (exons/introns),
      with elements: (structure_name, start, end)

    returns:
    - struct: structure_name (e.g., "exon1"), type=str
    - start: start position of genomic structure, type=int
    '''
    for struct, start, end in struct_pos:
        if start <= pos <= end:
            return struct, start