from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

pdf_file = "output.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)

image_folder = "pages"

image_files = ("page1.png", "page2.png", "page3.png", "page4.png", "page5.png")

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)
    c.drawImage(image_path, 0, 0, letter[0], letter[1])
    c.showPage()

c.save()