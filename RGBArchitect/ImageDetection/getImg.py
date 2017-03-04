from PIL import Image
from numpy import *



def modify(matrix):
    transformedmatrix = matrix

    for i in range(matrix.shape[0]):  # for every pixel:
        for j in range(matrix.shape[1]):
            pixel = matrix[i][j]
            pixel = define(pixel)
            transformedmatrix[i, j,0] = int(pixel[0])
            transformedmatrix[i, j, 1] = int(pixel[1])
            transformedmatrix[i, j, 2] = int(pixel[2])
    return transformedmatrix


def define(pixel):
    white = [255,255,255]
    red = [255,0,0]
    green = [0,255,0]
    blue =[0,0,255]
    black = [0,0,0]
    pink =[255,0,255]
    yellow = [255,255,0]
    cyan = [0,255,255]

    colors = (white, red, green, blue, black, pink, yellow, cyan)
    res = white
    for color in colors:
        aux =linalg.norm(color - pixel)**2
        if linalg.norm(res - pixel)**2 > aux:
            res = color

    return res



foto = Image.open("perf.png")

#Si, hemos contado cuadraditos
ancho = 21
alto = 17

foto = foto.resize((int(foto.size[0]/6),int(foto.size[1]/6)))

foto.show()
print(foto.format, foto.size, foto.mode)

xsize, ysize = foto.size

matrix = array(foto)


print(matrix.shape)

transformedmatrix = modify(matrix)

print("transformed")

img = Image.new('RGB', foto.size, "black") # create a new black image
pixels = img.load() # create the pixel map
#print(pixels)
print(transformedmatrix.shape)



for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        v = (0,0,0)
        v = tuple(transformedmatrix[j,i])
        pixels[i, j] = v


img.show()

