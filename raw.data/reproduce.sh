cd abstractLinks 
grep "" *txt | awk '{if ($3!="" && $3!="NoLink") print}' | sed 's/_linkStatus.txt:/\t/' >../abstractLinks.prepared.tsv
cd ..

cd bodyLinks
grep "" *txt | awk '{if ($3!="" && $3!="NoLink") print}' | sed 's/_linkStatus.txt:/\t/' >../bodyLinks.prepared.tsv

cd ..

#separate analysis for abstract
# separate for body
# merge. filter based on Angela data
# make sure not to have dublicates
