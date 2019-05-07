# Get data from simulator
We wrote a very simple bash script to get sensor data from our simulator. This can be run with
`./getdata.sh [dest]`
[dest] is the location to save data to. 

The simulator is buggy, in that we cannot send "loserville" right after sending it without spacing. 
But sending it with spacing will not initiate the data stream, therefore we send empty string afterards to 
"clear" the input for the simulator
