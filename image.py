from PIL import Image, ImageFilter
before = Image.open("link.png")
after = before.filter(ImageFilter.BoxBlur(10))
after.save("out.png")
