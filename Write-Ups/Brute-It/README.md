# Brute It

## Summary

[Brute It](https://tryhackme.com/room/bruteit "Brute It CTF on TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Official Website") and created by [ReddyyZ](https://tryhackme.com/p/ReddyyZ "ReddyyZ Profile On TryHackMe").

This CTF requires basic knowledge of:

* Port scanning with tools like ```nmap```.

* Directory/file scanning with tools like ```gobuster```.

* Examining ```HTML``` source code.

* Examining HTTP requests with tools like ```BurpSuite```.

* Bruteforcing login pages with tools like ```Hydra```.

* Getting the hash value of a private RSA key with tools like ```ssh2john```.

* Hash cracking with tools like ```JohnTheRipper```.

* Connecting to a remote server with ```SSH``` using a private key.

* Combining passwd and shadow files with tools like ```unshadow```.

---

## Contents

* [Reconnaissance](#recoinnaissance "Jump To Recoinnassance")

    * [How Many Ports Are Open?](#ports "Jump To Ports")

    * [What Version Of SSH Is Running?](#ssh-version "Jump To SSH Version")

    * [What Version Of Apache Is Running?](#apache-version "Jump To Apache Version")

    * [Which Linux Distribution Is Running?](#linux-distribution "Jump To Linnux Distribution")

    * [What Is The Hidden Directory?](#hidden-directory "Jump To Hidden Directory")

* [Getting A Shell](#getting-a-shell "Jump To Getting A Shell")

    * [What Is The User:Password Of The Admin Panel?](#credentials "Jump To Credentials")

    * [What Is John's RSA Private Key Passphrase?](#rsa-private-key "Jump To RSA Private Key")

    * [User.txt Flag](#usertxt "Jump To User.txt")

    * [Web Flag](#web-flag "Jump To Web Flag")

* [Privilege Escalation](#privilege-escalation "Jump To Privilege Escalation")

    * [What Is The Root's Password?](#roots-password "Jump To Root's Password")

    * [Root.txt Flag](#root-flag "Jump To Root Flag")

---

## Recoinnaissance

### Ports

As always, we start by turning on the target machine and using the ```ping``` command to make sure the machine is up and running.

```
$ ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=213 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=175 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=218 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=179 ms
^C
--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 175.097/195.956/217.527/19.226 ms
```

Once we've verified the machine is active we can move on to a port scan using ```nmap``` in aggressive mode (```-A```). This will return open ports, services, as well as other useful information.

```
$ nmap -A <IP_Address>

Nmap scan report for <IP_Address>
Host is up (0.24s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

After we run a port scan we'll see that we have 2 ports open.

* ```Port 22``` - SSH (Secure Shell)

* ```Port 80``` - HTTP (HyperText Transfer Protocol)

### SSH Version

We can also see, from the results of our port scan above, that the SSH version of the target IP is ```OpenSSH 7.6p1```.

```22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)```

### Apache Version

The port scan also showed us that the version of Apache that is running on the target IP is ```2.4.29```.

```80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))```

### Linux Distribution

We also saw the Linux Distribution on the target IP was ```Ubuntu```.

```|_http-title: Apache2 Ubuntu Default Page: It works```

### Hidden Directory

If we visit the website we found in the port scan we'll be greeted with the "Apache2 Ubuntu Default Page", and viewing the HTML source code reveals nothing of use. So our next step is to use ```GoBuster``` to find hidden directories.

```
$ gobuster -w /path/to/wordlist -u <IP_Address>

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://<IP_Address>/
[+] Threads      : 10
[+] Wordlist     : /path/to/wordlist
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2023/01/18 10:29:23 Starting gobuster
=====================================================
/admin (Status: 301)
```

Almost immediately the scan returns a directory named ```/admin```.

[BACK TO TOP](#brute-it "Jump To Top")

---

## Getting A Shell

### Credentials

Now that we've found the admin login at ```http://<IP_Address>/admin``` we need a way to login.

### RSA Private Key

### user.txt

### Web Flag

[BACK TO TOP](#brute-it "Jump To Top")

---

## Privilege Escalation

### Root's Password

### Root Flag

---

[BACK TO TOP](#brute-it "Jump To Top")
