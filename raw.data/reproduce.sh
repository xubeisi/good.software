cd abstractLinks 
grep "" *txt | awk '{if ($3!="" && $3!="NoLink") print}' | sed 's/_linkStatus.txt:/\t/' >../abstractLinks.prepared.tsv
cd ..

cd bodyLinks
grep "" *txt | awk '{if ($3!="" && $3!="NoLink") print}' | sed 's/_linkStatus.txt:/\t/' >../bodyLinks.prepared.tsv

cd ..

awk '{print $1","$2","$3","$4","$5","$6}' abstractLinks.prepared.tsv >abstractLinks.prepared.clean.tsv



#separate analysis for abstract
# separate for body
# merge. filter based on Angela data
# make sure not to have dublicates
