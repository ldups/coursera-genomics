# coursera-genomics
# Overview
This repository contains code I wrote while enrolled in the [Coursera Genomic Data Specialization](https://www.coursera.org/specializations/genomic-data-science). In particular, the repository contains code from Course 2 [Python for Genomic Data Science](https://www.coursera.org/learn/python-genomics?specialization=genomic-data-science) and Course 3 [Algorithms for DNA Sequencing](https://www.coursera.org/learn/dna-sequencing?specialization=genomic-data-science). The repository also contains several files provided by the course for use in practicals and homeworks, including FASTA and FASTQ files.

# Files Included
## Helper Methods

readFASTQ.py - function for reading sequences and qualities from FASTQ files

readFASTA.py- function for reading sequences from FASTA files

## Algorithms

recursiveEditDistance.py- algorithm for finding edit distance using recursion

pigeonHoleIndex.py- algorithms for matching allowing substitutions, including naive matching with substitution allowance and k-mer index adapted using pigeon hole principle

overlapPairs.py- algorithms for finding overlaps in strings and creating overlap map from set of strings

greedySCS.py- greedy shortest common superstring algorithm for genome assembly

greedySCSIndex.py- greedy shortest common superstring algorithm for genome assembly, adapted to use a k-mer index to increase efficiency

globalAlignment.py- algorithm for global alignment implementing penalty matrix based on biological context

dynamicEditDist.py- algorithm for calculating edit distance implementing dynamic techniques to improve efficiency

bruijnGraph.py- algorithm for creating De Bruijn graph from set of strings

## Practicals and Homeworks
practicalstringmanipulation.py- practical from Course 2, includes finding longest common prefixes of strings and reverse complements of DNA strings

practicalParseGenome.py- practical from Course 2, includes counting numbers of different bases in genome

findSpecies.py- homework from Course 2, uses Bio.Blast to identify unknown DNA

course2FinalExam.py- final exam from Course 2, finding lengths of reads, open reading frames, and repeats from FASTA file

practicalkMerIndex.py- practical from Course 3, includes creating and querying a k-mer index

practicalArtificialReads.py- practical from Course 3, generates short reads from genomes and implements naive exact matching algorithm to reassemble genome

practicalOverlapGraph.py- practical from Course 3, builds overlap graph from reads taken from FASTQ file

homework2NumComparisons.py- homework from Course 3, compares number of comparisons when finding pattern using naive exact matching vs. Boyer Moore pattern matching algorithm

assembleGenome.py- homework from Course 3, assembles genome from reads using shortest common superstring and greedy shortest common superstring algorithms

## Course Provided Resources
mysteryGenome.fq- mystery genome in the form of reads

ERR266411_1.for_asm.fastq- FASTQ file including reads and qualities

chr1.GRCh38.excerpt.fasta- FASTA file of chromosome excerpt

bm_preproc.py- preprocesses sequences to enable use of Boyer Moore pattern matching algorithm

