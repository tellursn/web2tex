import subprocess
import time
from pathlib import Path
from PIL import Image
import pyperclip
from scocr import recognize_from_image

def main():
    print("Starting spectacle... Please select a region.")
    subprocess.Popen(["spectacle", "-r", "-b", "-c"])
    print("Waiting for image on clipboard...")
    for i in range(60):  
        time.sleep(0.5)
        print(f"Checking clipboard... ({i+1})")
        try:
            proc = subprocess.run(
                ["wl-paste", "-l"], 
                check=True, capture_output=True, text=True
            )
            mime_types = proc.stdout.splitlines()
            if "image/png" in mime_types:
                print("Image found in clipboard!")
                
                filepath = Path("/tmp/ocr_screenshot.png")
                with open(filepath, "wb") as f:
                    subprocess.run(["wl-paste", "-t", "image/png"], stdout=f, check=True)
                
                img = Image.open(filepath)
                latex_code = recognize_from_image(img)
                
                pyperclip.copy(latex_code)
                print("Success! LaTeX code has been copied to the clipboard.")
                return  

        except (FileNotFoundError, subprocess.CalledProcessError):
            continue

    print("Timeout: Could not find an image on the clipboard within 30 seconds.")

if __name__ == '__main__':
    main()
