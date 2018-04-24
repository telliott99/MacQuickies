Historically, there were 1 + 9 modes shown by ``ls -l``, as in ``-rwxr-----`` or ``drwxr-x---``.  

You can see the new ones here:

```
> ls -al
total 146688
drwxr-x---@ 14 telliott_admin  staff       448 Feb 27 11:03 .
drwxr-x---+ 61 telliott_admin  staff      1952 Feb 27 09:31 ..
-rwxr-----@  1 telliott_admin  staff        18 Feb 27 09:30 x.txt
> 
``` 

The trailing symbols are ``@`` and ``+``.

The ``+`` indicates that the entity has an access control list, while the ``@`` means it has extended attributes

```
> ls -aled ..
drwxr-x---+ 61 telliott_admin  staff  1952 Feb 27 09:31 ..
 0: group:everyone deny delete
> ls -aled .
drwxr-x---@ 14 telliott_admin  staff  448 Feb 27 11:08 .
 0: group:everyone deny delete
>
```

The ``e`` flag is to show the ACL and the ``d`` flag is to suppress listing of all the directory contents.

#### Extended attributes

The ``@`` indicates extended attributes for the Desktop directory.

```
> ls -ael ~
-rwxr-x---@   1 telliott_admin  staff  28676 Feb 27 10:18 .DS_Store
..
-rw-r--r--@   1 telliott_admin  staff    114 Feb 15 08:51 @to_make.txt
..
drwxr-x---@  14 telliott_admin  staff    448 Feb 27 11:10 Desktop
 0: group:everyone deny delete
..
drwxr-x---@  45 telliott_admin  staff   1440 Feb  7 17:19 Food
..
> 
```

Some of my files and folders have extended attributes.  To view them:

```
> xattr -l Food
com.dropbox.attributes:
00000000  78 9C AB 56 4A 29 CA 2F 48 CA AF 88 4F CB CC 49  |x..VJ)./H...O..I|
00000010  CD 4C 89 CF C9 4F 4E CC 51 B2 52 A8 56 CA 4D 4C  |.L...ON.Q.R.V.ML|
00000020  CE C8 CC 03 89 25 96 94 14 81 85 52 12 4B 12 81  |.....%.....R.K..|
00000030  0C 25 D7 22 4B 3F B7 6C C7 12 CF F0 48 1F C3 EC  |.%."K?.l....H...|
00000040  B2 74 8F 7C A7 AA B0 40 5B 5B A5 DA DA 5A 00 C6  |.t.|...@[[...Z..|
00000050  40 1C 87                                         |@..|
00000053
> xattr -l @to_make.txt
com.apple.TextEncoding: utf-8;134217984
com.apple.lastuseddate#PS:
00000000  36 90 85 5A 00 00 00 00 2C 1E E8 37 00 00 00 00  |6..Z....,..7....|
00000010
com.apple.metadata:_kMDItemUserTags:
00000000  62 70 6C 69 73 74 30 30 A0 08 00 00 00 00 00 00  |bplist00........|
00000010  01 01 00 00 00 00 00 00 00 01 00 00 00 00 00 00  |................|
00000020  00 00 00 00 00 00 00 00 00 09                    |..........|
0000002a
> 
> 

```

So, these can be quite complex.  They do not have to be Apple stuff only.  The Food directory was for a while on Dropbox.  It still carries an ``xattr`` from that time.

To delete this:

```
Last login: Tue Feb 27 11:10:54 on ttys000
> cd Desktop
> cd ..
> xattr -d com.dropbox.attributes Food
> ls -aeld Food
drwxr-x---  45 telliott_admin  staff  1440 Feb  7 17:19 Food
> 
```

The man page for ``xattr`` explains how to write extended attributes.  I did this for ``x.txt`` but it did not go as I expected:

```
> xattr -w com.te abc x.txt
> ls -l@ x.txt
-rwxr-----@ 1 telliott_admin  staff  18 Feb 27 09:30 x.txt
	com.apple.TextEncoding	15 
	com.apple.lastuseddate#PS	16 
	com.apple.metadata:kMDLabel_2mayoxv2tt5ot4v322v7ho3ffy	89
	com.te	 3
> xattr -l x.txt
com.apple.TextEncoding: utf-8;134217984
..
com.te: abc
```

The process of trying to write caused other extended attributes to show up.

The names can be seen with ``ls -l@`` and the values with ``xattr -l``.

#### .DS_Store

>    DS_Store is a file that stores custom attributes of its containing folder, such as the position of icons or the choice of a background image.


This invisible file has extended attributes:

```
> ls -l@ .DS_Store 
-rwxr-x---@ 1 telliott_admin  staff  10244 Feb 27 11:23 .DS_Store
	com.apple.FinderInfo	   32 
> xattr -p com.apple.FinderInfo .DS_Store
20 20 20 20 20 20 20 20 00 10 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
>
```

though what value that information would have, I can't say.