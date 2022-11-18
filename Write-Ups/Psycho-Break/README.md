# The Evil Within

![Psycho Break](./Assets/the-evil-within.jpg "Image of The Evil Within character looking at a city in decay")

## Summary

[Psycho Break](https://tryhackme.com/room/psychobreak "Psycho Break room on TryHackMe") is a <abbr title="Capture The Flag">CTF</abbr> created by [Shafdo](https://github.com/shafdo "Shafdos GitHub") and inspired by the survival horror video game ["The Evil Within"](https://en.wikipedia.org/wiki/The_Evil_Within "The Evil Within Wikipedia"). This room can be found on [TryHackMe](https://tryhackme.com/ "TryHackMe Website") along with other CTF's.

---

## Sections

* [Task 1 - Recon](#task-1---recon "Jump To Task 1")
* [Task 2 - Web](#task-2---web "Jump To Task 2")
* [Task 3 - Help Mee](#task-3---help-mee "Jump To Task 3")
* [Task 4 - Crack It Open](#task-4---crack-it-open "Jump To Task 4")
* [Task 5 - Go Capture The Flag](#task-5---go-capture-the-flag "Jump To Task 5")
* [Task 6 - Copyright Material](#task-6---copyright-material "Jump To Task 6")

---

## Task 1 - Recon

### How many ports are open?

Starting a port scan with ```nmap``` in aggressive mode (```-A```) to see what services are up and running on IP. We can see that 3 ports are open and the target machine OS is Ubuntu.

1. Port 21 - ftp
2. Port 22 - ssh
3. Port 80 - http

```
$ nmap -A <IP Address>

PORT   STATE SERVICE VERSION
21/tcp open  ftp     ProFTPD 1.3.5a
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))

Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

### What is the operating system that runs on the target machine?

Running the above command (```nmap -A <IP Address>```) shows the operating system is **Ubuntu**.


#### [BACK TO TOP](#the-evil-within "Jump To Top")

---

## Task 2 - Web

Visiting port 80 (```<IP Address>:80```) takes us to the website. Nothing looks out of the ordinary until you view the <abbr title="Hyper Text MarkUp Language">HTML</abbr> source code where you can find the following three interesting lines.

**Unprotected Directory (```<IP Address>/css/```)** -
```html
<link rel="stylesheet" type="text/css" href="../css/mainstylesheet.css">
```

**<abbr title="Hyper Text MarkUp Language">HTML</abbr> Comment** -

```html
<!-- Sebastian sees a path through the darkness which leads to a room => /sadistRoom -->
```

**Obscured <abbr title="Hyper Text MarkUp Language">HTML</abbr> Element (White Text On A White Background)** -

```html
<a href="map.html" style="color: #fff;">Here is the map</a>
```

The unprotected directory (```<IP Address>/css```) has two css files.

1. ```/css/mainstylesheet.css```
2. ```/css/lightbox.css``` (this file references an ```/images``` directory I couldn't find).

![Unprotected Directory](./Assets/unprotected-css-directory.png "Unprotected CSS Directory")

The link to ```map.html``` goes nowhere.

So the only way forward for now is to visit the directory referenced in the <abbr title="Hyper Text MarkUp Language">HTML</abbr> comment.

Navigating to ```<IP Address>/sadistRoom``` and clicking the link at the bottom of the screen triggers the following JavaScript alert:

> Key to locker Room => 532219a04ab7a02b56faafbec1a4c1ea

Copy the key, click the button that says "**Enter Key To The Locker Room**" and paste it into the prompt to be taken to ```<IP Address>/lockerRoom/```

### Key to the looker room

You can find the key by clicking the link at the bottom of ```<IP Address>/sadistRoom```.

> Key to locker Room => 532219a04ab7a02b56faafbec1a4c1ea

Additional Notes -

The key to the locker room is an MD5 hash of "**enterlockerroom**".

### Key to access the map

At the bottom of ```<IP Address>/lockerRoom``` we see the following text:

> Decode this piece of text "Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv" and get the key to access the map.

And a link that leads to ```<IP Address>/map.php``` where we can paste our decrypted text.

At first the cipher text looks like a Caesar Cipher but using CyberChef to brute force the 26 keys. None of the outputs seem valid.

And it's not a Vigenere Cipher.

So the next option is to put the cipher text into a [cipher identifier/analyzer](https://www.boxentriq.com/code-breaking/cipher-identifier "Boxentriq Cipher Analyzer").

The tool informs us that this is most likely an [Atbash Cipher](https://en.wikipedia.org/wiki/Atbash "Atbash Cipher Wikipedia").

Atbash is a simple cipher often referred to as "mirror code" where a letter is mapped to its reverse (A=Z, B=Y, C=X, Z=A, Y=B, C=X, etc).

Atbash Table (Taken From Wikipedia)-

<table><tbody><tr style="vertical-align:top"><th scope="row">  Plain</th><td>  A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td><td>G</td><td>H</td><td>I</td><td>J</td><td>K</td><td>L</td><td>M</td><td>N</td><td>O</td><td>P</td><td>Q</td><td>R</td><td>S</td><td>T</td><td>U</td><td>V</td><td>W</td><td>X</td><td>Y</td><td>Z</td></tr><tr style="vertical-align:top"><th scope="row">  Cipher</th><td> Z</td><td>Y</td><td>X</td><td>W</td><td>V</td><td>U</td><td>T</td><td>S</td><td>R</td><td>Q</td><td>P</td><td>O</td><td>N</td><td>M</td><td>L</td><td>K</td><td>J</td><td>I</td><td>H</td><td>G</td><td>F</td><td>E</td><td>D</td><td>C</td><td>B</td><td>A</td></tr></tbody></table>

Knowing all this, we can take our cipher text and manually decrypt it with the above table or use a tool like [CyberChef](https://cyberchef.org/ "CyberChef Website") to get the following secret message.

> Grant_me_access_to_the_map_please

![Atbash Cypher Decrypted](./Assets/atbash-decrypted.png "Atbash Cypher Decrypted")

### The Keeper Key

### What is the filename of the text file (without the file extension)

#### [BACK TO TOP](#the-evil-within "Jump To Top")

---

## Task 3 - Help Mee

### Who is locked up in the cell?

### There is something weird with the .wav file. What does it say?

### What is the FTP Username

### What is the FTP User Password

#### [BACK TO TOP](#the-evil-within "Jump To Top")

---

## Task 4 - Crack It Open


### The key used by the program

### What do the crazy long numbers mean when there decrypted.

#### [BACK TO TOP](#the-evil-within "Jump To Top")

---

## Task 5 - Go Capture The Flag

### user.txt

### root.txt

### **Bonus**: Defeat Ruvik

#### [BACK TO TOP](#the-evil-within "Jump To Top")
