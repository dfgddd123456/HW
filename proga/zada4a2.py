# -*- coding: utf-8 -*-
short_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
comp_dna = short_dna.translate(str.maketrans('ACTG', 'TGAC'))
print(comp_dna)