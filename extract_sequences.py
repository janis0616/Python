#!/usr/bin/env python

#extract sequences from a genome, based on the start and stop coordinates
def getsequences(genome, coordinates):
    #open the coordinates file
    Positions = open(coordinates)
    #read each line of the coordinates file into a list
    Positions_list = Positions.readlines()
    #start a for loop with the positions list to extract each sequence based on its coordinates
    for position in Positions_list:
        #open the output file [append]
        Output = open("output.txt", "a")
        #strip the newline from the end of each line of the positions list
        strip_positions = position.rstrip("\n")
        #split each line of the positions list based on the comma 
        split_positions = strip_positions.split(",")
        #define the start and stop coordinates as the [integer] first and second values in each line of the positions list
        start = int(split_positions[0])
        stop = int(split_positions[1])
        #open and read the genome fasta
        DNA = open(host_genome)
        DNA_read = DNA.read()
        #define each prophage as the start minus one to the stop positions, read from the genome file
        eachsequence = DNA_read[(start - 1):stop]
        #append each sequence to the output file, with a newline at the beginning and end of each sequence
        Output.write("\n" + eachsequence + "\n")
        #close all the files
        Output.close()
        DNA.close()
    Positions.close()
#call the function, using the genome file and the coordinates file
getsequences("example_genome.fasta","coordinates.txt")


