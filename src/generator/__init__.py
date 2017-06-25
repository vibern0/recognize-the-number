from PIL import Image
import numpy as np

class Dataset_Generator:
    def __init__(self):
         # open image
        image = Image.open("generator/binaryalphadigs.jpg")
        
        num_glyphs_per_line=39;
        num_lines_in_base_image=36;

        fullwidth, fullheight = image.size
        singlewidth= int(fullwidth/num_glyphs_per_line)
        singleheight = int(fullheight/num_lines_in_base_image)
        
        with open('./generator/tmp/matrizes.txt',"w") as f:
            for image_line in range(0, num_lines_in_base_image): # indice 0 a 35
                for glyph in range(0, num_glyphs_per_line): # indice 0 a 38
                    # calcular a coordenada x e y da glyph atual relativo á origem da imagem principal
                    absX = glyph*singlewidth
                    absY = image_line*singleheight
                    
                    #Saca imagem individual do mapa grande
                    new_image = image.crop((absX, absY, absX+singlewidth, absY+singleheight))
                    #new_image.save('./generator/tmp/char_'+str(image_line)+ '_'+str(glyph)+'.jpg')

                    #Redimensiona imagem individual para 20 * 16
                    new_image = new_image.resize((20, 16), Image.ANTIALIAS)

                    # make it black and white
                    gray = new_image.convert('L')
                    #gray.save('./generator/tmp/grey_'+str(image_line)+ '_'+str(glyph)+'.jpg')
                    bw = gray.point(lambda x: 0 if x < 128 else 255, '1')
                    #bw.save('./generator/tmp/bw_'+str(image_line)+ '_'+str(glyph)+'.jpg')

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

                    # write information to a file
                    f.write("Glyph["+str(image_line)+ ']['+str(glyph)+"] = \n")
                    f.write(np.array2string(np.reshape(pixels,(16, 20)), separator=', ', max_line_width=120)) 
                    f.write('\n\n')                

    def __del__(self):
        pass
