TL;DR

Use the [Swift version](join.swift)

#### Combine pdfs into one

The problem came up of combining a series of pdf's into a single document.  Of course, you can use Preview to do this.

But [this](https://apple.stackexchange.com/questions/230437/how-can-i-combine-multiple-pdfs-using-the-command-line) alerted me to another approach.

There is a huge number of "automator" scripts in 

```
> cd /System/Library/Automator
> ls | wc
     288     990    8226

```

One of them is

```
Combine PDF Pages.action
```

And inside that "package" is a Python [script](/System/Library/Automator/Combine PDF Pages.action/Contents/Resources/join.py)

It's got some extra stuff, so I boiled it down to the essentials and made the method names less convoluted:

```
# /usr/bin/python script.py

import sys
from CoreFoundation import *
from Quartz.CoreGraphics import *

pdf_from_url = CGPDFDocumentCreateWithURL
make_url = CFURLCreateFromFileSystemRepresentation
alloc = kCFAllocatorDefault

num_pages = CGPDFDocumentGetNumberOfPages
get_pg    = CGPDFDocumentGetPage
get_box   = CGPDFPageGetBoxRect
begin_pg  = CGContextBeginPage
draw_pg   = CGContextDrawPDFPage
end_pg    = CGContextEndPage

ctx_from_url = CGPDFContextCreateWithURL

#---------------------------------

def pdf_from_path(path):
	return pdf_from_url(
	    make_url(alloc, path, len(path), False))

def write_pg(ctx, doc, pageNum):
	page = get_pg(doc, pageNum)
	if page:
		box = get_box(page, kCGPDFMediaBox)
		if CGRectIsEmpty(box):
			box = None
			
		begin_pg(ctx, box)
		draw_pg(ctx, page)
		end_pg(ctx)

#---------------------------------

out = 'out.pdf'
args = sys.argv[1:]

# output context
ctx = ctx_from_url(
    make_url(alloc, out, len(out), False), None, None)

# input docs
docs = map(pdf_from_path, args)

maxPages = 0
for doc in docs:
	if num_pages(doc) > maxPages:
		maxPages = num_pages(doc)

for doc in docs:
	for n in xrange(1, maxPages + 1) :
		write_pg(ctx, doc, n)

CGPDFContextClose(ctx)
```

It does what it says, but it's pretty slow, maybe 3 seconds.