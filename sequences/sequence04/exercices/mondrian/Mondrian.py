from PIL import Image, ImageDraw

image = Image.open("mondrian.jpg")

x, y = image.size
grande_image = Image.new('RGBA', (x, y), (255, 255, 255, 0))
grande_image.paste(image, (0, 0))


def abyme(image, n):
    if n == 1:
        image.show()
    else:
        coeff = 470 / 1005
        x, y = image.size
        x = round(x * coeff)
        y = round(y * coeff)
        image_plus_petite = image.resize((x, y))
        image.paste(image_plus_petite, (145, 155))
        abyme(grande_image, n - 1)


abyme(grande_image, 10)

