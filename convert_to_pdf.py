from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

# convert images to pdf
def convert_to_pdf(image_files):
    pdf_file = "output.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    image_folder = "pages"

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        c.drawImage(image_path, 0, 0, letter[0], letter[1])
        c.showPage()

    c.save()