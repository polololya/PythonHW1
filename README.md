## PythonHW1 Homework1 17-02-18 ( _Levenstein distance_ )

### Command line agruments:

-s --savehm Whether you need the heatmap to be saved to file\
-i --inputfile Link to your marvellous input file

### Workflow
Input has to be fasta file with at least to sequences.
* Programm creates square matrix with dimensions equal to a number of sequences in the input file. 
* It counts Levenstein distance between all sequences in pairs. More mismatches - bigger the score
* Fills the matrix with distances
* Result matrix is shown as a standart output. You can put it in a file via pipe 'Argparse.py | filename.txt'
* If you set savehm argument than it creates heatmap (matplotlib) and saves it as HWA.pdf file in workind directory

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
