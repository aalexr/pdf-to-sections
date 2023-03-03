from PyPDF2 import PdfReader, PdfWriter

if __name__ == '__main__':
    pdfPath = 'insert your path here'
    reader = PdfReader(pdfPath)
    writer = PdfWriter()

    # const
    pages_per_sheet = 4
    sheets_per_section = 4
    pages_per_section = sheets_per_section * pages_per_sheet

    length = len(reader.pages)
    num_sections = length // pages_per_section
    for i in range(num_sections):
        section_from = pages_per_section * i
        section_to = pages_per_section * (i + 1) - 1

        for j in range(pages_per_section // 2):
            first_page = section_from + j
            last_page = section_to - j
            if j % 2 == 0:
                [first_page, last_page] = [last_page, first_page]

            writer.add_page(reader.pages[first_page])
            writer.add_page(reader.pages[last_page])

        writer.write('output path here')

    writer.close()
