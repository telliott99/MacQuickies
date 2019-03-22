#### Unzip

Important!  ``unzip`` can ``-t`` <i>test</i> a zipfile for errors:

```
> unzip -t x.txt.zip
Archive:  x.txt.zip
    testing: x.txt                    OK
    testing: __MACOSX/                OK
    testing: __MACOSX/._x.txt         OK
No errors detected in compressed data of x.txt.zip.
```
Normally, you'd want the ``-q`` quiet flag.

```
> unzip -tq x.txt.zip
No errors detected in compressed data of x.txt.zip.
>
```

``-p`` pipes the data to ``stdout``.

```
> unzip -p x.txt.zip
my data
>
```

To save to a file:

```
> unzip x.txt.zip
Archive:  x.txt.zip
replace x.txt? [y]es, [n]o, [A]ll, [N]one, [r]ename: r y.txt             
new name: y.txt
>
```