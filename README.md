## PythonHW1 Homework1 17-02-18 ( _Levenstein distance_ )

### Command line agruments:

-s --savehm Whether you need the heatmap to be saved to file\
-i --inputfile Link to your marvellous input file

### Usage example

``` $ python Levenstein-distance-counter.py -i filename.fa -s```

### Workflow
Input has to be fasta file with at least to sequences.
1. Programm creates square matrix with dimensions equal to a number of sequences in the input file. 
2. It counts Levenstein distance between all sequences in pairs. More mismatches - bigger the score
3. Fills the matrix with distances
4. Result matrix is shown as a standart output. You can put it in a file via pipe 'Argparse.py | filename.txt'
5. If you set savehm argument than it creates heatmap (matplotlib) and saves it as HWA.pdf file in workind directory

### Required packages
* matplotlib
* numpy
* biopython
* itertools
* argparse

### Example of an output
* Distances matrix:
```
[[ 75.  83.  88.  84.]
 [ 83.  80.  81.  86.]
 [ 88.  81.  91.  84.]
 [ 84.  86.  84.  80.]]
```
* Heatmap:\
![](https://pp.userapi.com/c831508/v831508933/93fec/UShjFNSFTdo.jpg)

### Things to be improved
* Ability to set output file name
* Building an alignment
