import csv
import argparse
import sys
from collections import Counter

def is_number(var):
    try:
        if var == int(var):
            return True
    except Exception:
        return False

# 0 - timeout, -1 broken, 2 - redirection, 3 - normal
def classify_link(n):
    # broken link >=400
    # -1 - tme out
    # [300,400) - redirection
    if n==-1:
        return 0
    elif n>=400:
        return -1
    elif n>=300 and n<400:
        return 2
    else:
        return 3





#####################################
ap = argparse.ArgumentParser()
ap.add_argument('input', help='CDR3 file from BCRSEQ')
ap.add_argument('manual', help='CDR3 file from BCRSEQ')
ap.add_argument('output', help='imrep  file with CDR3s')
args = ap.parse_args()





#List of links cheked manually
#Journal,ID,Year,Keyword,Link,Status,manual.flag
#Bioinformatics,18940825,2008,available,http://sitepredict.org/,-1,0

#0 means is it really -1 status

goodLinks=set()
file=open(args.manual)
reader=csv.reader(file)
next(reader,None)
for line in reader:
    if line[6]=='1':
        goodLinks.add(line[4])


print ("Number of manually identified good links",len(goodLinks))



linkSet=set()
dict_status={}
dict_year={}
dict_journal={}

n_2_abstracts=0
n_1_abstract=0
total=0

file=open(args.input,"r")
reader=csv.reader(file)


#['PLoS_Comput_Biol', '19381256', '2009', 'null', 'http://purl.org/net/cito/', '502',
# 'available', 'http://dx.doi.org/10.1371/journal.pntd.0000228.x001', '303']

for line in reader:



    total+=1

    if line[3]!="abstractNotFound":

        link_final=''
        status_final=''

        if line[5]!='':
            if line[5][len(line[5])-1].isdigit():

                journal = line[0]
                year = int(line[2])

                n_1_abstract+=1
                link1 = line[4]

                # check if the link is not part of good links
                if link1 in goodLinks:
                    status1=200 # normal link
                else:
                    status1 = int(line[5])




                if line[8] != '':
                    link2=line[7]
                    #['PLoS_Comput_Biol', '19381256', '2009', 'null', 'http://purl.org/net/cito/',  '502', 'available',
                    # 'http://dx.doi.org/10.1371/journal.pntd.0000228.x001', '303']

                    #check if the link is not part of good links
                    if link2 in goodLinks:
                        status2 = 200  # normal link
                    else:
                        status2 = int(line[8])

                    n_2_abstracts+=1

                    if classify_link(status1)==classify_link(status2):

                        link_final=link1
                        status_final=classify_link(status1)

                    else:
                        if classify_link(status1)==3: #if first is normal, it doesn;t matter what is the second one
                            link_final = link1
                            status_final = classify_link(status1)
                        elif classify_link(status1)==2: # if fist is redirected, that only in case second is normal, we will assign second
                            if classify_link(status2)==3:
                                link_final = link2
                                status_final = classify_link(status2)
                            else:
                                link_final = link1
                                status_final = classify_link(status1)
                        elif classify_link(status2)==2 or classify_link(status2)==3:
                            link_final = link2
                            status_final = classify_link(status2)
                        else:
                            link_final = link1
                            status_final = classify_link(status1)
                            #print (status1,status2,classify_link(status1),classify_link(status2))
                else: # link is just one in the abstract
                    link_final = link1
                    status_final = classify_link(status1)


                #after we decided 1st or 2nsd link to use
                linkSet.add(link_final)
                dict_status[link_final] = status_final
                dict_year[link_final] = year
                dict_journal[link_final] = journal

statusSet=set()
journalSet=set()
yearSet=set()


dict=Counter(dict_journal.values())
print (dict)


#journals with at list 50 links
journalSet_currated=set()

dict2={}

for key,value in dict.items():
    if value>50:
        journalSet_currated.add(key)
        dict2[key]=[0,0,0,value]

statusSet=set(dict_status.values())
journalSet=set(dict_journal.values())
yearSet=set(dict_year.values())


print (statusSet)
print (journalSet)
print (yearSet)


fileOut=open(args.output,"w")
fileOut.write("link,status.detailed,status.general,journal,year\n")

for l in linkSet:


    if dict_journal[l] in journalSet_currated:
        status=dict_status[l]
        type1=''
        type2=''
        if status==0:
            type1='timeout'
            type2='timeout'
            dict2[dict_journal[l]][0]+=1


        elif status==-1:
            type1='broken'
            type2='broken'
            dict2[dict_journal[l]][1]+=1
        elif status==2:
            type1='redirected'
            type2='good'
            dict2[dict_journal[l]][2]+=1
        else:
            type1 = 'good'
            type2 = 'good'
            dict2[dict_journal[l]][2]+=1




        fileOut.write(l+","+type1+","+type2+","+dict_journal[l]+","+str(dict_year[l]))
        fileOut.write("\n")


print ("total,n_1_abstract,n_2_abstracts")
print (total,n_1_abstract,n_2_abstracts)
print ("0 - timeout, -1 broken, 2 - redirection, 3 - good")


fileOut.close()

fileOut=open("Prc.abstract.links.per.journal.csv","w")
fileOut.write("Journal, time,out,broken,good\n")

for key,value in dict2.items():
    sum=float(value[3])
    time_out=value[0]/sum
    broken=value[1]/sum
    good=value[2]/sum
    fileOut.write(key+","+str(time_out)+","+str(broken)+","+str(good))
    fileOut.write("\n")

fileOut.close()



print ("DONE!")

