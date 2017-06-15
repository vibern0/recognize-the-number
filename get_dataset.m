load('/home/bernardovieira/Dropbox/Faculdade/3/s2/CR/Enunciado e Ficheiros complementares-20170506/binaryalphadigs.mat')
[h, w] = size(dat);
fileID = fopen('generated_dataset.txt','w');
fprintf(fileID, 'input = [\n');
for a = 1:h
    for b = 1:w
        mn = dat{a, b};
        if(b == 1)
            fprintf(fileID, '\t[\n');
        end
        
        for l = 1:20
            for c = 0:15
                if(l == 1 && c == 0)
                    fprintf(fileID, '\t\t[\n\t\t\t%.1f, ', mn(1));
                elseif(l == 20 && c == 15)
                    if(b == w)
                        fprintf(fileID, '%.1f\n\t\t]\n\t],\n', mn(320));
                    else
                        fprintf(fileID, '%.1f\n\t\t],\n', mn(320));
                    end
                elseif(c == 15)
                    fprintf(fileID, '%.1f,\n\t\t\t', mn(20 * c + l));
                else
                    fprintf(fileID, '%.1f, ', mn(20 * c + l));
                end
            end
        end
    end
end
fprintf(fileID, ']');
fclose(fileID);