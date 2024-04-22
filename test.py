import psd_tools as psd_
from PIL import Image
import openpyxl as xl

psd = psd_.PSDImage.open('info_time.psd')
number_layer = list(filter(lambda layer: layer.name == "taça", psd.descendants()))[0]
number_layer.visible = True
image = psd.composite(force=True)
image.save('output.png', 'png')