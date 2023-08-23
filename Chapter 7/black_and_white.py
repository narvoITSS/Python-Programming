from images import Image

def blackAndWhite(image):
    """Converts the argument image to black and white."""
    blackPixel = (0,0,0)
    whitePixel = (255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            average = (r + g + b) // 3
            if average < 128:
                image.setPixel(x,y,blackPixel)
            else:
                image.setPixel(x,y,whitePixel)
    image.draw()

def grayScale(image):
    """Converts the argument image to grayscale"""
    blackPixel = (0,0,0)
    whitePixel = (255,255,255)
    for y in range(image.getHeight()):
        for x in range(image.getWidth()):
            (r,g,b) = image.getPixel(x,y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            image.setPixel(x,y,(lum,lum,lum))
    image.draw()

def main():
    image = Image("./smokey.gif")
    image2 = image.clone()
    blackAndWhite(image)
    grayScale(image2)

if __name__ == "__main__":
    main()
