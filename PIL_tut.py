from PIL import Image, ImageChops, ImageFilter
from matplotlib import pyplot as plt



image_x = 'jl.jpg'
image_o =  'jl2.jpg'


x = Image.open(image_x)
o = Image.open(image_o)

print(' image size', x.size , 'color mode' , x.mode)
print(' image size', o.size , 'color mode' , o.mode)

plt.subplot(121) , plt.imshow(x)

plt.imshow(x)
plt.axis('off')

plt.subplot(122)
plt.imshow(o)
plt.axis('off')

plt.show()


#merging these two images together
merged = ImageChops.multiply(x,o)
plt.figure()
plt.imshow(merged)
plt.show()

# adding, will only get the common area. like the Intersection in a set.
add = ImageChops.add(x,o)
plt.imshow(add)
plt.show()

# converting color mode, L is for grayscale
greyscale = merged.convert('L')
greyscale.show()

pixel = merged.load()

# white = (255,255,255) , if not white, make it black

for row in range(merged.size[0]):
    for column in range(merged.size[1]):
        if pixel[row, column] !=(255,255,255):
            pixel[row,column] = (0,0,0)

merged.show()

# what if using a greyscale image which is not RGB ? 

for row in range(greyscale.size[0]):
    for column in range(merged.size[1]):
        if pixel[row, column] !=(255,255,255):
            pixel[row,column] = (0,0,0)

greyscale.show()

#inverting the image
invert = ImageChops.invert(greyscale)
# inverting by subtracting

bg = Image.new('L' , (256,256) , color=(255))
subtraction = ImageChops.difference ( bg , greyscale)


#blur
blur = greyscale.filter(ImageFilter.GaussianBlur(radius = 2 ))
blur.show()




invert.show()

# rotaate the image
rotate = subtraction.rotate(45)
rotate.show() 


#edge detection
edge = blur.filter(ImageFilter.FIND_EDGES)
edge.show()
