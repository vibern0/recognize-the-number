from PIL import Image

# open image
col = Image.open("one.jpg")

# resize image
col = col.resize((20, 16), Image.ANTIALIAS)

# make it black and white
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')

# get transformed data
pixels = list(bw.getdata())
width, height = bw.size

# make a matrix
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

# update values
pixels = [[1. if pixels[i][g] == 0 else 0. for g in xrange(width)] for i in xrange(height)]

for h in range(0, len(pixels)):
	print(pixels[h])

# test with trained neural network
