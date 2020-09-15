import base64
import io

import pdf2image
from PIL import Image


def piltobase64(pil_image):
    stream = io.BytesIO()
    pil_image.save(stream, format="PNG")
    return base64.b64encode(stream.getvalue()).decode('utf-8')


def pdftobase64(pdf_file, width, height):
    """
    Return base64 image string image from a PDF file to be used in HTML code
    :param pdf_file_name: PDF file name
    :param width: Final image width
    :param height: Final image height
    :return: base64 image string
    """
    pil_images = pdf2image.convert_from_path(pdf_file, dpi=300,
                                             output_folder=None, first_page=None,
                                             last_page=None, fmt='PNG', thread_count=1,
                                             userpw=None, use_cropbox=False, strict=False)
    pil_image = pil_images[0].resize((width, height), Image.ANTIALIAS)
    return piltobase64(pil_image)
