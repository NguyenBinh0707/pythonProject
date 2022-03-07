from PIL import Image
import numpy as np
img = Image.open('test.png')
img.show()
np_img = np.array(img)
print(np_img.shape)
def grayfade():
    newimg = img.convert('L')
    newimg.show()
    newimg.save('test2.png')
grayfade()
def resize():
    print(img.size)
    newimg2 = img.resize((1980,3080))
    newimg2.show()
    newimg2.save('test2.png')
resize()