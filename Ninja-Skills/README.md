https://tryhackme.com/room/ninjaskills


Answer the questions about the following files:

    8V2L
    bny0
    c4ZX
    D8B3
    FHl1
    oiMO
    PFbD
    rmfX
    SRSq
    uqyw
    v2Vb
    X1Uy

The aim is to answer the questions as efficiently as possible.


find / -type f -name 8V2L 2>/dev/null

find / -type f -group best-group 2>/dev/null





Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)
find / -type f -group best-group 2>/dev/null
/mnt/D8B3
/home/v2Vb



Which of these files contain an IP address?





Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94

Which file contains 230 lines?

Which file's owner has an ID of 502?


Which file is executable by everyone?

https://www.shellhacks.com/regex-find-ip-addresses-file-grep/



nano ninja-skills.sh

chmod u+x ninja-skills.sh

ls -la




#!/bin/bash

declare -a files;

files=(8V2L bny0 c4ZX D8B3 FHl1 oiMO PFbD rmfX SRSq uqyw v2Vb X1Uy)

for i in "${files[@]}"
do
find / -type f -name "$i" 2>/dev/null
done


/etc/8V2L
/mnt/c4ZX
/mnt/D8B3
/var/FHl1
/opt/oiMO
/opt/PFbD
/media/rmfX
/etc/ssh/SRSq
/var/log/uqyw
/home/v2Vb
/X1Uy





-rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /mnt/c4ZX
-rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /mnt/D8B3
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/FHl1
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/oiMO
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /opt/PFbD
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /media/rmfX
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /etc/ssh/SRSq
-rw-rw-r-- 1 new-user new-user 13545 Oct 23  2019 /var/log/uqyw
-rw-rw-r-- 1 new-user best-group 13545 Oct 23  2019 /home/v2Vb
-rw-rw-r-- 1 newer-user new-user 13545 Oct 23  2019 /X1Uy
