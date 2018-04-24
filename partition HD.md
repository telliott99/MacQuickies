#### New Volume

The old instructions were to launch Disk Utility, select the desired Hard Drive, click ``Partition`` and ``+`` and then choose the size.  

With the new APFS file system, there is a different approach, which is to add a "volume to container."  OK.

I named the new volume **Tester**.

It is hard to believe, but the owner/group of this account are

```
> ls -al /Volumes/Tester/Users/te
total 8
drwxr-xr-x+ 11 telliott_admin  staff   352 Feb 26 11:59 .
```

That is, the auto login Admin user of the original volume is the owner of the account on the new volume.  How is that possible?  I will explore and get back to you.

#### Install High Sierra

In any event, the next step is to install High Sierra.  I have the installer on a USB stick.  Apple's instructions for making one of these are [here](https://support.apple.com/en-us/HT201372).

