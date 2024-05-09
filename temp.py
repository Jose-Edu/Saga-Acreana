from PIL import Image, ImageDraw


for c in ('acre', 'amazonense', 'cfc', 'floresta', 'rural', 'silvestre'):
    image = Image.open(f'escudos//180px//{c}.png')
    img = image.resize((50, 50))
    img.save(f'escudos//table6//{c}.png', 'png')