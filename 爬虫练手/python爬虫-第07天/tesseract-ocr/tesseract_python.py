#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image
import pytesseract

#image_data = Image.open("english.jpg")
image_data = Image.open("排序算法.png")

text = pytesseract.image_to_string(image_data, lang="chi_sim")

print(text)
