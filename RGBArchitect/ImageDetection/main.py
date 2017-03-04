from levelDetector import levelDetector

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

imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/RNG2.jpg"
imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/RNG2.png"
levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = int(274/4)
boardrows = int(184/4)
scale = 1

imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/RNG2.jpg"
imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/RNG2.png"
levelDetector(imageload, boardrows, boardcols, scale, imageoutput)


boardcols = 120
boardrows = 90
scale = 1

imageload = "C:/Unity/Projects/RGBArchitect/ImageDetection/InputImages/Maze1.gif"
imageoutput = "C:/Unity/Projects/RGBArchitect/ImageDetection/OutputImages/Maze1.png"
levelDetector(imageload, boardrows, boardcols, scale, imageoutput)
