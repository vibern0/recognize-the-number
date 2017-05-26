from PIL import Image

col = Image.open("one.jpg")
col = col.resize((26, 28), Image.ANTIALIAS)
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("result_bw.jpg")
pixels = list(bw.getdata())
width, height = bw.size
pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]
pixels = [[1 if pixels[i][g] == 0 else 0 for g in xrange(width)] for i in xrange(height)]

for h in range(0, len(pixels)):
	print(pixels[h])

# test with trained neural network
