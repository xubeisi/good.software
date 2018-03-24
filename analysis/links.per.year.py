import csv



#link,status.detailed,status.general,journal,year
#http://cottonevolution.info,redirected,good,BMC_Genomics,2007

dict={}
dict_year={}
dict_year_timeout={}
dict_year_broken={}
dict_year_redirect={}

file=open("../abstractLinks.csv")
reader=csv.reader(file)
next(reader,None)
for line in reader:
    link=line[0]
    year=int(line[4])
    dict_year[year]=0
    dict_year_timeout[year]=0
    dict_year_broken[year] = 0
    dict_year_redirect[year] = 0

    dict[link]=line

file.close()

file = open("../bodyLinks.csv")
reader = csv.reader(file)
next(reader, None)
for line in reader:
    link = line[0]
    dict[link] = line
    year = int(line[4])
    dict_year[year] = 0
    dict_year_timeout[year]=0
    dict_year_broken[year] = 0
    dict_year_redirect[year] = 0

file.close()


print ("Total number of links", len(dict.values()))




for key,value in dict.items():
    year=int(value[4])
    status=value[1]
    if year<=2005:
        year=2005
    dict_year[year]+=1
    if status=='redirected':
        dict_year_redirect[year] +=1
    elif status=='timeout':
        dict_year_timeout[year] +=1
    elif status=='broken':
        dict_year_broken[year] +=1


fileOut=open("results.links.type.per.year.csv","w")
fileOut.write("year,status,prc\n")

for y in range(2005,2018):
    #print (dict_year_broken[y],float(dict_year[y]))
    prc_broken=dict_year_broken[y]/float(dict_year[y])
    prc_timeout = dict_year_timeout[y]/float(dict_year[y])
    prc_redirected = dict_year_redirect[y]/float(dict_year[y])
    prc_good=1-prc_broken-prc_timeout-prc_redirected

    fileOut.write(str(y) + ",0.broken," + str(prc_broken))
    fileOut.write("\n")
    fileOut.write(str(y)+",1.timeout,"+str(prc_timeout))
    fileOut.write("\n")
    fileOut.write(str(y) + ",3.redirected," + str(prc_redirected))
    fileOut.write("\n")
    fileOut.write(str(y) + ",2.good," + str(prc_good))
    fileOut.write("\n")


fileOut.close()