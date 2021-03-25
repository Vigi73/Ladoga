import pytesseract
from PIL import Image

img = Image.open('my_screenshot.png')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

answer = pytesseract.image_to_string(img, lang='rus')
print(answer)