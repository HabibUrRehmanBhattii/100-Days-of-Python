import os
from tkinter import filedialog, Tk
from PIL import Image

def resize_image(image_path, width, height):
    with Image.open(image_path) as img:
        img = img.resize((width, height), Image.ANTIALIAS)
        return img

def create_passport_sheet(images, sheet_size, margin):
    sheet = Image.new("RGB", sheet_size, (255, 255, 255))
    x, y = margin
    for img in images:
        sheet.paste(img, (x, y))
        x += img.width + margin[0]
        if x + img.width + margin[0] > sheet_size[0]:
            x = margin[0]
            y += img.height + margin[1]
    return sheet

def main(image_paths, passport_size, sheet_size, margin, output_path):
    passport_images = [resize_image(image_path, *passport_size) for image_path in image_paths]
    passport_sheet = create_passport_sheet(passport_images, sheet_size, margin)
    passport_sheet.save(output_path)

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    filepaths = filedialog.askopenfilenames(title="Select Images",
                                            filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    root.destroy()
    images = [Image.open(filepath) for filepath in filepaths]
    passport_size = (105, 148)
    sheet_size = (297, 210)
    margin = (5, 5)
    output_path = os.path.join(os.path.dirname(filepaths[0]), "passport_sheet.jpg")
    main(filepaths, passport_size, sheet_size, margin, output_path)

# Path: 3_Day\Repeat\test.py