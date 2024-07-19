import PyPDF2

# Open the PDF file
pdf_file = open('your_file.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF
num_pages = len(pdf_reader.pages)

# Loop through each page and extract text
for page_num in range(num_pages):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()  # Call the method correctly by adding parentheses
    print(f"Page {page_num + 1}:\n{text}\n")

# Close the PDF file
pdf_file.close()



# import pdfplumber

# # Open the PDF file
# with pdfplumber.open('your_file.pdf') as pdf:
#     for page_num, page in enumerate(pdf.pages):
#         text = page.extract_text()
#         if text:  # Check if text is not None
#             print(f"Page {page_num + 1}:\n{text}\n")
#         else:
#             print(f"Page {page_num + 1}:\n(No text found)\n")



# from pdf2image import convert_from_path
# import pytesseract

# # Convert PDF to images
# pages = convert_from_path('your_file.pdf')

# # Extract text from each image
# for page_num, page in enumerate(pages):
#     text = pytesseract.image_to_string(page)
#     print(f"Page {page_num + 1}:\n{text}\n")