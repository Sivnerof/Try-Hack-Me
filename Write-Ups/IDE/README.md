# IDE

![IDE Room Logo](./Assets/ide.png "IDE Room Logo")

---

## Summary

[IDE](https://tryhackme.com/room/ide "IDE Room On TryHackMe") is a beginner friendly, "easy box to polish your enumeration skills" hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Official Website") and created by [BlueStorm](https://tryhackme.com/p/bluestorm "BlueStorm TryHackMe Profile") and [403 Exploit](https://tryhackme.com/p/403Exploit "403 Exploit TryHackMe Profile").

This CTF requires basic knowledge of:

* Linux commands such as ```ping```, ```which```, ```ls```, ```cd```, ```cat```, ```sudo```, ```find```, ```systemctl``` and ```restart```.

* Port scanning with tools like ```NMAP```.

* Retrieving files from an ```FTP``` server.

* Uploading a reverse shell to a server.

* Using ```Netcat``` to listen for an incoming connection.

* (**OPTIONAL**) Upgrading a dumb terminal using ```Python```.

* Connecting to a remote server via ```SSH```.

* Editing files with tools like ```Nano```.

* Stopping and restarting services in Linux.

---

## Contents

* [Getting Started](#getting-started "Jump To Getting Started")

* [Port Scanning](#port-scanning "Jump To Port Scanning")

* [Getting Username From FTP Server](#ftp-server "Jump To FTP Server")

* [Finding Password For Website](#website-password "Jump To Website Password")

* [Uploading And Calling Reverse Shell](#reverse-shell "Jump To Reverse Shell")

* [Upgrading The Terminal](#terminal-upgrade "Jump To Terminal Upgrade")

* [Horizontal Privilege Escalation - First Flag](#horizontal-escalation "Jump To Horizontal Escalation")

* [Vertical Privilege Escalation - Root Flag](#vertical-escalation "Jump To Vertical Escalation")

---

## Getting Started

As always we start off by checking that the target machine is up and running by pinging the target IP Address.

```
$ ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=224 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=180 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=222 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=183 ms

--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 180.258/202.493/224.379/20.761 ms
```

[Back To Top](#ide "Jump To Top")

---

## Port Scanning

Once we've verified the machine is active we can move on to a port scan using ```nmap``` with the ```-p-``` flag to make sure we scan **ALL** ports.

```
$ nmap -p- <IP_Address>

Nmap scan report for <IP_Address>
Host is up (0.16s latency).
Not shown: 65531 closed ports
PORT      STATE SERVICE
21/tcp    open  ftp
22/tcp    open  ssh
80/tcp    open  http
62337/tcp open  unknown
```

After our initial port scan we can see that there are 4 open ports.

* ```PORT 21``` - FTP (File Transfer Protocol)
* ```PORT 22``` - SSH (Secure Shell)
* ```PORT 80``` - HTTP (HyperText Transfer Protocol)
* ```PORT 62337``` - UNKNOWN

To get more information on these services we can run another port scan but this time we'll use the ```-A``` and ```-p``` flag in order to aggressively scan only these specific ports.

```
$ nmap -A -p 21,22,80,62337 <IP_Address>

Nmap scan report for <IP_Address>
Host is up (0.16s latency).

PORT      STATE SERVICE VERSION
21/tcp    open  ftp     vsftpd 3.0.3
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
62337/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Codiad 2.8.4
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

We can see from the above port scan that the unknown service on ```PORT 62337``` that we found earlier is another website and the ```FTP``` service allows anonymous login. So our next logical step is to check the ```FTP``` server.

[Back To Top](#ide "Jump To Top")

---

## FTP Server



[Back To Top](#ide "Jump To Top")

---

## Website Password



[Back To Top](#ide "Jump To Top")

---

## Reverse Shell



[Back To Top](#ide "Jump To Top")

---

## Terminal Upgrade



[Back To Top](#ide "Jump To Top")

---

## Horizontal Escalation



[Back To Top](#ide "Jump To Top")

---

## Vertical Escalation



[Back To Top](#ide "Jump To Top")
