#!/bin/bash

iperf -s -u -i 1 -p 5003 > h3file.txt &
time=5
for((i=1;i<80;i++))
do
  time=$((time+5))
  iperf -c 10.0.0.4 -p 5004 -u -t $time -b 1000M
  iperf -c 10.0.0.2 -p 5002 -u -t $time -b 1000M
  iperf -c 10.0.0.1 -p 5001 -u -t $time -b 1000M
done
