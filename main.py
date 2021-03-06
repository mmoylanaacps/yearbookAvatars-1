import string
from io import BytesIO
from PIL import Image
import pandas as pd
from avatar_generator import get_png_avatar
import os

#read yearbook and generate images.  change to yearbook test to run for first 10 rows only.
ds = pd.read_csv('students.csv').to_dict('records')
for student in ds:
  text = student['Stfirst'][:1].upper() + student['Stlast'][:1].upper();
  rawIO = BytesIO()
  get_png_avatar(text, rawIO)
  byteImg = Image.open(rawIO)
  filename = student['Stlast'] + ":" + student['Stfirst'] + ":" + str(student['Studentid'])
  #os.remove(filename + ".png")
  byteImg.save("./images/" + str(student['Grade']) + "/" + filename + '.png', 'PNG')
  byteImg.save("./imagessif/" + str(student['Grade']) + "/" + str(student['Studentid']) + '.png', 'PNG')




