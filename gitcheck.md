#### Running git status in Python

For a directory containing more than a dozen git repos, I would like to run ``git status`` on each one, and then only print the names of those which have unsaved changes.  

We get all the sub-paths --- files and sub-directories and links, etc. --- by ``os.listdir(target_dir)``.

Some paths in the directory are not directories (like ``.DS_store``), and some directories are not git repos.  

Rather than first discovering whether a path is a directory, we just follow the Python maxim EAFP:  "easier to ask for forgiveness than permission."

```
    try:
        os.chdir(p)
    except OSError:
        continue
```

Otherwise known as "duck typing":  if it quacks, it's a duck.

Python3 has ``subprocess.run`` (not present in Python 2.7).  

One quirk of ``run`` is that the command and arguments are given as a list:  ``run(['git', 'status'])``.  You get a very strange and unhelpful error if you forget this and do ``run('git', 'status')``.

```
TypeError: bufsize must be an integer
```

We do not want the usual output of the process's ``git`` command to be output to the screen, so capture it with

```
stdout=subprocess.PIPE
stderr=subprocess.PIPE
```

The result of the ``run`` command is an object that has various properties (called attributes). 

``result.stdout`` is a bytes object which must first be decoded to a string to do substring tests on it.

```
o = result.stdout.decode("utf-8")
```

Here is the output for one run:

```
> python3 script.py /Users/telliott_admin/Github 
              Crypto OK
      CryptoQuickies OK
             Dayhoff OK
            MyCrypto OK
              MyJava OK
              MyMath OK
               MyOSX OK
            MySphinx not staged
            MySwift2 OK
              MyUnix OK
    PyBioinformatics OK
        Python2-Data OK
      PythonQuickies untracked files
            RandomPW not staged
          SimpleView OK
       SudokuBlocks3 not staged
   SudokuBlocks3.app not a git repo
       SudokuBlocks4 OK
    Swift frameworks OK
      Swift writeups OK
                 Tex OK
              Ubuntu OK
        UnixQuickies untracked files
                 old not a git repo
    python_challenge not staged
             writing untracked files
> 
```

**script.py**

```
import os, sys, subprocess
from subprocess import run

target_dir = sys.argv[1]
L = os.listdir(target_dir)
L.sort()

cmd = 'git status'
devnull = open(os.devnull, 'w')

for sub in L:
    p = target_dir + '/' + sub
    try:
        os.chdir(p)
    except OSError:
        continue
        
    result = subprocess.run(
        ['git', 'status'], 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
    
    o = result.stdout.decode("utf-8")
    e = result.stderr.decode("utf-8")
     
    if "fatal" in e:
        msg = 'not a git repo'
    elif "Untracked files" in o:
        msg = 'untracked files'
    elif "nothing to commit" in o:
        msg = "OK"
    elif "not staged" in o:
        msg = "not staged"
    else:
        msg = "unknown result"
        
    print(sub.rjust(20), msg)
```