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

* [Getting Started]("Jump To ")
* [Port Scan]("Jump To ")
* [Finding Credentials]("Jump To ")
* [Logging Onto Remote Server]("Jump To ")
* [Finding The Flag]("Jump To ")

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



[Back To Top](#intermediate-nmap "Jump To Top")

---

## Flag



[Back To Top](#intermediate-nmap "Jump To Top")
