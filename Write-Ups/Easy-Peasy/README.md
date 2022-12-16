# Easy Peasy

## Summary

[Easy Peasy](https://tryhackme.com/room/easypeasyctf "Easy Peasy CTF on TryHackMe") is a CTF created by TryHackMe user [Kral4](https://tryhackme.com/p/kral4 "Kral4 TryHackMe Profile") and hosted on [TryHackMe](https://tryhackme.com/ "TryHackMe Website"). The room contains the following description.

> Practice using tools such as Nmap and GoBuster to locate a hidden directory to get initial access to a vulnerable machine. Then escalate your privileges through a vulnerable cronjob.

---

## Contents

* [Task 1 - Enumeration through Nmap](#task-1 "Jump To Task 1")
    * [How many ports are open?](#ports "Jump To Question Section")
    * [What is the version of nginx?](#version "Jump To Question Section")
    * [What is running on the highest port?](#highest-port "Jump To Question Section")
* [Task 2 - Compromising the machine](#task-2 "Jump To Task 2")
    * [Using GoBuster, find flag 1.](#gobuster "Jump To Question Section")
    * [Further enumerate the machine, what is flag 2?](#enumerate "Jump To Question Section")
    * [Crack the hash with easypeasy.txt, What is the flag 3?](#crack-the-hash "Jump To Question Section")
    * [What is the hidden directory?](#hidden-directory "Jump To Question Section")
    * [What is the password?](#password "Jump To Question Section")
    * [What is the password to login to the machine via SSH?](#ssh-password "Jump To Question Section")
    * [What is the user flag?](#user-flag "Jump To Question Section")
    * [What is the root flag?](#root-flag "Jump To Question Section")

---

## Task 1

Deploy the machine attached to this task and use nmap to enumerate it.

Before we start we can check to make sure the machine is up by pinging the IP Address.

```
$ ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=239 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=195 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=231 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=172 ms

--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3002ms
rtt min/avg/max/mdev = 172.396/209.308/238.892/26.979 ms

```

### Ports

How many ports are open?

Now that we know the machine is up we can do a port scan with ```nmap``` in aggresive mode (```-A```) and make sure it scans **all** ports with the ```-p-``` flag.

```
$ nmap -A -p- <IP_Address>

Starting Nmap 7.80 ( https://nmap.org )
Nmap scan report for <IP_Address>
Host is up (0.17s latency).
Not shown: 65532 closed ports

PORT      STATE SERVICE VERSION
80/tcp    open  http    nginx 1.16.1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: nginx/1.16.1
|_http-title: Welcome to nginx!
6498/tcp  open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.43 (Ubuntu)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 706.08 seconds
```

The output of scan reveals 3 ports.

* Port 80 - HTTP
* Port 6498 - SSH
* Port 65524 - HTTP

### Version

What is the version of nginx?

The results of the ```nmap``` scan we ran in the previous step showed that the version of nginx was ```1.16.1```.

```
PORT      STATE SERVICE VERSION
80/tcp    open  http    nginx 1.16.1
```

### Highest Port

What is running on the highest port?

```Apache``` was found running on the highest port (65524).

```
PORT      STATE SERVICE VERSION
65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.43 (Ubuntu)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

[Back To Top](#easy-peasy "Jump To Top")

---

## Task 2

Now you've enumerated the machine, answer questions and compromise it!

### GoBuster

Using GoBuster, find flag 1.

### Enumerate

Further enumerate the machine, what is flag 2?

### Crack The Hash

Crack the hash with easypeasy.txt, What is the flag 3?

### Hidden Directory

What is the hidden directory?

### Password

Using the wordlist that provided to you in this task crack the hash
what is the password?

### SSH Password

What is the password to login to the machine via SSH?

### User Flag

What is the user flag?

### Root Flag

What is the root flag?

---

[Back To Top](#easy-peasy "Jump To Top")
