from PyPDF2 import PdfReader, PdfWriter
import sys, getopt

if __name__ == '__main__':

    pages_per_sheet = 4
    sheets_per_section = 4
    pdfPath = ""
    outputPath = "./out.pdf"

    for option, arg in getopt.getopt(sys.argv[1:], "hs:i:o:")[0]:
        if option == '-h':
            print("-s Sheets per section. Default is 4. -i input file -o output file")
        elif option == '-s':
            sheets_per_section = int(arg)
        elif option == "-i":
            pdfPath = str(arg)
        elif option == "-o":
            outputPath = str(arg)

    if (pdfPath == ""):
        raise Exception("No input file provided")
    
    pages_per_section = sheets_per_section * pages_per_sheet

    reader = PdfReader(pdfPath)

    length = len(reader.pages)
    num_sections = length // pages_per_section

    writer = PdfWriter()

    for section in range(num_sections):
        section_from = pages_per_section * section
        section_to = pages_per_section * (section + 1) - 1

        for page_offset in range(pages_per_section // 2):
            first_page = section_from + page_offset
            last_page = section_to - page_offset
            if page_offset % 2 == 0:
                first_page, last_page = last_page, first_page

            writer.add_page(reader.pages[first_page])
            writer.add_page(reader.pages[last_page])

        writer.write(outputPath)

    writer.close()
