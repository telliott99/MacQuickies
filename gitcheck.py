# python3 gitcheck.py /Users/telliott_admin/Github

import os, sys, subprocess
from subprocess import run

path = sys.argv[1]
L = os.listdir(path)
L.sort()

for sub in L:
    p = path + '/' + sub
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
