def parseAltmetricData(filename):

    parsedData = {}

    inputfile = open( filename, 'r' )

    # skipping first row
    inputfile.readline()

    for line in inputfile:

        lineSplit = line.split('\n')[0].split('[')

        ls_comma  = lineSplit[0].split(',')
        pmid      = int( ls_comma[0] )
        parsedData[pmid] = {}

        score     = float( ls_comma[1] )
        parsedData[pmid]['score'] = score

        numReaders = int( ls_comma[2] )
        parsedData[pmid]['numReaders'] = numReaders

        cited     = int( ls_comma[3] )
        parsedData[pmid]['cited'] = cited

        scopus = lineSplit[1][:-1]
        parsedData[pmid]['scopus'] = scopus

    return parsedData
