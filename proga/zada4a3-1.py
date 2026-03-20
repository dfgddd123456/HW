# -*- coding: utf-8 -*-
gen_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = gen_dna[0:63:1]
exon2 = gen_dna[91::1]
intron = gen_dna[63:91:1]

print("Coding part: ", exon1 + exon2)
print("Intron is: ", intron)