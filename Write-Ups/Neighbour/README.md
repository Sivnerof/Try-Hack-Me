# Neighbour

![Neighbour Logo](./neighbour-logo.png "Neighbour Logo")

## Summary

[Neighbour](https://tryhackme.com/room/neighbour "Neighbour CTF On TryHackMe") is a begginer friendly CTF hosted by [TryHackMe](https://tryhackme.com/ "TryHackMe Website") and created by [CMNatic](https://github.com/CMNatic "CMNatic GitHub Profile").

Room Description -

> Check out our new cloud service, Authentication Anywhere -- log in from anywhere you would like! Users can enter their username and password, for a totally secure login process! You definitely wouldn't be able to find any secrets that other people have in their profile, right?

This CTF requires basic knowledge of:

* Viewing ```HTML``` source code

* Insecure Direct Object References (```IDOR```)

---

## Contents

* [Getting Started](#getting-started "Jump To Getting Started")

* [Viewing Source Code](#source-code "Jump To Source Code")

* [Examining URL](#url "Jump To URL")

* [Grabbing The Flag](#flag "Jump To Flag")

---

## Getting Started

Unlike other CTF's this one tells us exactly where to start. So we won't be doing any reconnaissance or port scans. We just need to head straight over to the website.

[Back To Top](#neighbour "Jump To Top")

---

## Source Code

Once we've navigated to the website we'll see a login form with text underneath telling us that we can use a "guest" account if we choose not to login regularly.

We can find the guest credentials by viewing the comment in the ```HTML``` source code where, not only do we get the credentials ```guest:guest```, but we get a warning to stay off the admin account.

```html
<!-- use guest:guest credentials until registration is fixed. "admin" user account is off limits!!!!! -->
```

[Back To Top](#neighbour "Jump To Top")

---

## URL

After we've logged in we'll see some welcome text and another warning to stay off the "neighbours" acount.

If we view the ```HTML``` source code we'll find a comment from the developer reminding himself to update the vulnerability that leads to the admin account.

```html
<!-- admin account could be vulnerable, need to update -->
```

The vulnerabilty mentioned can be found by examining the URL we were redirected to when we logged in.

```http://<IP_Address>/profile.php?user=guest```

We can see that our profile page is loaded by the ```profile.php``` script, and it loads in the ```user``` value, which for us is ```guest```.

But if we were to replace the ```guest``` value with ```admin``` we could potentially be taken to the admins homepage.

This vulnerability is known as an Insecure Direct Object Reference or ```IDOR``` because we are directly referencing resources which we shouldn't be able to.

[Back To Top](#neighbour "Jump To Top")

---

## Flag

Once we've navigated to ```http://<IP_Address>/profile.php?user=admin``` we'll see the flag.

```
Hi, admin. Welcome to your site. The flag is: flag{66be95c478473d91a5358f2440c7af1f}
```

[Back To Top](#neighbour "Jump To Top")
