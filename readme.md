

Steps to Run Traffic Dataset Collector

    Install ryu controller by "pip install ryu".

    Install mininet from its github (Mininet is a Network Emulator).

    Run controller.py on ryu by "ryu-manager controller.py"

    Run mininet Topology with "sudo python topology.py" The topology created by this command is custom topology with 10 switches and 4 hosts. Topology Tree looks like following.

                h1---s10---s3---s1---s2---s9---s2
                         \     /   \     /
                          s4          s6
                         /    \     /   \
                   h4---s2 -----s5 ------ s8---h3


    start xterm for all nodes using "xterm h1" on mininet console for each h1,h2,h3,h4

    Run script on each xterm example: on Node: h1 run "./script1.sh" on Node: h2 run "./script2.sh" on Node: h3 run "./script3.sh" on Node: h4 run "./script4.sh"

    After Process is completed files as name "h1file.txt" and "h2file.txt" are generated for each h1,h2,h3,h4 containing data about traffic at each node.

We can change status the links of Network topology by "link S1 s2 down" or "link s6 s8 up" in order to provide variance to the data collected.

We can scale this thing at a very large scale and can collect data of a very complex Network topology. The Large data collected can be very useful to increase efficiency of network by creatin a Machine Learning Model and training through that large data.

I have pre collected a lot of data for around 700 MegaBytes of data. 
Can refer to data at this link  https://drive.google.com/file/d/10I9oGn3WJjIjgbCgr9wuS65jv4VLJp59/view?usp=sharing=
