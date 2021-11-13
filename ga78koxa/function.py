import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
def imshow(X, resize=None):
  pil_image=Image.fromarray(X)
  pil_image_resize = pil_image.resize(resize)
  #pil_image_resize.show()
  return pil_image_resize
