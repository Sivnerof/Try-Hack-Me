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

For this challenge we're given no files to download, no _visible_ text to analyze, decrypt, or decipher.

All we have is the text "Huh, where is the flag?".

Interestingly, this lack of clues ends up being our biggest clue.

We know that a flag exists but we can't see it. So where is it? If there is not a single visible clue here, then what we are looking for must be "invisible".

Let's find what this challenge section really contains by using the Dev Tools in our browser.

If we inspect the ```Huh, where is the flag?``` text we'll see it's written within a paragraph tag (```<p>```) and it's not the only thing in there.

```html
<p>Huh, where is the flag? <span style="color:rgb(255, 255, 255);"><span style="background-color:rgb(255, 255, 255);">THM{wh173_fl46}</span></span><br></p>
```

There's our flag, hidden within the same paragraph and styled with white font on a white background, ```THM{wh173_fl46}```.

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## QRrrrr

For this challenge we're given a QR code and all we need to do is scan it on order to get the flag.

![QR.png](./Assets/QR.png "Qr Code")

I didn't want to scan the code for security reasons so instead I used [this website](https://zxing.org/w/decode.jspx "QR Decoder Website") and uploaded the file, where it returned the following flag...

```THM{qr_m4k3_l1f3_345y}```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Reverse it or read it?

For this challenge we're given an executable file named [hello.hello](./Assets/hello.hello "hello.hello executable file") and told to "reverse or read it".

In order to "read it" we can use the ```strings``` command and parse through the output for any strings that may resemble a flag.

But since we know all flags start with ```THM``` we can pipe the output from ```strings``` to ```grep``` for cleaner output.

```
$ strings hello.hello | grep THM

THM{345y_f1nd_345y_60}
```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Another decoding stuff

For this challenge we're given the encoded string ```3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L```.

One quick way to solve this, if you don't know what kind of encoding was used, is to use the ```Magic``` operation in [CyberChef](https://cyberchef.org/ "Cyber Chef Website").

![magic-operation.png](./Assets/magic-operation.png "Magic operation on encoded string")

The ```Magic``` operation identifies ```3agrSy1CewF9v8ukcSkPSYm3oKUoByUpKG4L``` as the ```Base58``` encoding of the flag ```THM{17_h45_l3553r_l3773r5}```.

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Left or right

For this challenge we're given the flag in its encrypted version
(```MAF{atbe_max_vtxltk}```) and told that "ROT13 is too mainstream".

This encrypted flag looks like a basic substitution cipher which we can confirm by using the ```ROT13 Bruteforce``` operation in [CyberChef](https://cyberchef.org/ "Cyber Chef Website").

The output shows this encrypted flag was rotated with a key of 7. Which is the original key used for the famous Caesar Cipher.

Here is the result of shifting all characters 7 positions.

```THM{hail_the_caesar}```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Make a comment

For this challenge, once again, we're given no downloadable files to analyze or text to decode/decrypt. Time to use the developer tools and inspect this challenges section in order to find any hidden information.

If we look at the ```<div>``` element where the challenge description text is stored, we'll find another paragraph that is never seen in the browser.

```html
<div class="room-task-desc-data">
    <p>No downloadable file, no ciphered or encoded text. Huh .......<br><p> 
    <p style="display:none;"> THM{4lw4y5_ch3ck_7h3_c0m3mn7} </p>
</div>
```

So there's our flag, hidden within a paragraph element and styled to never display, ```THM{4lw4y5_ch3ck_7h3_c0m3mn7}```.

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Can you fix it?

For this challenge, we're given a "PNG" file and told "I accidentally messed up with this PNG file. Can you help me fix it? Thanks, ^^".

Before we start "fixing" this PNG let's check what Linux identifies the file as with the ```file``` command.

```
$ file spoil.png

spoil.png: data
```

Linux says the file is "data" _not_ a PNG.

If we check the hex signature of the file with the ```xxd``` command and try to identify it on the [Wikipedia for file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures "File signature WikiPedia"), we'll see that nothing matches.

```
$ xxd spoil.png
00000000: 2333 445f 0d0a 1a0a 0000 000d 4948 4452  #3D_........IHDR
```

Let's change the hex signature with ```hexedit``` to ```89 50 4E 47 0D 0A 1A 0A``` (PNG signature) and see if that fixes it.

![spoil-backup.png](./Assets/spoil-backup.png "restored image of spoil.png")

There it is, changing the file signature worked. The restored image is the TryHackMe logo with a flag underneath that reads ```THM{y35_w3_c4n}```.

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Read it

For this challenge all we're given is the text "Some hidden flag inside Tryhackme social account".

The title of this section (Read It) hints that we should look within [TryHackMe's Reddit account](https://www.reddit.com/r/tryhackme/ "TryHackMe's Sub Reddit") for the flag.

If we search the terms [reddit flag](https://www.reddit.com/r/tryhackme/search/?q=reddit%20flag "TryHackMe Reddit Search For Flag") within the subreddit we'll find the following five posts.

![Reddit Search](./Assets/reddit-search.png "Reddit Search")

The post titled "[New room Coming soon!](https://www.reddit.com/r/tryhackme/comments/eizxaq/new_room_coming_soon/ "Flag location on Reddit")" contains an image of a flag with the words "Vol. 1" just like the name of this room.

If we view the image in this post we can see in tiny little letters the flag for this challenge.

```THM{50c14l_4cc0un7_15_p4r7_0f_051n7}```

![flag](./Assets/flag.png "flag.png")

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## Spin my head

For this challenge we're given the following text.

```brainfuck
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++++.------------.+++++.>+++++++++++++++++++++++.<<++++++++++++++++++.>>-------------------.---------.++++++++++++++.++++++++++++.<++++++++++++++++++.+++++++++.<+++.+.>----.>++++.
```

If you've spent enough time programming you might have come across some really [strange programming languages](https://en.wikipedia.org/wiki/Esoteric_programming_language "Wikipedia For Esoteric Programming Languages"), in which case you might immediately recognize that this "gibberish" isn't gibberish at all. It's a programming language named [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck "Brainfuck Wikipedia Entry").

Knowing that, we can take the text and paste it into a [Brainfuck Interpreter](https://www.dcode.fr/brainfuck-language "Website to interpret Brainfuck"), which reveals the following flag.

```THM{0h_my_h34d}```

### [BACK TO TOP](#ctf-collection-volume-1 "Jump To Top")

---

## An exclusive!

For this challenge we're given the following two strings.

```S1: 44585d6b2368737c65252166234f20626d```

```S2: 1010101010101010101010101010101010```

Along with some text that says "Exclusive strings for everyone!". This along with the title of the challenge (An exclusive!) suggests that we'll need to [XOR](https://en.wikipedia.org/wiki/XOR_cipher "Wikipedia Entry For Xor Ciphers") (exclusively or) the two strings in order to recieve the flag.

Since the second string only has two values that repeat we can guess this is the key and string one is our flag.

Another thing to note here is that although the second flag looks like binary it's actually hexadecimal.

If we take both strings and put them into a [Hexadecimal Xor calculator](https://onlinehextools.com/xor-hex-numbers "Hexadecimal XOR Calculator") we'll get the following string back.

```54484d7b3378636c75353176335f30727d```

![xor-calculator.png](./Assets/xor-calculator.png "Result of Xor Calculation On Two Strings")

Taking this string and converting it into ASCII reveals the following flag. 

```THM{3xclu51v3_0r}```

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