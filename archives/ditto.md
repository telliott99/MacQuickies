According to [this](https://superuser.com/questions/114011/extract-large-zip-file-50-gb-on-mac-os-x?noredirect=1), ``ditto`` has no problem with large files (> 10GB).

#### ditto

Unarchiving a zip file made with the ``zip`` utility on macOS:

```
> ditto -x x.txt.zip tmp
ditto: cpio read error: bad file format
> ditto -xk x.txt.zip tmp
> cat tmp/x.txt
my data
>

``-k`` flag specifies PKZip format.

A quick look at ``man zip`` confirms that is the format that it uses.