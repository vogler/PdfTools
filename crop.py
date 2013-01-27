from pyPdf import PdfFileWriter, PdfFileReader, generic
import sys, os

def crop(filein):
	output = PdfFileWriter()
	input1 = PdfFileReader(file(filein, "rb"))
	input2 = PdfFileReader(file(filein, "rb"))
	# print the title of the document
	print "title = %s" % (input1.getDocumentInfo().title)
	n = input1.getNumPages()
	# loop over pages
	for i in range(n):
		# p = input1.getPage(i)
		# print p.cropBox
		# p.mediaBox.upperRight = (
		# 	p.mediaBox.getUpperRight_x() / 2,
		# 	p.mediaBox.getUpperRight_y() / 2
		# )
		w, h = 359, 269
		slide1 = input1.getPage(i)
		rect = lambda x, y: generic.RectangleObject([x, y, x+w, y+h])
		slide1.mediaBox = rect(117, 462)
		output.addPage(slide1)
		slide2 = input2.getPage(i)
		slide2.mediaBox = rect(117, 111)
		output.addPage(slide2)
	# write output
	fileout = "%s-cropped%s" % os.path.splitext(filein)
	outputStream = file(fileout, "wb")
	output.write(outputStream)
	outputStream.close()
	# print some information
	n2 = output.getNumPages()
	print "%s has %s pages." % (filein, n)
	print "%s has %s pages." % (fileout, n2)

if len(sys.argv) < 2:
	print "Usage: %s <inputfile(s)>" % sys.argv[0]
	sys.exit(2)

for filein in sys.argv[1:]:
	crop(filein)