# CTF Collection, Volume 1

![CTF Collection, Volume 1 Logo](./Assets/holiday.png "Logo for CTF Collection, Volume 1")

## Summary

[CTF Collection, Volume 1](https://tryhackme.com/room/ctfcollectionvol1 "CTF Collection, Volume 1 on TryHackMe") is a begginer <abbr title="Capture The Flag">CTF</abbr> with 20 challenges created by [DesKel](https://tryhackme.com/p/DesKel "Deskel TryHackMe"). You can find the room on [TryHackMe's official website](https://tryhackme.com/ "TryHackMe Website") along with other <abbr title="Capture The Flag">CTF's</abbr>.

---

## Challenges

* [What does the base said?](#what-does-the-base-said "Jump To Challenge Section")

* [Meta meta](#meta-meta "Jump To Challenge Section")

* [Mon, are we going to be okay?](#mon-are-we-going-to-be-okay "Jump To Challenge Section")

* [Erm......Magick](#ermmagick "Jump To Challenge Section")

* [QRrrrr](#qrrrrr "Jump To Challenge Section")

* [Reverse it or read it?](#reverse-it-or-read-it "Jump To Challenge Section")

* [Another decoding stuff](#another-decoding-stuff "Jump To Challenge Section")

* [Left or right](#left-or-right "Jump To Challenge Section")

* [Make a comment](#make-a-comment "Jump To Challenge Section")

* [Can you fix it?](#can-you-fix-it "Jump To Challenge Section")

* [Read it](#read-it "Jump To Challenge Section")

* [Spin my head](#spin-my-head "Jump To Challenge Section")

* [An exclusive!](#an-exclusive "Jump To Challenge Section")

* [Binary walk](#binary-walk "Jump To Challenge Section")

* [Darkness](#darkness "Jump To Challenge Section")

* [A sounding QR](#a-sounding-qr "Jump To Challenge Section")

* [Dig up the past](#dig-up-the-past "Jump To Challenge Section")

* [Uncrackable!](#uncrackable "Jump To Challenge Section")

* [Small bases](#small-bases "Jump To Challenge Section")

* [Read the packet](#read-the-packet "Jump To Challenge Section")

---

## What does the base said?

For this challenge we have to decode the following string...

```VEhNe2p1NTdfZDNjMGQzXzdoM19iNDUzfQ==```

The double equals signs on the end are a hint that this string is encoded in ```Base64```.

Using a Base64 decoder online such as [CyberChef](https://cyberchef.org/ "Cyber Chef Website") reveals the following decoded string...

```THM{ju57_d3c0d3_7h3_b453}```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Meta meta

For this challenge we're given an image of Earth from space titled [Findme.jpg](./Assets/Findme.jpg "Findme Image").

![Findme.jpg](./Assets/Findme.jpg "View of Earth from space")

The title ("meta meta") hints that the flag is hidden within the metadata of the image. This can be confirmed by using ```exiftool``` and  finding ```THM{3x1f_0r_3x17}``` under the ```Owner Name```.

```
$ exiftool Findme.jpg
ExifTool Version Number         : 12.40
File Name                       : Findme.jpg
Directory                       : .
File Size                       : 34 KiB
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
X Resolution                    : 96
Y Resolution                    : 96
Exif Byte Order                 : Big-endian (Motorola, MM)
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
Flashpix Version                : 0100
Owner Name                      : THM{3x1f_0r_3x17}
Comment                         : CREATOR: gd-jpeg v1.0 (using IJG JPEG v62), quality = 60.
Image Width                     : 800
Image Height                    : 480
Encoding Process                : Progressive DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 800x480
Megapixels                      : 0.384
```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Mon, are we going to be okay?

For this challenge we're given an image of two Stegosauruses about to be hit by a meteor. A hint at using steganography again, specifically a tool called [steghide](https://www.kali.org/tools/steghide/ "Kali Linux Steghide Manual").

![Extinction.jpg](./Assets/Extinction.jpg "A Stegasaurus mother comforting her child as a meteorite falls to the Earth")

To extract any hidden files from this image we're going to use ```steghide``` with two arguments, ```--extract``` and ```-sf```.

When prompted for the password we're going to press enter, leaving the password field empty.

If succesful we should see steghide extract a text file named [Final_message.txt](./Assets/Final_message.txt "Text file that was embedded in Extinction.jpg").

```
$ steghide extract -sf Extinction.jpg
Enter passphrase: 
wrote extracted data to "Final_message.txt".
```

Within the text file we can find our flag.

```
It going to be over soon. Sleep my child.

THM{500n3r_0r_l473r_17_15_0ur_7urn}
```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Erm......Magick

Huh, where is the flag? THM{wh173_fl46}

```html
<p>Huh, where is the flag? <span style="color:rgb(255, 255, 255);"><span style="background-color:rgb(255, 255, 255);">THM{wh173_fl46}</span></span><br></p>
```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## QRrrrr



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Reverse it or read it?



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Another decoding stuff



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Left or right



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Make a comment



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Can you fix it?



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Read it



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Spin my head



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## An exclusive!



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Binary walk



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Darkness



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## A sounding QR



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Dig up the past



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Uncrackable!



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Small bases



### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Read the packet

---

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")