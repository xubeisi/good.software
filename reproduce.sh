# Average age of active software tools
cat *csv | grep -v timeout | grep -v broken | awk -F "," '{print 2018-$5}' | awk '{s+=$1} END {print s/NR}'


