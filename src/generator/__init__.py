from PIL import Image
import numpy as np

nomes_ficheiro = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ca',
    'cb',
    'cc',
    'cd',
    'ce',
    'cf',
    'cg',
    'ch',
    'ci',
    'cj',
    'ck',
    'cl',
    'cm',
    'cn',
    'co',
    'cp',
    'cq',
    'cr',
    'cs',
    'ct',
    'cu',
    'cv',
    'cw',
    'cx',
    'cy',
    'cz'
]
nomes_variavel = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

class Dataset_Generator:
    def __init__(self):
         # open image
        image = Image.open("generator/binaryalphadigs.jpg")
        
        num_glyphs_per_line=39;
        num_lines_in_base_image=36;

        fullwidth, fullheight = image.size
        singlewidth= int(fullwidth/num_glyphs_per_line)
        singleheight = int(fullheight/num_lines_in_base_image)
        
        for image_line in range(0, num_lines_in_base_image): # indice 0 a 35
            with open('./generator/tmp/'+nomes_ficheiro[image_line]+'.py',"w") as f:
                f.write('input_'+nomes_variavel[image_line]+' = [\n')
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
                    #pixels2 = [[' ' if pixels[i][g] == 0 else '@' for g in range(width)] for i in range(height)]
                    
                    # write information to a file
                    f.write(np.array2string(np.reshape(pixels,(16, 20)), separator=',', max_line_width=120)) 
                    if glyph < num_glyphs_per_line-1:
                        f.write('\n,\n')   
                # fechar o array            
                f.write(']\n\n')
                #escrever variavel de output
                f.write('output_'+nomes_variavel[image_line]+' = [\n')
                for i in range(0,40):
                    f.write(np.array2string(self.convert_int_to_binaryArray(image_line), separator=','))
                    if i < 39:
                        f.write(',\n') 
                f.write(']\n\n')        
                    

    def convert_int_to_binaryArray(self,number_to_convert):
        output= np.zeros(6)
        weight =32;

        for i in range(0,6):
            output[i]=int(number_to_convert/weight)
            if output[i] == 1:
                number_to_convert=number_to_convert-weight
            weight=weight/2
        return output

    def __del__(self):
        pass
