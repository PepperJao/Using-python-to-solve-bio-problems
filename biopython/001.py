from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC

for record in SeqIO.parse('A.fasta',"fasta"):
    seq_r = record.seq
    my_seq = Seq(str(seq_r),IUPAC.unambiguous_dna)
    for index,letter in enumerate(my_seq):
        print(index,letter)
    

'''for index, letter in enumerate(seq_record):
    print("%i%s"%(index,letter))
'''

