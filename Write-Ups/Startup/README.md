# Startup

![Startup Logo](./Assets/startup.png "A Flaming Chilli Pepper")

## Summary

[Startup](https://tryhackme.com/room/startup "Startup CTF on TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Official Website") and created by [Elbee](https://tryhackme.com/p/elbee). The room consists of 1 task and 3 flags, and the only description the room gives is the following.

> We are Spice Hut, a new startup company that just made it big! We offer a variety of spices and club sandwiches (in case you get hungry), but that is not why you are here. To be truthful, we aren't sure if our developers know what they are doing and our security concerns are rising. We ask that you perform a thorough penetration test and try to own root. Good luck!

The room creator (Elbee) can also be found at:
* [TryHackMe](https://tryhackme.com/p/elbee "Elbee's TryHackMe")
* [Twitter](https://twitter.com/elbee_ez "Elbee's Twitter")
* [GitHub](https://github.com/elbee-cyber "Elbee's GitHub")
* [YouTube](https://www.youtube.com/@elbee1473 "Elbee's YouTube")

---

## Contents

* [Flag 1 - What is the secret spicy soup recipe?](#flag-1 "Jump To Flag 1")
* [Flag 2 - What are the contents of user.txt?](#flag-2 "Jump To Flag 2")
* [Flag 3 - What are the contents of root.txt?](#flag-3 "Jump To Flag 3")

---

## Flag 1

As always we start by pinging the target machine to make sure it's up.

```
ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=169 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=167 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=168 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=168 ms
^C
--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 167.185/167.915/168.506/0.563 ms
```

Once we've verified the machine is up and running we can start a port scan on the IP address using ```nmap``` in aggresive mode by using the ```-A``` flag.

```
$ nmap -A <IP_Address>

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp [NSE: writeable]
| -rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
|_-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to <IP_Address>
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Maintenance
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

The result of the nmap scan shows 3 open ports.

* 21 - FTP (File Transfer Protocol)
* 22 - SSH (Secure Shell)
* 80 - HTTP (HyperText Transfer Protocol)

It also shows that FTP allows anonymous login and there are files currently stored there, as well as a writable directory. Meaning we also have permissions to upload files.

Before we visit the website we should make sure to download and check all the files on the FTP server.

We can connect to FTP with the following command.

```ftp <IP_Address>```

Once we connect, it should ask us for our credentials. For username we specify ```anonymous``` and for password we can type anything or just press enter.

We should see output similar to the following.

```
$ ftp <IP_Address>
Connected to <IP_Address>.
220 (vsFTPd 3.0.3)
Name: Anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```

To list all files in the current directory we can use the ```ls -la``` command which shows us the following.

```
ftp> ls -la
229 Entering Extended Passive Mode (|||15969|)
150 Here comes the directory listing.
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 .
drwxr-xr-x    3 65534    65534        4096 Nov 12  2020 ..
-rw-r--r--    1 0        0               5 Nov 12  2020 .test.log
drwxrwxrwx    2 65534    65534        4096 Nov 12  2020 ftp
-rw-r--r--    1 0        0          251631 Nov 12  2020 important.jpg
-rw-r--r--    1 0        0             208 Nov 12  2020 notice.txt
226 Directory send OK.
ftp>
```

We have 3 files, ```.test.log```, ```important.jpg```, and ```notice.txt```, as well as a writable directory named ```ftp``` which is currently empty.

To download these files we'll have to use the ```get``` command followed by the file name like so...

```
ftp> get .test.log
local: .test.log remote: .test.log
229 Entering Extended Passive Mode (|||32609|)
150 Opening BINARY mode data connection for .test.log (5 bytes).
100% |***********************************|     5        6.59 KiB/s    00:00 ETA
226 Transfer complete.
5 bytes received in 00:00 (0.02 KiB/s)

ftp> get important.jpg
local: important.jpg remote: important.jpg
229 Entering Extended Passive Mode (|||50936|)
150 Opening BINARY mode data connection for important.jpg (251631 bytes).
100% |***********************************|   245 KiB   79.75 KiB/s    00:00 ETA
226 Transfer complete.
251631 bytes received in 00:03 (75.63 KiB/s)

ftp> get notice.txt
local: notice.txt remote: notice.txt
229 Entering Extended Passive Mode (|||32740|)
150 Opening BINARY mode data connection for notice.txt (208 bytes).
100% |***********************************|   208        1.69 MiB/s    00:00 ETA
226 Transfer complete.
208 bytes received in 00:00 (1.19 KiB/s)
ftp> 
```

After we've downloaded the files we can go through them and see if we can find anything of use.

The ```.test.log``` file is empty, so obviously nothing important there.

The ```important.jpg``` file is just an "Among Us" meme.

![amongus](./Assets/important.jpg "Character from Among Us with crying doggo superimposed on face")

Lastly the ```notice.txt``` file reads...

> Whoever is leaving these damn Among Us memes in this share, it IS NOT FUNNY. People downloading documents from our website will think we are a joke! Now I dont know who it is, but Maya is looking pretty sus.

This message implies that users are downloading files on the website that are being uploaded by the developers through FTP.

That being said, we should check the website now.

Once we visit the website we'll be greeted with placeholder text for a website currently under construction and viewing the source code reveals the following HTML comment. 

```html
<article>
    <h1>No spice here!</h1>
    <div>
	<!--when are we gonna update this??-->
        <p>Please excuse us as we develop our site. We want to make it the most stylish and convienient way to buy peppers. Plus, we need a web developer. BTW if you're a web developer, <a href="mailto:#">contact us.</a> Otherwise, don't you worry. We'll be online shortly!</p>
        <p>&mdash; Dev Team</p>
    </div>
</article>
```

But none of these things lead us anywhere, so we should further enumerate the site with a tool like [GoBuster](https://www.kali.org/tools/gobuster/ "Kali Documentation for GoBuster") and see what we can find.

The wordlist I used for the directory scan was [directory-list-2.3-small.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-2.3-small.txt "Small Directory Word List")

```
$ gobuster -u <IP_Address> -w /path/to/word/list

=====================================================
Gobuster v2.0.1              OJ Reeves (@TheColonial)
=====================================================
[+] Mode         : dir
[+] Url/Domain   : http://<IP_Address>/
[+] Threads      : 10
[+] Wordlist     : /path/to/word/list
[+] Status codes : 200,204,301,302,307,403
[+] Timeout      : 10s
=====================================================
2023/01/08 11:59:46 Starting gobuster
=====================================================
/files (Status: 301)

```

Almost immediately the ```gobuster``` scan finds a directory named ```files```.

If we visit ```http://<IP_Address>/files/``` we'll see an unprotected directory with **exactly** the same files we discovered on the FTP server.

![Unprotected Directory](./Assets/unprotected-directory.png "Unprotected Directory")

As well as the empty directory named ```ftp``` which we had write access to.

![Empty FTP Directory](./Assets/empty-ftp-directory.png "Empty FTP Directory")

This vulnerability gives us the ability to upload a reverse shell on the FTP server into this directory and come back to this site to access it.

Let's try it out.




### [Back To Top](#startup "Jump To Top")

---

## Flag 2



### [Back To Top](#startup "Jump To Top")

---

## Flag 3



---

### [Back To Top](#startup "Jump To Top")
