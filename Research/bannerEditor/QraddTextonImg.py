from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import os


def generateQRCode(url: str, size: int = 80) -> Image.Image:
    """
    Generates a QR code for the given URL.
    
    Args:
        url (str): The URL to encode in the QR code.
        size (int): The size of the QR code (width and height).

    Returns:
        Image.Image: The QR code as a PIL Image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image = qr_image.resize((size, size))
    return qr_image


def placeQRCodeOnImage(imagePath: str, url: str, qrSize: int = 80, margin: int = 20) -> None:
    """
    Places a QR code of a given URL onto an image at a random position (left or right).

    Args:
        imagePath (str): Path to the image file.
        url (str): The URL to encode in the QR code.
        qrSize (int): The size of the QR code (width and height).
        margin (int): The margin around the QR code.
    """
    try:
        # Load the banner image
        img = Image.open(imagePath)
        imgWidth, imgHeight = img.size

        # Generate the QR code
        qrCode = generateQRCode(url, size=qrSize)

        # Determine random position (left or right)
        positionX = margin if random.choice([True, False]) else imgWidth - qrSize - margin
        positionY = margin

        # Ensure QR code does not exceed image dimensions
        if positionX + qrSize > imgWidth or positionY + qrSize > imgHeight:
            raise ValueError("QR code dimensions exceed image dimensions with the given margin.")

        # Paste the QR code onto the banner image
        img.paste(qrCode, (positionX, positionY))

        # Save the updated image
        outputPath = os.path.splitext(imagePath)[0] + "_with_qr.png"
        img.save(outputPath, quality=95)
        print(f"QR code added and image saved to {outputPath}.")

    except Exception as e:
        print(f"Error: {e}")


# Usage
bannerImages = [
    "banners/1.png",
    "banners/2.png",
    "banners/3.png",
    "banners/4.png",
]

for banner in bannerImages:
    placeQRCodeOnImage(banner, "https://level.game/")
