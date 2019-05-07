#!/bin/bash
# We're cool, so we do a one liner to fetch data from sensor simulator
FILE1=$1

stty 115200 sane -echo -echok -icrnl -ixoff  -opost -onlcr time 3 min 0 < /dev/ttyPS0
stty -F /dev/ttyPS0 speed 115200 cs8 -cstopb -parenb

echo 'loserville' > /dev/ttyPS0 && timeout 6s cat < /dev/ttyPS0 > $FILE1
echo ' ' > /dev/ttyPS0

