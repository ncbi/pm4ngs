from PIL import Image
from pm4ngs.jupyterngsplugin.image.pdftobase64 import piltobase64


def imagetobase64(png_file, width, height):
    """
    Return base64 image string image from a PDF file to be used in HTML code
    :param png_file_name: PNG file name
    :param width: Final image width
    :param height: Final image height
    :return: base64 image string
    """
    pil_image = Image.open(png_file)
    pil_image = pil_image.resize((width, height), Image.ANTIALIAS)
    return piltobase64(pil_image)
