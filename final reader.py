# read text from image
from PIL import Image
import pytesseract
image = Image.open('med1.jpeg')
pytesseract.pytesseract.tesseract_cmd =r"C:\Program Files\Tesseract-OCR\tesseract.exe"
txt = pytesseract.image_to_string(image)
print(txt)
