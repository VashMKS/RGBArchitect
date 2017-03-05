from levelDetector import levelDetector
from PIL import Image

boardcols = 21
boardrows = 17
scale = 6

imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/Level 4.jpg"
imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/Level 4.png"
levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = 21
boardrows = 17
scale = 2

imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/Level 5.jpg"
imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/Level 5.png"
levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = int(730/5)
boardrows = int(300/5)
scale = 1

imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/RNG1.jpg"
imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/RNG1.png"
levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = int(274/4)
boardrows = int(184/4)
scale = 1

#imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/RNG2.jpg"
#imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/RNG2.png"

imageload = "InputImages/RNG2.jpg"
imageoutput = "OutputImages/RNG2.png"

levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = int(274/4)
boardrows = int(184/4)
scale = 1

#imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/RNG2.jpg"
#imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/RNG2.png"

imageload = "InputImages/RNG2.jpg"
imageoutput = "OutputImages/RNG2.png"

levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = 120
boardrows = 90
scale = 1

#imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/Maze1.gif"
#imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/Maze1.png"

imageload = "InputImages/Maze1.gif"
imageoutput = "OutputImages/Maze1.png"

levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = 32
boardrows = 23
scale = 1
#Wincows Path

#imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/RNG3.gif"
#imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/RNG3.png"

#Linux Path
imageload = "InputImages/RNG3.jpg"
imageoutput = "OutputImages/RNG3.png"


levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = 120
boardrows = 90
scale = 1

#Windows Path
#imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/Maze1.gif"
#imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/Maze1.png"

#Linux Path
imageload = "InputImages/Maze1.gif"
imageoutput = "OutputImages/Maze1.png"
#transform gif to jpg

img = Image.open(imageload)
new_im = Image.new("RGB", img.size)
new_im.paste(img)

new_im.save("InputImages/Maze1.jpg")

imageload = "InputImages/Maze1.jpg"

levelDetector(imageload, boardrows, boardcols, scale, imageoutput)
