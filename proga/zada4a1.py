# -*- coding: utf-8 -*-
short_dna = 'ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCATGGG'
g_number = (short_dna.count("G"))
c_number = (short_dna.count("C"))
overall_len = len(short_dna)
gc_content = g_number / overall_len + c_number / overall_len

print("GC content is: ", gc_content)

print("GC content is: ", gc_content * 100, "%")  # то же самое, только в процентах