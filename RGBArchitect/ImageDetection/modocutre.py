from PIL import Image
from numpy import *
import operator

foto = Image.open("hackmap.jpg")
foto = foto.resize((int(foto.size[0]/2),int(foto.size[1]/2)))
matrix = array(foto)
print(foto.size)
print(matrix.shape)
anchototal = foto.size[0]
altototal = foto.size[1]

#Si, hemos contado cuadraditos
cuadraditoshorizontales = 21
cuadraditosverticales = 17

cuadraditosize = int(anchototal/cuadraditoshorizontales)


def keywithmaxval(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

white = [255,255,255]
red = [255,0,0]
green = [0,255,0]
blue =[0,0,255]
black = [0,0,0]
pink =[255,0,255]
yellow = [255,255,0]
cyan = [0,255,255]

colors = (white, red, green, blue, black, pink, yellow, cyan)
colornames = ("white", "red", "green", "blue", "black", "pink", "yellow", "cyan")

def getColorbyName(colorName):
    for c in range(0,len(colornames)):
        if(colorName == colornames[c]):
            return colors[c]


def calculaPixel(i,j):
    xreal = i*cuadraditosize
    yreal = j*cuadraditosize

    totalScore = {'white' : 0, 'red' : 0, 'green': 0, 'blue':0, 'black':0, 'pink':0, 'yellow':0, 'cyan':0}
    for x in range(0,cuadraditosize):
        for y in range(0,cuadraditosize):
            if(xreal + x < anchototal and yreal + y < altototal):
                color = matrix[yreal + y,xreal + x]

                fitcolor = white
                fitcolorn = colornames[0]
                for c in range(0, len(colors)):
                    if linalg.norm(colors[c] - color) < linalg.norm(fitcolor - color):
                        fitcolor = colors[c]
                        fitcolorn = colornames[c]

                totalScore[fitcolorn] +=1
                #el mayor de totalscore sera el color elegido para la region
                definitivePixelColorName = keywithmaxval(totalScore)
                definitiveColor = getColorbyName(definitivePixelColorName)
                return definitiveColor


salida = Image.new('RGBA', (cuadraditoshorizontales,cuadraditosverticales),'white') # create a new black image
pixels = salida.load() # create the pixel map

for i in range(0,cuadraditoshorizontales):
    for j in range(0,cuadraditosverticales):
        pixelcolor = calculaPixel(i,j)
        pixels[i,j]= tuple(pixelcolor)
pixels[0,0] = tuple(white)
pixels[0,16] = tuple(white)
salida.save('chachi.png')