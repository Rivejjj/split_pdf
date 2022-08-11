import sys
import os 

try:
	from pdfrw import PdfReader, PdfWriter, PageMerge
except:
	os.system("pip install pdfrw")
	from pdfrw import PdfReader, PdfWriter, PageMerge


def splitpage(file):
	page = PageMerge()

	for x_pos in (0,0.5):
		page.add(file, viewrect=(x_pos, 0, 0.5,1))
		yield page.render()


def main():
	#file = "pasajes.pdf"
	file = sys.argv[1]

	writer = PdfWriter()
	for page in PdfReader(file).pages:
	    writer.addpages(splitpage(page))

	with open("nuevo.pdf","wb") as nuevo:
		writer.write(nuevo)

main()