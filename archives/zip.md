#### zip

There is some discussion of problems with command-line zip on macOS [here](http://hints.macworld.com/article.php?story=20061128120143184)...

From [wikipedia](https://en.wikipedia.org/wiki/Zip_(file_format):


> A ZIP file may contain one or more files or directories that may have been compressed. The ZIP file format permits a number of compression algorithms

To construct a zipped archive on macOS, select the file or directory in the Finder and do File > Compress <target>.  Or from the command line just

```
zip <outfile> <input>
```

If we do that with a simple text file and then look at result

```
> zip x.txt.zip x.txt
  adding: x.txt (stored 0%)
> hexdump -n 4 -C x.txt.zip
00000000  50 4b 03 04                                       |PK..|
00000004
>
```

Note that the Finder's version is somewhat larger than the one produced on the command line.

According to [wikipedia](https://en.wikipedia.org/wiki/Zip_(file_format), the first four bytes should be `` 0x04034b50`` (little-endian), and we have:

```
50 4b 03 04
```

According to wikipedia the file name length is 2 bytes at offset 26 and the file name is ``n`` bytes at offset 30.

```
> hexdump -C x.txt.zip
00000000  50 4b 03 04 0a 00 00 00  00 00 4c 57 4e 4e 52 c8  |PK........LWNNR.|
00000010  73 70 08 00 00 00 08 00  00 00 05 00 1c 00 78 2e  |sp............x.|
00000020  74 78 74 55 54 09 00 03  20 90 65 5c 38 90 65 5c  |txtUT... .e\8.e\|
```

The length is ``05 00`` byte 27-28 and the file name is ``78 2e 74 78 74`` or ``x.txt``.

```
>hexdump -C x.txt.zip
00000000  50 4b 03 04 0a 00 00 00  00 00 4c 57 4e 4e 52 c8  |PK........LWNNR.|
00000010  73 70 08 00 00 00 08 00  00 00 05 00 1c 00 78 2e  |sp............x.|
00000020  74 78 74 55 54 09 00 03  20 90 65 5c 38 90 65 5c  |txtUT... .e\8.e\|
00000030  75 78 0b 00 01 04 f5 01  00 00 04 14 00 00 00 6d  |ux.............m|
00000040  79 20 64 61 74 61 0a 50  4b 01 02 1e 03 0a 00 00  |y data.PK.......|
00000050  00 00 00 4c 57 4e 4e 52  c8 73 70 08 00 00 00 08  |...LWNNR.sp.....|
00000060  00 00 00 05 00 18 00 00  00 00 00 01 00 00 00 a4  |................|
00000070  81 00 00 00 00 78 2e 74  78 74 55 54 05 00 03 20  |.....x.txtUT... |
00000080  90 65 5c 75 78 0b 00 01  04 f5 01 00 00 04 14 00  |.e\ux...........|
00000090  00 00 50 4b 05 06 00 00  00 00 01 00 01 00 4b 00  |..PK..........K.|
000000a0  00 00 47 00 00 00 00 00                           |..G.....|
000000a8
>
```

