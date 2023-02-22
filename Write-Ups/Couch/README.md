# Couch

## Summary

[Couch](https://tryhackme.com/room/couch "Couch Room On TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/room/couch "TryHackMe Official Website") and created by [Cesar Calderon A.K.A Stuxnet](https://twitter.com/__stux "Stuxnet Twitter Profile").

Room Description:

> Hack into a vulnerable database server that collects and stores data in JSON-based document formats, in this semi-guided challenge.

This CTF requires basic knowledge of:

* Basic Linux commands such as ```ping```, .

* Port scanning with tools like ```NMAP```.

* Reading application documentation.

* Connecting to a remote server via ```SSH```.

* Starting a ```Docker``` container.

---

## Contents

* [Getting Started](#getting-started "Jump To Getting Started")

* [Port Scan](#port-scan "Jump To Port Scan")

    * [Scan the machine. How many ports are open?](#open-ports "Jump To Open Ports")

    * [What is the database management system installed on the server?](#database-discovery "Jump To Database Discovery")

    * [What port is the database management system running on?](#database-port "Jump To Database Port")

    * [What is the version of the management system installed on the server?](#database-version "Jump To Database Version")

* [Reading DataBase Documentation](#database-documentation "Jump To Database Documentation")

    * [What is the path for the web administration tool for this database management system?](#administrator-path "Jump To Administrator Path")

    * [What is the path to list all databases in the web browser of the database management system?](#all-databases "Jump To All Databases")

* [Finding SSH Credentials](#ssh-credentials "Jump To SSH Credentials")

    * [What are the credentials found in the web administration tool?](#credentials "Jump To Credentials")

* [First Flag](#first-flag "Jump To First Flag")

    * [Compromise the machine and locate user.txt](#usertxt "Jump To user.txt")

* [Root Flag](#root-flag "Jump To Root Flag")

    * [Escalate privileges and obtain root.txt](#roottxt "Jump To root.txt")

---

## Getting Started

As always we start by checking that the target machine is up and running by pinging the target IP Address.

```
$ ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=160 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=159 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=160 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=160 ms

--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3002ms
rtt min/avg/max/mdev = 159.318/159.807/160.327/0.362 ms
```

[Back To Top](#couch "Jump To Top")

---

## Port Scan



### Open Ports



### Database Discovery



### Database Port



### Database Version



[Back To Top](#couch "Jump To Top")

---

## Database Documentation

### Administrator Path

### All Databases


[Back To Top](#couch "Jump To Top")

---

## SSH Credentials

### Credentials

[Back To Top](#couch "Jump To Top")

---

## First Flag

### user.txt

[Back To Top](#couch "Jump To Top")

---

## Root Flag

### root.txt

[Back To Top](#couch "Jump To Top")
