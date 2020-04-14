#!/usr/bin/python
#
# PDFlib client: hello example in Python
#

from sys import exc_info
from traceback import print_tb
from PDFlib.PDFlib import *

# create a new PDFlib object
p = PDFlib()
searchpath = "../data"

try:
    # This means we must check return values of load_font() etc.
    p.set_option("errorpolicy=return")

    # Set the search path for font files
    p.set_option("SearchPath={{" + searchpath +"}}")

    if p.begin_document("hello.pdf", "") == -1:
        raise Exception("Error: " + p.get_errmsg())

    p.set_info("Author", "Thomas Merz")
    p.set_info("Creator", "hello.py")
    p.set_info("Title", "Hello world (Python)")

    p.begin_page_ext(0,0, "width=a4.width height=a4.height")
    fontopt = "fontname=NotoSerif-Regular encoding=unicode fontsize=24"
    p.fit_textline("Hello world!", 50, 700, fontopt)
    p.fit_textline("(says Python)",  50, 676, fontopt)

    p.end_page_ext("")

    p.end_document("")     

except PDFlibException:
    print("PDFlib exception occurred:\n[%d] %s: %s" %
	((p.get_errnum()), p.get_apiname(),  p.get_errmsg()))
    print_tb(exc_info()[2])

except Exception:
    print("Exception occurred: %s" % (exc_info()[0]))
    print_tb(exc_info()[2])

finally:
    p.delete()
