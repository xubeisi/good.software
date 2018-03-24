cd abstractLinks 
grep "" *txt | awk '{if ($3!="" && $3!="NoLink") print}' | sed 's/_linkStatus.txt:/\t/' >../abstractLinks.prepared.tsv
cd ..

cd bodyLinks
grep "" *txt | awk '{if ($3!="" && $3!="NoLink") print}' | sed 's/_linkStatus.txt:/\t/' >../bodyLinks.prepared.tsv

cd ..

#abstracts ----
awk '{print $1","$2","$3","$4","$5","$6","$7","$8","$9}' abstractLinks.prepared.tsv > abstractLinks.prepared.clean.tsv
python prepare.data.py abstractLinks.prepared.clean.tsv ../manual.evaluation/manual.test.csv ../abstractLinks.csv 0

#body links
awk '{print $1","$2","$3","$4","$5","$6","$7","$8","$9}' bodyLinks.prepared.tsv >bodyLinks.prepared.clean.tsv
python prepare.data.py bodyLinks.prepared.clean.tsv ../manual.evaluation/manual.test.csv ../bodyLinks.csv 1




#separate analysis for abstract
# separate for body
# merge. filter based on Angela data
# make sure not to have dublicates
