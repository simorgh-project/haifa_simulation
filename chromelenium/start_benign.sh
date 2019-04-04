#!/bin/bash

# get the url lists
input=$1
process_no=$2
webdriver=$3

if ["$input" = ""]; then
	echo "Please specify the input file path: "
	read input
fi

if ["$process_no" = ""]; then
	echo "Please specify the number of processes: "
	read process_no
fi

if ["$webdriver" = ""]; then
	echo "Please specify your webdriver: "
	read webdriver
fi

echo "Your input file:" $input
echo "Number of processes:" $process_no

# Get the number of lines
url_no=`awk 'END{print NR}' $input`

# Split the input file according to the number processes
line_no=0 
cat urls.txt | while read line
do
	file_no=$((line_no % $process_no));  
	echo $line >> part_$file_no.txt;  
	line_no=`expr $line_no + 1`;
done  

# nohup processes
for((i=0;i<$process_no;i++));  
do
file=part_$i.txt
nohup python3 -u ./randomvisit.py --driver $webdriver --file $file > log_$i.txt 2>&1 &
done
