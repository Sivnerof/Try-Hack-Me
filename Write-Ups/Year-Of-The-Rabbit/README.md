# Year Of The Rabbit

![Rabbit](./Assets/rabbit.jpg "Sketch Drawing Of A Rabbit")

## Summary

[Year Of The Rabbit](https://tryhackme.com/room/yearoftherabbit "Year Of The Rabbit Room On  TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Official Website") and created by [Muirlandoracle](https://tryhackme.com/p/MuirlandOracle "Muirlandoracle TryHackMe Profile").

This CTF requires basic knowledge of:

* Port scanning with tools like ```nmap```.

* Directory/file scanning with tools like ```gobuster```.

* Viewing ```HTML``` source code.

* Viewing ```CSS``` source code.

* Intercepting HTTP requests with tools like ```BurpSuite```.

* Extracting image metadata with tools like ```ExifTool```.

* Using the Linux ```strings``` command to find suspicious text in images.

* Brute forcing an FTP server with tools like ```Hydra```.

* Getting files from an ```FTP``` server.

* Connecting to remote server with ```SSH```.

* Linux privilege escalation with tools like ```GTFOBins```.

---

## Contents

* [Getting Started](#getting-started "Jump To Getting Started")

* [Port Enumeration](#port-enumeration "Jump To Port Enumeration")

* [Directory Scanning](#directory-scanning "Jump To Directory Scanning")

* [Examining Files](#examining-files "Jump To Examining Files")

* [The Rabbit Hole](#the-rabbit-hole "Jump To The Rabbit Hole")

* [Finding The Hidden Directory](#the-hidden-directory "Jump To The Hidden Directory")

* [Metadata and Steganography](#metadata-and-steganography "Jump To Metadata and Steganography")

* [FTP Bruteforce](#ftp-bruteforce "Jump To FTP Bruteforce")

* [Esoteric Language](#esoteric-language "Jump To Esoteric Language")

* [Initial Foothold](#initial-foothold "Jump To Initial Foothold")

* [What is the user flag?](#flag-1 "Jump To Flag 1")

* [What is the root flag?](#flag-2 "Jump To Flag 2")

---

## Getting Started

Before we've started the machine we're given the following introductory text...

> Let's have a nice gentle start to the New Year!
Can you hack into the Year of the Rabbit box without falling down a hole?
(Please ensure your volume is turned up!)

So we know at some point we'll have to listen closely to something in order to advance to the next step.

But for now our first step is to start the machine and use the ```ping``` command to ensure the target machine is up and running.

```
$ ping <IP_Address>

PING <IP_Address> (<IP_Address>) 56(84) bytes of data.
64 bytes from <IP_Address>: icmp_seq=1 ttl=61 time=171 ms
64 bytes from <IP_Address>: icmp_seq=2 ttl=61 time=169 ms
64 bytes from <IP_Address>: icmp_seq=3 ttl=61 time=170 ms
64 bytes from <IP_Address>: icmp_seq=4 ttl=61 time=168 ms
^C
--- <IP_Address> ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 168.085/169.433/170.750/0.963 ms
```

Now that we've ensured connectivity we can move on to port enumeration so that we can see what kind of services are running on the target machine.

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Port Enumeration

In order to discover what kind of services are running on the target machine we can use ```nmap``` in aggressive mode by using the ```-A``` flag. This will return open ports, services, as well as other useful information.

```
$ nmap -A <IP_Address>

Host is up (0.17s latency).
Not shown: 997 closed ports
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

After running the scan we can see we have 3 open ports.

* Port 21 - ```FTP``` (File Transfer Protocol)

* Port 22 - ```SSH``` (Secure Shell)

* Port 80 - ```HTTP``` (HyperText Transfer Protocol)

And we can also see the website at port 80 has the default ```Apache2``` landing page.

Our next step should be to check the page for any additional information as well as use ```GoBuster``` to find any hidden directories.

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Directory Scanning

Once we navigate to the website we'll see the ```Apache2 Debian Default Page```. We won't find anything useful on this page or in the HTML source code. So our next step is a directory scan using ```GoBuster``` and a wordlist like [directory-list-2.3-small.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/directory-list-2.3-small.txt "Small Directory Word List").

```
$ gobuster -u <IP_Address> -w /path/to/wordlist

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
2023/01/15 10:52:56 Starting gobuster
=====================================================
/assets (Status: 301)
```

After running the scan we should see a directory named ```/assets``` has been found.

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Examining Files

Once we have navigated to the newly discovered directory at ```http://<IP_Address>/assets``` we should see two files, ```RickRolled.mp4``` and ```style.css```.

![Assets Directory](./Assets/assets-directory.png "Assets Directory")

The RickRolled video is obviously Rick Astley singing "Never Gonna Give You Up", but if you listen closely you'll hear hidden information within the song. More on that later, for now all we need to do is to examine the ```style.css``` file.

Viewing the CSS source code we can find the following comment right after the ```body, html``` selector...

```css
/* Nice to see someone checking the stylesheets.
    Take a look at the page: /sup3r_s3cr3t_fl4g.php
*/
```

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## The Rabbit Hole

Visiting the file referenced in the CSS source code (```http://<IP_Address>/sup3r_s3cr3t_fl4g.php```) we'll be greeted by a JavaScript Alert that tells us to turn off JavaScript.

![JavaScript Alert](./Assets/javascript-alert.png "JavaScript Alert Telling Us To Turn Off JavaScript")

Once we press ```OK``` we'll be RickRolled again. The site will redirect us to Rick Astley's "[Never Gonna Give You Up](https://www.youtube.com/watch?v=dQw4w9WgXcQ "Never Gonna Give You Up Song On YouTube")" song on YouTube.

If we turn off JavaScript as suggested by the alert, we'll be greeted with text that reads...

```
Love it when people block Javascript...
This is happening whether you like it or not... The hint is in the video. If you're stuck here then you're just going to have to bite the bullet!
Make sure your audio is turned up!
```

And the Rick Astley Rick Roll video is back again, this time it's the one we found earlier in the ```/assets``` folder. So wether or not we have JavaScript enabled we're stuck in a rabbit hole of Rick Rolls.

If we listen to the song, around the ```56 second mark```, we can hear the following...

```I'll put you out of your misery, you're looking in the wrong place *burp*.```

The burp at the end is a somewhat subtle reference to the ```BurpSuite``` tool used for intercepting HTTP requests.

Logically our next step should be intercepting the request to ```http://<IP_Address>/sup3r_s3cr3t_fl4g.php``` with ```BurpSuite``` but there's actually an easier way to move on from this step and that's to use the ```Network``` tab in our ```Dev Console```.

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## The Hidden Directory

If we open our ```Developer Console``` in the browser, switch over to the ```Network``` tab, and visit ```http://<IP_Address>/sup3r_s3cr3t_fl4g.php``` we'll see that this request redirects us to ```intermediary.php?hidden_directory=/WExYY2Cv-qU``` which then redirects us to the ```/sup3r_s3cret_fl4g/``` directory.

![Network Tab Results](./Assets/network-tab-results.png "Network Tab Results")

It all happens so fast, but for a brief moment we request a file named ```intermediary.php``` and pass it the parameter ```hidden_directory``` and value ```/WExYY2Cv-qU```.

The intended way to have discovered this hidden directory was to use ```BurpSuite``` to intercept the initial request and forward it until we saw the following request being made...

```http
GET /intermediary.php?hidden_directory=/WExYY2Cv-qU HTTP/1.1
Host: <IP_Address>
User-Agent: <Your_Browser>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
DNT: 1
```

If we visit newly found directory at ```http://<IP_Address>/WExYY2Cv-qU/``` we'll find an image called ```Hot_Babe.png```.

![Hidden Directory](./Assets/intercepted-directory.png "Hidden Directory Contents")

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Metadata and Steganography

Once we have discovered the image at ```http://<IP_Address>/WExYY2Cv-qU/Hot_Babe.png``` we can download it for further analysis.

![Lena Soderberg](./Assets/Hot_Babe.png "Image of Lena Soderberg")

A quick side note about this image before we start extracting the metadata...

The woman in the photo is Lena Söderberg, and this image is a cropped version of the original which appeared in the November 1972 issue of Playboy magazine, where Lena was the centrefold model.

It is one of the most popular images on the internet due to it's use by scientific researchers working on image processing and the creation of the JPEG. It was also one of the first images uploaded to [ARPANET](https://en.wikipedia.org/wiki/ARPANET "ARPANet WikiPedia") and has a very long history in Computer Science and Image Processing.

There are many YouTube videos that explain the history of this image, as well as a [WikiPedia page](https://en.wikipedia.org/wiki/Lenna "WikiPedia page about Lena") and a [great article by The Atlantic](https://www.theatlantic.com/technology/archive/2016/02/lena-image-processing-playboy/461970/ "Atlantic article about Lena").

Anyways back to analyzing the image.

If we use the ```exiftool``` command on the image we'll notice a row named ```warning``` that reads "```[minor] Trailer data after PNG IEND chunk```".

```
$ exiftool Hot_Babe.png
ExifTool Version Number         : 12.40
File Name                       : Hot_Babe.png
Directory                       : .
File Size                       : 464 KiB
File Permissions                : -rw-rw-r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 512
Image Height                    : 512
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 512x512
Megapixels                      : 0.262
```

If we search the web for what this means we can find a [W3 page about PNG Chunks](https://www.w3.org/TR/PNG-Chunks.html "W3 page on PNG data chunks") which states...

> The IEND chunk must appear LAST. It marks the end of the PNG datastream. The chunk's data field is empty.

This warning in the metadata seems to tell us there's data in the file after the PNG ends.

And if we use the Linux ```strings``` command on the image and scroll up a bit we can find the string ```IEND```. This is where the PNG should end but instead there's a bunch of strings underneath. Appended to the PNG are an FTP username and a [list of possible passwords for the user](./Assets/ftp-password-list.txt "Password List").

```
IEND
Ot9RrG7h2~24?
Eh, you've earned this. Username for FTP is ftpuser
One of these is the password:
Mou+56n%QK8sr
1618B0AUshw1M
A56IpIl%1s02u
vTFbDzX9&Nmu?
FfF~sfu^UQZmT
8FF?iKO27b~V0
ua4W~2-@y7dE$
3j39aMQQ7xFXT
Wb4--CTc4ww*-
u6oY9?nHv84D&
0iBp4W69Gr_Yf
TS*%miyPsGV54
C77O3FIy0c0sd
O14xEhgg0Hxz1
5dpv#Pr$wqH7F
1G8Ucoce1+gS5
0plnI%f0~Jw71
0kLoLzfhqq8u&
kS9pn5yiFGj6d
zeff4#!b5Ib_n
rNT4E4SHDGBkl
KKH5zy23+S0@B
3r6PHtM4NzJjE
gm0!!EC1A0I2?
HPHr!j00RaDEi
7N+J9BYSp4uaY
PYKt-ebvtmWoC
3TN%cD_E6zm*s
eo?@c!ly3&=0Z
nR8&FXz$ZPelN
eE4Mu53UkKHx#
86?004F9!o49d
SNGY0JjA5@0EE
trm64++JZ7R6E
3zJuGL~8KmiK^
CR-ItthsH%9du
yP9kft386bB8G
A-*eE3L@!4W5o
GoM^$82l&GA5D
1t$4$g$I+V_BH
0XxpTd90Vt8OL
j0CN?Z#8Bp69_
G#h~9@5E5QA5l
DRWNM7auXF7@j
Fw!if_=kk7Oqz
92d5r$uyw!vaE
c-AA7a2u!W2*?
zy8z3kBi#2e36
J5%2Hn+7I6QLt
gL$2fmgnq8vI*
Etb?i?Kj4R=QM
7CabD7kwY7=ri
4uaIRX~-cY6K4
kY1oxscv4EB2d
k32?3^x1ex7#o
ep4IPQ_=ku@V8
tQxFJ909rd1y2
5L6kpPR5E2Msn
65NX66Wv~oFP2
LRAQ@zcBphn!1
V4bt3*58Z32Xe
ki^t!+uqB?DyI
5iez1wGXKfPKQ
nJ90XzX&AnF5v
7EiMd5!r%=18c
wYyx6Eq-T^9#@
yT2o$2exo~UdW
ZuI-8!JyI6iRS
PTKM6RsLWZ1&^
3O$oC~%XUlRO@
KW3fjzWpUGHSW
nTzl5f=9eS&*W
WS9x0ZF=x1%8z
Sr4*E4NT5fOhS
hLR3xQV*gHYuC
4P3QgF5kflszS
NIZ2D%d58*v@R
0rJ7p%6Axm05K
94rU30Zx45z5c
Vi^Qf+u%0*q_S
1Fvdp&bNl3#&l
zLH%Ot0Bw&c%9
```

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## FTP Bruteforce

Now that we have extracted the strings from the PNG we can copy [all of the possible passwords](./Assets/ftp-password-list.txt "FTP Password TXT File") and store them in a text file.

We also know the username for the FTP server is ```ftpuser```.

So we're going to have to bruteforce the FTP server using ```Hydra``` with the ```-l``` flag followed by the username ```ftpuser```, ```-P``` followed by our password file, ```-V``` for verbose mode, and we're going to prepend the target IP address with ```ftp:```.

The command should look something like this...

```hydra -l ftpuser -P /path/to/wordlist -V ftp://<IP_Address>```

After Hydra has finished running we should see the following output...

```
[21][ftp] host: 10.10.248.204   login: ftpuser   password: 5iez1wGXKfPKQ
1 of 1 target successfully completed, 1 valid password found
```

Now we have our full credentials.

```ftpuser:5iez1wGXKfPKQ```

To connect to the FTP server we just need to run the command ```ftp <IP_Address>``` and when prompted for the username, input ```ftpuser```. For the password we'll use ```5iez1wGXKfPKQ```.

```
$ ftp <IP_Address>

220 (vsFTPd 3.0.2)
Name: ftpuser
331 Please specify the password.
Password: 5iez1wGXKfPKQ
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```

Now that we're logged in to the FTP server we can list all files in the current directory with the ```ls -la``` command, which will show us only one file named ```Eli's_Creds.txt```.

```
ftp> ls -la
229 Entering Extended Passive Mode (|||22547|).
150 Here comes the directory listing.
drwxr-xr-x    2 0        0            4096 Jan 23  2020 .
drwxr-xr-x    2 0        0            4096 Jan 23  2020 ..
-rw-r--r--    1 0        0             758 Jan 23  2020 Eli's_Creds.txt
226 Directory send OK.
```

To download this file to our own machine we use the ```get``` command followed by the file name.

```
ftp> get Eli's_Creds.txt
local: Eli's_Creds.txt remote: Eli's_Creds.txt
229 Entering Extended Passive Mode (|||22266|).
150 Opening BINARY mode data connection for Eli's_Creds.txt (758 bytes).
100% |***********************************|   758      580.57 KiB/s    00:00 ETA
226 Transfer complete.
758 bytes received in 00:00 (4.24 KiB/s)
```

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Esoteric Language

Once we've downloaded [Eli's_Creds.txt](./Assets/Eli's_Creds.txt "Eli's Creds Text File") on to our local machine we'll see that the file reads...

```brainfuck
+++++ ++++[ ->+++ +++++ +<]>+ +++.< +++++ [->++ +++<] >++++ +.<++ +[->-
--<]> ----- .<+++ [->++ +<]>+ +++.< +++++ ++[-> ----- --<]> ----- --.<+
++++[ ->--- --<]> -.<++ +++++ +[->+ +++++ ++<]> +++++ .++++ +++.- --.<+
+++++ +++[- >---- ----- <]>-- ----- ----. ---.< +++++ +++[- >++++ ++++<
]>+++ +++.< ++++[ ->+++ +<]>+ .<+++ +[->+ +++<] >++.. ++++. ----- ---.+
++.<+ ++[-> ---<] >---- -.<++ ++++[ ->--- ---<] >---- --.<+ ++++[ ->---
--<]> -.<++ ++++[ ->+++ +++<] >.<++ +[->+ ++<]> +++++ +.<++ +++[- >++++
+<]>+ +++.< +++++ +[->- ----- <]>-- ----- -.<++ ++++[ ->+++ +++<] >+.<+
++++[ ->--- --<]> ---.< +++++ [->-- ---<] >---. <++++ ++++[ ->+++ +++++
<]>++ ++++. <++++ +++[- >---- ---<] >---- -.+++ +.<++ +++++ [->++ +++++
<]>+. <+++[ ->--- <]>-- ---.- ----. <
```

At first this might just look like gibberish but if you spend enough time programming, eventually you'll run into [esoteric programming languages](https://en.wikipedia.org/wiki/Esoteric_programming_language "WikiPedia For Esoteric Programming Languages"). One of the most popular is called [BrainFuck](https://en.wikipedia.org/wiki/Brainfuck "Wikipedia Page For BrainFuck Programming Language"), and this is what it looks like.

In order to find out what this program outputs we can use the [brainfuck interpreter from dcode](https://www.dcode.fr/brainfuck-language "Brainfuck Interpreter"), which shows us that the program outputs the following SSH credentials...

```
User: eli
Password: DSpDiM1wAEwid
```

### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Initial Foothold



### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Flag 1



### [Back To Top](#year-of-the-rabbit "Jump To Top")

---

## Flag 2

---

### [Back To Top](#year-of-the-rabbit "Jump To Top")
