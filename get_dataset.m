load('/home/bernardovieira/Dropbox/Faculdade/3/s2/CR/Enunciado e Ficheiros complementares-20170506/binaryalphadigs.mat')
[w, h] = size(dat);
fileID = fopen('generated_dataset.txt','w');
fprintf(fileID, 'input = [\n');
for a = 1:w
    for b = 1:h
        mn = dat{a, b};
        fprintf(fileID, '\t[\n\t\t%.1f, ', mn(1));
        for n = 2:319
            if(mod(n, 16) == 0)
                fprintf(fileID, '%.1f\n\t\t', mn(n));
            else
                fprintf(fileID, '%.1f, ', mn(n));
            end
        end
        fprintf(fileID, '%.1f\n\t],\n', mn(320));
    end
end
fprintf(fileID, ']');
fclose(fileID);