# Intermediate NMAP

## Summary

[Intermediate NMAP](https://tryhackme.com/room/intermediatenmap "Intermediate NMAP Room On TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Official Website") and created by [CMNatic](https://github.com/CMNatic "CMNatic GitHub Page").

This CTF requires basic knowledge of:

* Port scanning with tools like ```NMAP```.
* Read data from a network with tools like ```Netcat```.
* Connecting to a remote server via ```SSH```.
* Basic Linux commands such as ```ping```, ```which```, ```ls```, ```cd```, and ```cat```.
* (**OPTIONAL**) Upgrade a dumb shell using ```python```.

---

## Contents

* [Getting Started](#getting-started "Jump To Getting Started")
* [Port Scan](#port-scan "Jump To Port Scan")
* [Finding Credentials](#credentials "Jump To Credentials")
* [Logging Onto Remote Server](#ssh "Jump To SSH")
* [Upgrading Dumb Terminal](#upgrade-terminal "Jump To Upgrade Terminal")
* [Finding The Flag](#flag "Jump To Flag")

---

## Getting Started

As always we start off by pinging the target IP Address to make sure the host is up and running.

```
$ ping <IP_Address>

PING <IP_Address>(<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=160 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=160 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=159 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=160 ms

--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3003ms
rtt min/avg/max/mdev = 159.325/159.711/159.947/0.232 ms
```

[Back To Top](#intermediate-nmap "Jump To Top")

---

## Port Scan

Once we've verified the machine is active we can move on to a port scan using nmap in aggressive mode (-A) on **ALL** ports (-p-). This will return open ports, services, as well as other useful information.

```
$ nmap -p- -A <IP_Address>

Nmap scan report for <IP_Address>
Host is up (0.16s latency).
Not shown: 65532 closed ports
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
2222/tcp  open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
31337/tcp open  Elite?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|     In case I forget - user:pass
|_    ubuntu:Dafdas!!/str0ng

...[REDACTED FOR BREVITY]...
```

After running the port scan we'll see 3 open ports.

* ```Port 22``` - SSH (Secure Shell)
* ```Port 2222``` - SSH (Secure Shell)
* ```Port 31337``` - NetCat Listener

Under the results for ```Port 31337``` we'll also see repeated mentions of the SSH login credentials.

[Back To Top](#intermediate-nmap "Jump To Top")

---

## Credentials

There are three ways we can get the ```SSH``` login credentials for the target machine.

1. Reading the results from the ```NMAP``` scan performed above.
2. Using the browser to visit ```http://<IP_Address>:31337/```.
3. Using ```Netcat``` with the following command, ```nc <IP_Address> 31337```.

```
$ nc <IP_Address> 31337

In case I forget - user:pass
ubuntu:Dafdas!!/str0ng
```

After doing any of the above steps we'll get the credentials ```ubuntu:Dafdas!!/str0ng```.

[Back To Top](#intermediate-nmap "Jump To Top")

---

## SSH

Now that we have the login credentials we can connect to the remote target via ```SSH``` with the username ```ubuntu``` and the password ```Dafdas!!/str0ng```.

```
$ ssh ubuntu@<IP_Address>

ubuntu@<IP_Address>'s password: Dafdas!!/str0ng
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 5.13.0-1014-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

$
```

[Back To Top](#intermediate-nmap "Jump To Top")

---

## Upgrade Terminal

Now that we've logged in we can see that we're working on a dumb terminal. We can make things easier for us by upgrading the terminal with ```Python```. But first we should make sure if ```Python``` is on the target system. We can do this by using the linux ```which``` command followed by the executable file name we're looking for. In this case we're looking for any python version, so the command will look like this...

```
$ which python python2 python3

/usr/bin/python3
```

Now that we've verified what version of Python is on the target system we can use the following command to upgrade the shell...

```python3 -c 'import pty;pty.spawn("/bin/bash")';```

[Back To Top](#intermediate-nmap "Jump To Top")

---

## Flag

Now that the terminal has been upgraded we can start looking for the flag. We'll start by checking where we are with ```pwd``` and listing all the contents in the current directory with ```ls -la```.

```
ubuntu@f518fa10296d:~$ pwd
/home/ubuntu

ubuntu@f518fa10296d:~$ ls -la
total 28
drwxr-xr-x 1 ubuntu ubuntu 4096 Feb 20 23:21 .
drwxr-xr-x 1 root   root   4096 Mar  2  2022 ..
-rw-r--r-- 1 ubuntu ubuntu  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ubuntu ubuntu 3771 Feb 25  2020 .bashrc
drwx------ 2 ubuntu ubuntu 4096 Feb 20 23:21 .cache
-rw-r--r-- 1 ubuntu ubuntu  807 Feb 25  2020 .profile
```

So there's nothing interesting in our current directory. Our next step is to check what other users exist in the home directory.

```
ubuntu@f518fa10296d:~$ ls -la /home
total 20
drwxr-xr-x 1 root   root   4096 Mar  2  2022 .
drwxr-xr-x 1 root   root   4096 Mar  2  2022 ..
drwxr-xr-x 1 ubuntu ubuntu 4096 Feb 20 23:21 ubuntu
drwxr-xr-x 2 root   root   4096 Mar  2  2022 user
```

Next we can list all contents in the other users account, where we'll find a file named ```flag.txt```.

```
ubuntu@f518fa10296d:~$ ls -la /home/user

total 16
drwxr-xr-x 2 root root 4096 Mar  2  2022 .
drwxr-xr-x 1 root root 4096 Mar  2  2022 ..
-rw-rw-r-- 1 root root   38 Mar  2  2022 flag.txt

```

After we ```cat``` the file we'll finally have our flag.

```
ubuntu@f518fa10296d:~$ cat /home/user/flag.txt

flag{251f309497a18888dde5222761ea88e4}
```

[Back To Top](#intermediate-nmap "Jump To Top")
