#!/bin/bash

tms=1
sizes=(128 512 1024 1472)

if [ -z "$1" ] || [ -z "$2" ]
then
	echo "Must specify an ip address"
	echo "./iperf3.sh <addr> <title> <how many iterations of every test : optional>"
fi

if [ $3 ]; then
	times = $3
fi

for s in ${sizes[@]}; 
do
	for ((c = 1; c<=$tms; c++))
	do
		echo "$s - $c"
		iperf3 -c $1 --set-mss $s -T $s$2 -R
	done
done


