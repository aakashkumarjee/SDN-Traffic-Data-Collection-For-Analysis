#!/bin/bash

iperf -s -u -i 1 -p 5002 > h2file.txt &
time=3
for((i=1;i<75;i++))
do
  time=$((time+6))
  iperf -c 10.0.0.4 -p 5004 -u -t $time
  iperf -c 10.0.0.3 -p 5003 -u -t $time
  iperf -c 10.0.0.1 -p 5001 -u -t $time
done
