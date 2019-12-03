#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import MLE

# a random gene sequence in yeast for testing
sequence = "ATGGGTAAAGACAACAAGGAACATAAGGAAAGCAAAGAAAGCAAAACCGTAGACAACTATGAGGCCAGAATGCCTGCTGTGTTGCCATTCGCTAAACCATTGGCCTCTAAGAAACTAAACAAGAAGGTCTTGAAGACCGTGAAGAAGGCTTCCAAGGCCAAGAATGTTAAAAGAGGTGTCAAGGAAGTTGTCAAGGCCTTAAGAAAGGGTGAAAAAGGTTTAGTCGTCATCGCCGGTGACATTTCTCCAGCTGATGTTATTTCCCACATCCCAGTCTTATGTGAAGATCACTCTGTCCCATACATCTTCATACCTTCAAAGCAAGACTTAGGTGCCGCTGGCGCTACAAAAAGACCTACCTCAGTTGTCTTTATCGTCCCAGGTAGCAATAAGAAAAAAGATGGAAAAAATAAAGAAGAAGAATACAAGGAATCTTTCAACGAAGTTGTCAAAGAAGTTCAAGCTTTATGA"


def testGene(sequence):
    codonList = MLE.loadSequence(sequence)
    print("Condon List of Sequence, start and stop codon removed:")
    print(codonList)
    print("Codon List Length %d"%(len(codonList)))
    global_gene_expression = MLE.calPhiForGene(sequence)
    print("The estimated phi for entire gene is %f:" % (global_gene_expression))
    MLE_List = MLE.cal_mle_windows(sequence, windowSize=10)
    import matplotlib.pyplot as plt
    plt.plot(MLE_List)
    plt.xlabel("window location")
    plt.ylabel("MLE-Phi Estimate")
    plt.show()


testGene(sequence)
