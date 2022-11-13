#!/bin/bash

declare -a files;

files=("/etc/8V2L" "/mnt/c4ZX" "/mnt/D8B3" "/var/FHl1" "/opt/oiMO" "/opt/PFbD" "/media/rmfX" "/etc/ssh/SRSq" "/var/log/uqyw" "/home/v2Vb" "/X1Uy")

target_sha="9d54da7584015647ba052173b84d45e8007eba94"

for i in "${files[@]}"
do
    this_sha=$(sha1sum "$i")
    if [ "$this_sha" == "$target_sha  $i" ]
    then
        echo "$i"
        echo "$this_sha"
    fi
done
