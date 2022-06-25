from PIL import ImageDraw


def add_text(image, x=0, y=0, text="simple_text", color="#1C0606"):
    im = ImageDraw.Draw(image)
    im.text(
        (x, y),
        text,
        fill=color
    )
    return image


def paste_img(image, pasting_image, x=0, y=0, text="simple_text", color="#1C0606"):
    image.paste(pasting_image, (x, y))
    return image
