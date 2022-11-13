#!/bin/bash

declare -a files;

files=("/etc/8V2L" "/mnt/c4ZX" "/mnt/D8B3" "/var/FHl1" "/opt/oiMO" "/opt/PFbD" "/media/rmfX" "/etc/ssh/SRSq" "/var/log/uqyw" "/home/v2Vb" "/X1Uy")

for i in "${files[@]}"
do
    ls -la "$i"
done
