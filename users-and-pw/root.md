### Enable root

#### System Preferences

You can activate root from the command line 
or in System Preferences > Users & Groups.

However, you can't do any of this if you're not an Admin.

[link1](https://support.apple.com/en-us/HT204012)
[link2](https://www.howtogeek.com/howto/35132/how-to-enable-the-root-user-in-mac-os-x/)

- Users & Groups
- Authenticate
- Click Login Options
- Click on Join (Network Account Server)

<img src="figs/root1.png" style="width: 400px;" />

```
Open Directory Utility...
Authenticate (in that window)
```

<img src="figs/root2.png" style="width: 400px;" />


- Edit
- Change Root Password or Enable Root User


#### Command line

From the command line:

```
> dsenableroot
username = telliott_admin
user password:
root password:
verify root password:

dsenableroot:: ***Successfully enabled root user.
>
```

To disable:

```
> dsenableroot -d
username = telliott_admin
user password:

dsenableroot:: ***Successfully disabled root user.
>
```

### Things to do as root

#### su stuff


```
> su
Password:
sh-3.2# whoami
root
sh-3.2#
```

Now you can do anything that normally requires ``sudo`` and an Admin password.

For example, you can convert a Standard account to an Admin one as described in [dscl.md](dscl.md).

#### Password resets

Following advice on the web:

If necessary, restart in recovery mode:  Cmd+R, Restart.

Then just go to the Utilities menu and choose Terminal.  Enter

```
resetpassword
```

Click on the newly opened window and select the volume Macintosh HD.  Now select SystemAdministrator(root) from the dropdown list.  

Type the password twice and click save.

Except there is no longer any selectable volume and no dropdown.

---------------------------------

However, you can do (from Terminal in recovery mode):

```
dscl . -append /Groups/admin GroupMembership username
```

(root login is not required, because you are logged in as root already).

It is possible to set things so the above doesn't work without a firmware password.

https://discussions.apple.com/thread/8016903

Also:

Multiple steps to get root from single user mode here:
http://sachinparmarblog.com/enable-root-user-password-in-single-user-mode/

```
/sbin/fsck -fy
/sbin/mount -uw /
launchctl load /System/Library/LaunchDaemons/com.apple.opendirectoryd.plist
passwd root
```

you will be prompted to enter a password twice

reboot



