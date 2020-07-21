#!/bin/bash

iperf -s -u -i 1 -p 5001 > h1file.txt &
time=16500
for((i=1;i<80;i++))
do
  time=$((time-5))
  iperf -c 10.0.0.4 -p 5004 -u -t $time
  iperf -c 10.0.0.2 -p 5002 -u -t $time
  iperf -c 10.0.0.3 -p 5003 -u -t $time
done
