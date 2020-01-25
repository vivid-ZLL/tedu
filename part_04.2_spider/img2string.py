from PIL import Image
import matplotlib.pyplot as plt
import pytesseract

img = Image.open("1.jpg")
img_L = img.convert("L")

threshold = 120
table = []

for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

img2 = img_L.point(table,'1')
plt.imshow(img2)
plt.show()

res = pytesseract.image_to_string(img2)
print(res)
