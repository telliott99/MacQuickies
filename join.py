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
