
def setup():
    size(400, 400)
    dogImage = loadImage("dog.jpg")
    image(dogImage, 0, 0)
    loadPixels()
    print(pixels[57])
    c = color(0, 255, 100)
    print(red(pixels[57]),green(pixels[57]), blue(pixels[57]))
    yellow = color(0, 255, 100)
    pixels[57] = c


    updatePixels()
    
