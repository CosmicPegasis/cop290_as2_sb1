import sys
import pytesseract
import fitz
import io
from PIL import Image


def transcribe_pdf(pdf_file):
    pdf = fitz.open(pdf_file)
    text = ""
    for page_count in range(pdf.page_count):
        page = pdf[page_count]
        text += page.get_text()
        image_indices = page.get_images()
        imgs = [pdf.extract_image(image_index[0]) for image_index in image_indices]

        for img in imgs:
            img = Image.open(io.BytesIO(img["image"]))
            text += pytesseract.image_to_string(img)
    return text


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 pdf.py pdf_file.pdf output.txt")
        sys.exit(1)
    else:
        with open(sys.argv[2], "w") as f:
            f.write(transcribe_pdf(sys.argv[1]))
