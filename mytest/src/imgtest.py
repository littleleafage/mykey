import urllib
import StringIO
from PIL import Image
from PIL import ImageEnhance

import os
import time
from selenium import webdriver

im = Image.open("G:\\webdriver\\mytest\\src\\mn.jpeg")
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")






