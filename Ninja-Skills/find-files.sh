#!/bin/bash

declare -a files;

files=("8V2L" "bny0" "c4ZX" "D8B3" "FHl1" "oiMO" "PFbD" "rmfX" "SRSq" "uqyw" "v2Vb" "X1Uy")

for i in "${files[@]}"
do
find / -type f -name "$i" 2>/dev/null
done