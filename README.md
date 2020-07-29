# RGBArchitect
HackUPC 2017 Winter Demo

RGB Architect is a tool to generate playable levels of a simple 2D platformer game from any image (e.g. a sketch in a notebook). Please bear in mind that this has been the result of 36h hours of rush coding at a hackathon by two math degree students when you think about the (multiple) flaws the project has.

RGBArch makes level design, prototyping and testing fast and easy. How? The first part of the project uses Unity scripts to import a fully playable level in seconds from a small image. It does so by identifying the RGB values of the pixels and matching them with a game object in the Unity project. At runtime, it spawns the correct prefabs (units, terrain, sprites and game objects in general) at the right coordinates making the "level map" playable in seconds. This is essentially a way to store/compress the whole level layout in a very small image. The second part of the project is what maks it interesting: we crafted a simple Python computer vision algorithm that takes a picture, any picture, and translates it into a small PNG image that can be interpreted by the architect. This allows you to **sketch a level on a piece of paper, take a picture, upload it, and play and start playing right away!**

## Level Loader

Currently we use 8 different colors for 8 different prefabs, the colors being as separated as possible from each other (consider RGB colors as 3D vectors with a byte worth of info in each coordinate) in the RGB space. Those are: 

Black	[0,0,0]		simple terrain prefab  
Red	[255,0,0]	simple enemy mob (no AI yet, it's a snail)  
Green	[0,255,0]	player spawn  
Blue	[0,0,255]	object boxes (currently decoration)  
Yellow	[255,255,0]	coin  
Magenta	[255,0,255]	goal/end of level  
Cyan	[0,255,255]	coin (placeholder)  
White	[255,255,255]	empty space/background  

The Unity LevelLoader class will interpret any png image including only the above colors and start a new game right away. The fun part is that you can throw *anything* at it, making room for some awesome trickery (see the [assets](https://github.com/VashMKS/RGBArchitect/tree/master/RGBArchitect/Assets/StreamingAssets) like the Skyline of Barcelona, Minnessota and NY ploted onto the Game View or toy with images that were not intended as level maps like the RNG pack). Also, if you're into that kind of stuff you can choose to design your levels pixel by pixel using any image edition software such as Photoshop, GIMP or MSPaint and go much deeper into level generation and design by making your own prefabs or using slightly different values of RGB for a wider variety of prefabs (for instance, use pure Red[255,0,0] for the base version of an enemy AI and [255,0,x] for as many slightly different variations of it!). Or simply turn your favourite pixel art into a playable level!

We would like to give huge shoutouts to [quill18](https://www.youtube.com/channel/UCbx1TZgxfIauUZyPuBzEwZg) for his Unity tutorials and being the source of some of the free assets and code snippets we used when starting with this.

## Image Recognition

The reason we want our colors as different as possible is so the second part of this project works better. You'll notice a folder named ImageDetection containing a bunch of python scripts and input/output folders. The ultimate goal of this project is to create a Computer Vision algorithm that takes pictures of handwritten sketches for levels and outputs a readable png image that our Unity interpreter can instantly make into a playable 2D Scene!

Current version of the CV algorithm assumes a bunch of limitations and restrictions from the pictures it takes, such as knowing from beforehand the width and height of the target png image and very low to no inclination of the pictures. Both of those restrictions can very easily be taken out, we just didn't have the time for them at the hackathon.

Looking at future versions, we could use some reference points on the corners (like in QR codes) of the sketches so we can try making it more flexible and fix things like paper bending and weird camera angles.

And that's it! Thanks for going all the way to the bottom of this document, hope you enjoy RBG Architect as much as we did building it!

Raquel L. Pérez Arnal ([RaquelLeandra](https://github.com/RaquelLeandra) on GitHub)

Dídac Fernández Cadenas ([VashMKS](https://github.com/VashMKS) on GitHub)
