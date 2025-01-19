from PIL import Image, ImageDraw, ImageFont
import random
import os
from typing import List

def oldplaceTextOnImage(imagePath: str, text: str, fontSize: int = 60) -> None:
    try:
        # Load the image
        img = Image.open(imagePath)
        draw = ImageDraw.Draw(img)

        # Specify the folder containing fonts
        fontFolder = "fonts"

        # Get a list of all .ttf files in the folder
        fontList: List[str] = [
            os.path.join(fontFolder, fontFile) 
            for fontFile in os.listdir(fontFolder) 
            if fontFile.endswith(".ttf")
        ]

        if not fontList:
            raise FileNotFoundError(f"No .ttf fonts found in the folder: {fontFolder}")

        # Select a random font
        randomFont = random.choice(fontList)

        # Load the font
        try:
            font = ImageFont.truetype(randomFont, fontSize)
        except IOError:
            print(f"Font '{randomFont}' not found or invalid. Using default font.")
            font = ImageFont.load_default()

        # Get text size
        textWidth, textHeight = draw.textsize(text, font=font)

        # Calculate position for centered text
        imgWidth, imgHeight = img.size
        position = ((imgWidth - textWidth) // 2, (imgHeight - textHeight) // 2)

        # Draw text
        draw.text(position, text, fill="black", font=font)
        
        imagePathClean = imagePath.replace("\\", "_")
        imagePathClean = imagePathClean.replace(".png", "")
        imagePathClean = imagePathClean.replace(".jpg", "")

        # Save the updated image with the same quality
        outputPath = f"{imagePathClean}.png"
        img.save(outputPath, quality=95)  # Quality set to 95 (close to the original)
        print(f"Text added and image saved to {outputPath} with original quality.")

    except Exception as e:
        print(f"Error: {e}")



def placeTextOnImage(imagePath: str, text: str, cts: str, fontSize: int = 20) -> None:
    """
    Places two lines of text over an image. The first line (text) is centered horizontally and vertically.
    The second line (cts) is placed below the first line, at half the font size, with a 10-pixel gap.
    The image size and quality are preserved.

    Args:
        imagePath (str): Path to the image file.
        text (str): The main text to place on the image.
        cts (str): The secondary text to place below the main text.
        fontSize (int): The font size of the main text.
    """
    try:
        # Load the image
        img = Image.open(imagePath)
        draw = ImageDraw.Draw(img)

        # Specify the folder containing fonts
        fontFolder = "fonts"

        # Get a list of all .ttf files in the folder
        fontList: List[str] = [
            os.path.join(fontFolder, fontFile)
            for fontFile in os.listdir(fontFolder)
            if fontFile.endswith(".ttf")
        ]

        if not fontList:
            raise FileNotFoundError(f"No .ttf fonts found in the folder: {fontFolder}")

        # Select a random font
        randomFont = random.choice(fontList)

        # Load the fonts
        try:
            mainFont = ImageFont.truetype(randomFont, fontSize)
            ctsFont = ImageFont.truetype(randomFont, fontSize // 2)  # Half the font size for cts
        except IOError:
            print(f"Font '{randomFont}' not found or invalid. Using default font.")
            mainFont = ImageFont.load_default()
            ctsFont = ImageFont.load_default()

        # Get text size for the main text
        textWidth, textHeight = draw.textsize(text, font=mainFont)

        # Calculate position for centered main text
        imgWidth, imgHeight = img.size
        mainTextPosition = ((imgWidth - textWidth) // 2, (imgHeight - textHeight) // 2)

        # Draw the main text
        draw.text(mainTextPosition, text, fill="black", font=mainFont)

        # Get text size for the secondary text
        ctsWidth, ctsHeight = draw.textsize(cts, font=ctsFont)

        # Calculate position for the secondary text (10 pixels below the main text)
        ctsPosition = ((imgWidth - ctsWidth) // 2, mainTextPosition[1] + textHeight + 10)

        # Draw the secondary text
        draw.text(ctsPosition, cts, fill="black", font=ctsFont)

        # Prepare a clean output path
        imagePathClean = imagePath.replace("\\", "_").replace(".png", "").replace(".jpg", "")
        outputPath = f"{imagePathClean}_updated.png"

        # Save the updated image with the same quality
        img.save(outputPath, quality=95)  # Quality set to 95 (close to the original)
        print(f"Text added and image saved to {outputPath} with original quality.")

    except Exception as e:
        print(f"Error: {e}")
# Usage
# placeTextOnImage("banners\\1.png", "Calm, Heal, Happy")

title = "Feeling overwhelmed at work? Find calm amidst the chaos with just a few minutes a day"
cta = "Start your free trial today"
placeTextOnImage("banners\\1.png", title, cta)
placeTextOnImage("banners\\2.png", title, cta)
placeTextOnImage("banners\\3.png", title, cta)
placeTextOnImage("banners\\4.png", title, cta)
