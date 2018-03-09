#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from Bio import SeqIO
import itertools as itr
import argparse


def Levdist(x,y, dictio): #function for matrix for levenshtein distance between sequence x & sequence y
    D = np.zeros((len(x) + 1,len(y) + 1)) #create empty matrix and fill the first row and column
    for i in range(len(x) + 1):
        D[i,0] = -i
    for i in range(len(y) + 1):
        D[0,i] = -i
    
    for i in range(1, len(x) + 1): #fill the rest of the cells
        for j in range(1, len(y) + 1):
            dHor = D[i,j-1] - 10
            dVer = D[i-1,j] - 10
            if x[i-1] == y[j-1]:
                dDiag = D[i-1,j-1] + 5
            else:
                fee = dictio[((str(x[i-1]),str(y[j-1])))]
                dDiag = D[i-1,j-1] + fee
            D[i,j] = max(dHor, dVer, dDiag)
    return(D[-1,-1])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Needleman-Wunsch Algorithm')
    parser.add_argument('-s', '--savehm', help='Wheather you need the heatmap to de saved to file', action='store_true')
    parser.add_argument('-i', '--inputfile', help='Link to your input file', type = str)
    args = parser.parse_args()
    
    
    Nucl = set('AGCT') #set fees dictionary for substitutions. Fees are just random numbers in this case. For more accurate results use matrix from Bio.Subsmat
    Fees = {}
    j = -5
    for i in itr.combinations(Nucl,2):
        b = (i[1],i[0])
        d = {b : j}
        c = {i : j}
        m = {('G','G'): 5,('C','C'): 5, ('A','A'): 5, ('T','T'): 5}
        Fees.update(c)
        Fees.update(d)
        Fees.update(m)
        j -= 1
    
    
     
    with open(args.inputfile, "r") as file: #creating a list of sequences for subsequent analysis
        list_seq = []
        for record in SeqIO.parse(file, "fasta"):
            list_seq.append(str(record.seq))
        
    Distances = np.zeros((len(list_seq),len(list_seq))) #calculating levenshtein distance for each pair of sequences and creating the matrix of distances
    for i in range(len(list_seq)):
        for j in range(len(list_seq)):
            Distances[i,j] = Levdist(list_seq[i],list_seq[j], Fees)
       
    print(Distances)

    if args.savehm:
        plt.imshow(Distances, interpolation='nearest'); #Heatmap
        plt.colorbar(orientation='vertical')
        plt.title('Similarity scores between sequences in your input file')
        plt.savefig('HWA.pdf')
