from Bio import SeqIO
for record in SeqIO.parse("L.fasta","fasta"):
    print(len(record.seq))
