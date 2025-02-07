import os
import glob
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

IMAGE_EXTENSIONS = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.tiff', '*.webp')

image_files = []
for ext in IMAGE_EXTENSIONS:
    image_files.extend(glob.glob(ext))

image_files.sort()

with open('ocr_results.txt', 'w', encoding='utf-8') as results_file:
    for img_file in image_files:
        try:
            with Image.open(img_file) as img:
                text = pytesseract.image_to_string(img)
                clean_text = text.replace('\n', ' ').replace('\r', ' ').strip()
                results_file.write(f"{clean_text} | {os.path.basename(img_file)}\n")
            print(f"Processed: {img_file}")
        except Exception as e:
            print(f"Error processing {img_file}: {str(e)}")

print("OCR processing complete. Results saved to ocr_results.txt")