from PIL import Image

class Dataset_Generator:
    def __init__(self):
         # open image
        image = Image.open("generator/binaryalphadigs.jpg")
        
        num_glyphs_per_line=39;
        num_lines_in_base_image=36;

        fullwidth, fullheight = image.size
        singlewidth= int(fullwidth/num_glyphs_per_line)
        singleheight = int(fullheight/num_lines_in_base_image)

        for image_line in range(0, num_lines_in_base_image):
            for glyph in range(0, num_glyphs_per_line):
                absX= glyph*singlewidth
                absY=glyph*singleheight
                
                #Saca imagem individual do mapa grande
                new_image=image.crop((absX,absY,singlewidth,singleheight))
                #Redimensiona imagem individual para 20 * 16
                new_image= new_image.resize((20, 16), Image.ANTIALIAS)

                # make it black and white
                gray = new_image.convert('L')
                bw = gray.point(lambda x: 1 if x < 128 else 255, '1')

                # get transformed data
                pixels = list(bw.getdata())
                width, height = bw.size

                # make a matrix
                pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]

                # update values
                pixels = [[1. if pixels[i][g] == 0 else 0. for g in range(width)] for i in range(height)]
                pixels2 = [[' ' if pixels[i][g] == 0 else '@' for g in range(width)] for i in range(height)]
                
                print('Matriz Resultado:')
                
                for h in range(0, len(pixels)):
                    print(pixels[h])

                print('Matriz visual:')
                    
                for h in range(0, len(pixels2)):
                    print(pixels2[h])

        # test with trained neural network

    def __del__(self):
        pass
