from PIL import Image
from pix2tex.cli import LatexOCR

print("Loading LaTeX-OCR model...")
_model = LatexOCR()
print("Model loaded.")

def recognize_from_image(img: Image.Image) -> str:
    """PillowのImageオブジェクトを受け取り、数式認識を実行する"""
    try:
        latex_code = _model(img)
        print(f"Recognized: {latex_code}")
        return latex_code
    except Exception as e:
        print(f"Error during OCR: {e}")
        return "Error: Recognition failed."
