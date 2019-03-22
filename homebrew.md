### Homebrew

I love [Homebrew](https://brew.sh).  I have never had an issue with it, and I had nasty problems with Fink and more than a few with Macports.

I decided that if I want to test (one more time) how to install Homebrew and get my computing environment working, I need to uninstall it first.  :(

I did that first, but I describe it at the end of this write-up.

#### Install Homebrew

On macOS, a clean install of the OS comes with `/usr` but not `/usr/local`.  `/usr` is owned by `root`, and it requires `sudo` to `mkdir local`.  

First, let's do that

```
> sudo mkdir local
>> ls -al
drwxr-xr-x     2 root  wheel     68 Jul  9 16:30 local
...
```

Obviously, that is not what we want!  We want the user (an admin) to be the owner of ``/usr/local``.

```
> sudo chown telliott local
> sudo chgrp staff local
> ls -al
...
drwxr-xr-x     2 telliott  staff     68 Jul  9 16:30 local
...
>
```

That looks better.

Now, for Homebrew.  [link](https://brew.sh)

```
> /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
==> This script will install:
/usr/local/bin/brew
/usr/local/share/doc/homebrew
/usr/local/share/man/man1/brew.1
/usr/local/share/zsh/site-functions/_brew
/usr/local/etc/bash_completion.d/brew
/usr/local/Homebrew
==> The following new directories will be created:
/usr/local/Cellar
/usr/local/Homebrew
/usr/local/Frameworks
/usr/local/bin
/usr/local/etc
/usr/local/include
/usr/local/lib
/usr/local/opt
/usr/local/sbin
/usr/local/share
/usr/local/share/zsh
/usr/local/share/zsh/site-functions
/usr/local/var

Press RETURN to continue or any other key to abort
```

Takes a bit and triggers LittleSnitch, but it goes.

    > brew doctor
    Your system is ready to brew.
    > 

Note:  Homebrew will eventually write to `~/Library/Caches/Homebrew/` and `~/Library/Logs/Homebrew/` as well.

I have to look at a list of what I used to have and decide what I want.  Here is my list so far

- python
- git
- libdvdcss
- sphinx
- youtube-dl

So

```
brew install python
...
```

We build Python from source, it isn't clear why, and this didn't happen three weeks ago or so.  This is Python 2.13, which I still prefer.

(It turned out that for some reason when I upgraded Xcode, it did not install and actually removed, the Developer's tools).

    Pip and setuptools have been installed. To update them
    pip install --upgrade pip setuptools

Why not?

I look at Python modules with `help('modules')`, but there are already so many in the new default install that I can't tell what else I might want.

    `rsa`
    `pygments`

So

```
pip install rsa
...
```

#### LaTeX

The last big thing is support for LaTeX.

I install Basic TeX from [here](http://www.tug.org/mactex/morepackages.html).

Because I suspect there will be issues, I check for the wrong owner in `/usr/local`

```
> ls -al
...
drwxr-xr-x   3 root            wheel   102 Jun  7 12:10 texlive
...
```

Still the same problem, I wonder why.  Easily fixed with `chown` and `chgrp`.

Check for issues with LaTeX by running an example.  Looks good.  At least it didn't change the owner of `/usr/local`.
    
#### Uninstall first

Here is my uninstall experience ([instructions](http://docs.brew.sh/FAQ.html)):

```bash
> ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"
Warning: This script will remove:
/Users/telliott/Library/Caches/Homebrew/
/Users/telliottLibrary/Logs/Homebrew/
/usr/local/Cellar/
...
/usr/local...
```

Did it.

```
==> /usr/bin/sudo /usr/bin/find /usr/local/Frameworks /usr/local/bin /usr/local/etc /usr/local/include /usr/local/lib /usr/local/opt /usr/local/sbin /usr/local/share /usr/local/var -name .DS_Store -delete
Password:
```

was a bit scary.  But the `sudo` is just to run find on `/usr/local...`.  A bit silly, if you ask me.

At the end:

``` bash
/usr/local/bin/
/usr/local/etc/
/usr/local/lib/
/usr/local/remotedesktop/
/usr/local/share/
/usr/local/texlive/
You may wish to remove them yourself.
>
```

It was unable to remove these directories.

I think I will.  (Remember we will need `texlive` again too).

    > pwd
	/usr
	> sudo rm -r local
	Password:
	>

That's it.



