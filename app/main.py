# Download and install Tesseract OCR from
# https://github.com/UB-Mannheim/tesseract/wiki

# Import required libraries
from PIL import Image 
from pytesseract import pytesseract
from config import myConfig

# Define path to tesseract executable
path_to_tsrct = r'C:/Tesseract-OCR/tesseract'

# Set path to tesseractOCR
pytesseract.tesseract_cmd = path_to_tsrct

# Set image path
img_path = './images/sampleOne.jpg'

# Open image
img = Image.open(img_path)

# Extract text from image
text = pytesseract.image_to_string(Image.open(img_path), config=myConfig)


print(text)