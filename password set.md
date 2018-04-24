#### Lost password

You are working on your grandmother's Mac.  She has no idea what an Admin account is, let alone the password for it.

Start the computer in single user mode, by holding down ``Cmd+S``.

The system will come up virtually immediately, a Terminal window with white text on black background.  Lots of it.  

I have not found a way to scroll back and read it all.

Before the prompt

```
localhost:/ root #
```
you find a hint, which you follow:

```
mount -uw /
```

which allows you to write to the the drive.  Now do

```
launchctl load /System/Library/LaunchDaemons/com.apple.opendirectoryd.plist
passwd username
```

where username is discovered, if necessary, from ``ls /Users``.

The prompts will ask you to enter and confirm a new password, with no requirement for the old one.

Exit this mode with

```
reboot
```

#### pwpolicy

``pwpolicy`` is a utility available in the Terminal whose primary usage is to "get and set password policies".  For example, to enforce a minimum password length.

However, it can also be used to reset passwords.  

```
> pwpolicy -a te -u te -setpassword
Setting password for te
Enter new password for te:
Verify new password:
Password for authenticator te:
>
```
