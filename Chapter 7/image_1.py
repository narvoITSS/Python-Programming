from images import Image
# Absolute File Path
image = Image("/home/leninade/Dropbox/DCCCD Course Work/Spring 2023/Python Programming/Chapter 7/smokey.gif")
#image.draw()

# Relative File Path
image2 = Image("./smokey.gif")
image2.draw()
print(image2)
