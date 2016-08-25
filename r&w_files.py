import collections
population_dict = collections.defaultdict(int)  # create a dict with continent as key and population as value

'''To read in a file, we don't have to import any packages, we just call the built-in function open(). The basic usage is:
with open('path/to/filename', 'rU') as inputFile:
    process the inputFile here
    more processing
    after we stop indenting, the file is closed! '''

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)                        #remove the header and assign it to a variable
    for line in inputFile:                          #for each line in the inputfile
        line = line.rstrip().split(',')             #rstrip() removes any trailing or leading spaces & split () performs a text to columns delimit split to create multiple columns
        line[5] = int(line[5])                      #changed the population in line 5 from a string to a number
        if line[1] == 'Total National Population':  #there is overlap in the data. I just want to calculate total population
            population_dict[line[0]] += line[5]     #create a dict with continent as key and population as value and add the populations of rural and urban

with open('national_population.csv', 'w') as outputFile:   #opens the file in write mode
    outputFile.write('continent,2010_population\n')        #write a header line into the file witht he column headers and the write() method
    
    for k, v in population_dict.iteritems():        #write the rest of the data to file with a loop. The function iteritems() iterates through each key-value pair in the dictionary
        outputFile.write(k + ',' + str(v) + '\n')   #output the continent(k) and convert the total population(v) into a string. 