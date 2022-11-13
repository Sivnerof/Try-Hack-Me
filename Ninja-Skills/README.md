# Ninja Skills

## Summary

[Ninja Skills](https://tryhackme.com/room/ninjaskills "Ninja Skills Room") is a Linux challenge that can be found on [TryHackMe](https://www.tryhackme.com "TryHackMe Website"). The challenge revolves around 12 files scattered throughout the file system in unknown locations and answering 6 questions about those files.

---

## Contents

* [Challenge](#challenge "Jump To Challenge")
* [Question 1](#question-1 "Jump To Question 1")
* [Question 2](#question-2 "Jump To Question 2")
* [Question 3](#question-3 "Jump To Question 3")
* [Question 4](#question-4 "Jump To Question 4")
* [Question 5](#question-5 "Jump To Question 5")
* [Question 6](#question-6 "Jump To Question 6")

---

## Challenge

Answer the questions about the following files:

* 8V2L
* bny0
* c4ZX
* D8B3
* FHl1
* oiMO
* PFbD
* rmfX
* SRSq
* uqyw
* v2Vb
* X1Uy

The aim is to answer the questions as efficiently as possible.

---

## Question 1

* Which of the above files are owned by the best-group group (enter the answer separated by spaces in alphabetical order).

    * D8B3 v2Vb

For this one I used the Linux ```file``` command to search for all files (```type -f```) where the group name was best-group (```-group best-group```) and redirected all errors to ```/dev/null```.

```
$ find / -type f -group best-group 2>/dev/null
/mnt/D8B3
/home/v2Vb
```

---

## Question 2

* Which of these files contain an IP address?

    * oiMO

At this point it becomes too tedious to keep running the same commands on different files in different locations. So I decided to write some very simple shell scripts to help out.

The first bash script I wrote ([find-files.sh](./find-files.sh "Bash script for finding file locations")) just finds all the file locations.

```bash
#!/bin/bash

declare -a files;

files=("8V2L" "bny0" "c4ZX" "D8B3" "FHl1" "oiMO" "PFbD" "rmfX" "SRSq" "uqyw" "v2Vb" "X1Uy")

for i in "${files[@]}"
do
    find / -type f -name "$i" 2>/dev/null
done
```

Output-

* /etc/8V2L
* /mnt/c4ZX
* /mnt/D8B3
* /var/FHl1
* /opt/oiMO
* /opt/PFbD
* /media/rmfX
* /etc/ssh/SRSq
* /var/log/uqyw
* /home/v2Vb
* /X1Uy

Then I wrote a bash script ([find-ip.sh](./find-ip.sh "Bash Script For Finding IP Addresses")) that iterates over those files and uses ```grep``` and regex to [match valid IPV4 addresses](https://www.shellhacks.com/regex-find-ip-addresses-file-grep/ "Article on IP regex").

```bash
#!/bin/bash

declare -a files;

files=("/etc/8V2L" "/mnt/c4ZX" "/mnt/D8B3" "/var/FHl1" "/opt/oiMO" "/opt/PFbD" "/media/rmfX" "/etc/ssh/SRSq" "/var/log/uqyw" "/home/v2Vb" "/X1Uy")

for i in "${files[@]}"
do
    if
        grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" "$i"
    then
        echo "$i"
    fi
done
```

Output -
* 1.1.1.1
* /opt/oiMO

---

## Question 3

* Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94?

    * c4ZX

For this one I wrote a script ([find-sha.sh](./find-sha.sh "Find file that matches sha script")) that iterates over the files in the array and runs the ```sha1sum``` command on each one, comparing it to the target sha.

```bash
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
```

---

## Question 4

* Which file contains 230 lines?

    * bny0

For this one I used another bash script ([find-lines.sh](./find-lines.sh "Script that checks if line count is equal to 230")) that checks if a files line count is equal to 230. But none of them are because a file is missing (bny0 doesn't exist on the system). So I put that as the answer and it worked.

```bash
#!/bin/bash

declare -a files;

files=("/etc/8V2L" "/mnt/c4ZX" "/mnt/D8B3" "/var/FHl1" "/opt/oiMO" "/opt/PFbD" "/media/rmfX" "/etc/ssh/SRSq" "/var/log/uqyw" "/home/v2Vb" "/X1Uy")

for i in "${files[@]}"
do
    line_count=$(wc -l < "$i")
    if [ "$line_count" == 230 ]
    then
        echo "$i"
    fi
done
```

---

## Question 5

* Which file's owner has an ID of 502?

    * X1uY

For this one I made the [ls-ln-files.sh](./ls-ln-files.sh "Script to list files in long format") script. It executes the ```ls -ln``` command on every file. Which gives us the answers we need for the last two questions.

```bash
#!/bin/bash

declare -a files;

files=("/etc/8V2L" "/mnt/c4ZX" "/mnt/D8B3" "/var/FHl1" "/opt/oiMO" "/opt/PFbD" "/media/rmfX" "/etc/ssh/SRSq" "/var/log/uqyw" "/home/v2Vb" "/X1Uy")

for i in "${files[@]}"
do
    ls -ln "$i"
done
```

Output -

```
-rwxrwxr-x 1 501 501 13545 Oct 23  2019 /etc/8V2L
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /mnt/c4ZX
-rw-rw-r-- 1 501 502 13545 Oct 23  2019 /mnt/D8B3
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /var/FHl1
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /opt/oiMO
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /opt/PFbD
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /media/rmfX
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /etc/ssh/SRSq
-rw-rw-r-- 1 501 501 13545 Oct 23  2019 /var/log/uqyw
-rw-rw-r-- 1 501 502 13545 Oct 23  2019 /home/v2Vb
-rw-rw-r-- 1 502 501 13545 Oct 23  2019 /X1Uy
```

**-rw-rw-r-- 1 502 501 13545 Oct 23  2019 /X1Uy**

---

## Question 6

* Which file is executable by everyone?

    * 8V2l

Looking at the output from the above script we can also see a file executable by everyone.

**-rwxrwxr-x 1 501 501 13545 Oct 23  2019 /etc/8V2L**