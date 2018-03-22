import csv
import argparse


ap = argparse.ArgumentParser()
ap.add_argument('input', help='CDR3 file from BCRSEQ')
ap.add_argument('output', help='imrep  file with CDR3s')
args = ap.parse_args()

#Bioinformatics  25173419 2015 package http://sourceforge.net/projects/rpore/ 301 available https://sourceforge.net/p/rpore/wiki/Home/ 302


linkSet=set()

file=open(args.input,"r")
reader=csv.reader(file)
for line in reader:
    if line[3]!="abstractNotFound":
        linkSet.add(line[4])


print linkSet
print len(linkSet)


for l in linkSet


