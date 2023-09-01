# Lesson Learned?

![Lesson Learned?](./Assets/lesson-learned.png "Lesson Learned Room Avatar")

## Summary

[Lesson Learned](https://tryhackme.com/room/lessonlearned "Lesson Learned CTF on TryHackMe") is a beginner-friendly CTF hosted on [TryHackMe](https://tryhackme.com/ "TryHackMe Website") and created by [Tib3rius](https://tryhackme.com/p/Tib3rius "TryHackMe user profile for Tib3rius").

This CTF requires basic knowledge of:

* Safer alternatives to common ```SQL Injections```.

---

## Contents

* [Getting Started](#getting-started "Jump To Section")

* [Getting Kicked Out](#getting-kicked-out "Jump To Section")

* [The Right Way](#the-right-way "Jump To Section")

---

## Getting Started

For this room we're given the following description:

> This is a relatively easy machine that tries to teach you a lesson, but perhaps you've already learned the lesson? Let's find out.
>
> Treat this box as if it were a real target and not a CTF.
>
> Get past the login screen and you will find the flag. There are no rabbit holes, no hidden files, just a login page and a flag. Good luck!

The above description let's us know that this CTF will be a straight-forward login page bypass. There will be no need for a network scan or directory enumeration, so we can skip the usual tools like NMAP and GoBuster and move straight to website.

[Back To Top](#lesson-learned "Jump To Top")

---

## Getting Kicked Out

Once we navigate to the URL for the website we'll see a simple login page. Reviewing the source code reveals nothing, just bare-bones HTML and CSS.

Our first instinct may be to perform a ```SQL Injection``` like ```admin' OR 1 = 1-- -```, but when thinking of performing a SQL Injection it is important to consider the context into which the injection is being placed. Is it a ```SELECT``` statement or a ```UPDATE``` statement? Into which part of the SQL query are we injecting into? Here we can guess that we're injecting into a ```SELECT``` query based on the fact that the login form will query the SQL database for our username. However, we don't know _exactly_ what the program does with our input, we can only guess. Say, for instance, that we wanted to inject ```admin' OR 1 = 1-- -``` into a ```SELECT``` statement. This would return every row. However, if the same injection is inserted into a ```DELETE``` statement, every row would be deleted. This is what makes SQL injections so dangerous.

We can test out the wrong way to inject into the database with the following injection:

* Username: ```test' OR 1 = 1-- -``` (MySQL comments need to start with a space so the dash following the space is used to ensure that the space before is not stripped, you can use anything though. For instance, ```test' OR 1 = 1-- x```, is also a valid injection.)

* Password: ```anything```

After our SQL injection, we'll get the following message:

![CTF Error Message](./Assets/error-message.png "CTF Error Message")

The flag has been destroyed due to our injection making it's way to a ```DELETE``` statement. We'll need to restart the room and try a "less destructive" method.

[Back To Top](#lesson-learned "Jump To Top")

---

## The Right Way

![Tweet from Tib3rius on safer alternatives to 1 = 1 injection](./Assets/tib3rius-tweet-on-sql-injection.png "Tweet from Tib3rius on safer alternatives to 1 = 1 injection")

Instead of trying to return every row with ```test' OR 1 = 1-- -``` and hoping we're logged into the account of the user in the first row we can use a SQL injection like ```test'; -- -``` or ```test' AND 1 = 1 -- -```. The problem with this safer alternative is that we need a valid username. So our next step is to enumerate possible usernames using a tool like [Hydra](https://www.kali.org/tools/hydra/ "Kali Linux Documentation For Hydra").

The syntax for bruteforcing usernames with Hydra on a login form that uses ```POST``` requests is the following:

```hydra -L /path/to/wordlist -p testing IP_ADDRESS -s 80 http-post-form "/index.php:username=^USER^&password=^PASS^":"Invalid username and password."```

Breakdown of above command:

* ```-L /path/to/wordlist``` - .

![Success Page](./Assets/success.png "Success Page")

THM{aab02c6b76bb752456a54c80c2d6fb1e}

```test' UNION SELECT null-- -```

[Back To Top](#lesson-learned "Jump To Top")

---
