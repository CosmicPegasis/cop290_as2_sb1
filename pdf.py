import pypdf
import sys
import pytesseract
import pdf2image


def transcribe_pdf(pdf_file):
    pdf = pypdf.PdfReader(open(pdf_file, "rb"))
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text


def transcribe_pdf_ocr(pdf_file):

    # Simple image to string
    # print(pytesseract.image_to_string(Image.open("test.png")))

    # convert pdf_file to image then use pytesseract to extract text
    num_pages = len(pypdf.PdfReader(open(pdf_file, "rb")).pages)
    pages = pdf2image.convert_from_path(
        pdf_file, num_pages, fmt="jpeg", size=(1080, None)
    )
    text = ""
    for page in pages:
        text += pytesseract.image_to_string(page)
    return text


if __name__ == "__main__":
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print(
            "Usage: python3 pdf.py pdf_file.pdf output.txt or python3 pdf.py pdf_file.pdf output.txt --ocr"
        )
        sys.exit(1)

    if len(sys.argv) == 4:
        if sys.argv[3] != "--ocr":
            print(
                "Usage: python3 pdf.py pdf_file.pdf output.txt or python3 pdf.py pdf_file.pdf output.txt --ocr"
            )
            sys.exit(1)
        with open(sys.argv[2], "w") as f:
            f.write(transcribe_pdf_ocr(sys.argv[1]))

    else:
        with open(sys.argv[2], "w") as f:
            f.write(transcribe_pdf(sys.argv[1]))
