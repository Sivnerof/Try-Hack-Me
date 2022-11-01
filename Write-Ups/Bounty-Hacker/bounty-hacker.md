# Bounty Hacker

![Main Characters From Cowboy Bebop](./Assets/crew.jpg)

This [Cowboy Bebop](https://en.wikipedia.org/wiki/Cowboy_Bebop "Cowboy Bebop Wikipedia") themed room created by [Sevuhl](https://twitter.com/sevuhl "Sevuhls Twitter") is one of the many free [CTF's](https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity) "CTF Wikipedia") available on the [TryHackMe](https://tryhackme.com "TryHackMe Website") website aimed at begginers.

---


## Deploy the machine.

Start the attack box or connect to TryHackMe via VPN. If you don't know how to connect with the VPN, check out the [OpenVPN room](https://tryhackme.com/room/openvpn "OpenVPN Room").

## Find open ports on the machine

Start by navigating to the website to check for connectivity or alternatively [ping](https://www.geeksforgeeks.org/ping-command-in-linux-with-examples/ "Ping Information") the IP.

```bash
ping <IP Address>
```

Once we confirm the machine is up we can start a port scan using [nmap](https://www.freecodecamp.org/news/what-is-nmap-and-how-to-use-it-a-tutorial-for-the-greatest-scanning-tool-of-all-time/ "FreeCodeCamp Tutorial For NMAP") to see what services are running on the machine.

```bash
nmap -A <IP Address>
```

The results of this nmap scan return three open ports (21, 22, 80) and the services they're currently running (ftp, ssh, http).

 But one of these sticks out and that is:

* 21/tcp open  ftp     vsftpd 3.0.3
    * ftp-anon: Anonymous FTP login allowed (FTP code 230)

[Port 21](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers "Wikipedia List Of Port Numbers And Services") is open and allows Anonymous login for the [FTP](https://www.linkedin.com/pulse/pentesting-exploiting-ftp-servers-kubotor "Article on FTP, and anonymous login") service.

Type the following command in your terminal and when it asks for your name use the word "**anonymous**"

```bash
ftp <IP Address>
```

After logging in execute the following command to list all files in the directory:

```bash
ls -la
```

You should see the following output:

* -rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
* -rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt

To download these to your current directory type:

```bash
get locks.txt
get task.txt
```

## Who wrote the task list?

Reading the [task.txt](./Assets/task.txt "task.txt file") gives us the answer to this step.

```text
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin
```

## What service can you bruteforce with the text file found?


## What is the users password?



## user.txt


## root.txt
