from pyPdf import PdfFileWriter, PdfFileReader
import sys, os

def compact(filein):
	output = PdfFileWriter()
	input1 = PdfFileReader(file(filein, "rb"))
	# print the title of the document
	print "title = %s" % (input1.getDocumentInfo().title)
	n = input1.getNumPages()
	# loop over pages
	for i in range(1, n):
		curr = input1.getPage(i)
		prev = input1.getPage(i-1)
		currTxt = curr.extractText()[:-3]
		prevTxt = prev.extractText()[:-3]
		if currTxt.find(prevTxt) == 0: # prevTxt is prefix of currTxt
			pass # the current page is an extension to the previous one -> continue
		else:
			output.addPage(prev) # current page is something new -> save latest old one
	output.addPage(input1.getPage(n-1)) # add last page
	# write output
	fileout = "%s-compact%s" % os.path.splitext(filein)
	outputStream = file(fileout, "wb")
	output.write(outputStream)
	outputStream.close()
	# print some information
	n2 = output.getNumPages()
	print "%s has %s pages." % (filein, n)
	print "%s has %s pages." % (fileout, n2)
	print "-> removed %s pages\n" % (n-n2)


if len(sys.argv) < 2:
	print "Usage: %s <inputfile(s)>" % sys.argv[0]
	sys.exit(2)

for filein in sys.argv[1:]:
	compact(filein)