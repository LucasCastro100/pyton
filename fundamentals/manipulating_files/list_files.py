import glob, os, zipfile 

#glob - Expansão de padrão de caminho de estilo Unix
#os - Interfaces de sistemas operacionais diversos
#zipfile - Trabalhar com arquivos ZIP

# Diretorio de trabalho
os.getcwd()

# Listar todos os arquivos de um diretório
for file in glob.glob("fundamentals/manipulating_files/dados/*"): # para bsucar um tipo de arquivo específico, basta adicionar a extensão *.extensão
    print(file)
    
#Compactar arquivos em um diretório
with zipfile .ZipFile("fundamentals/manipulating_files/dados.zip", "w") as zip:
    for file in glob.glob("fundamentals/manipulating_files/dados/*"):
        zip.write(file, os.path.basename(file)) # para compactararquivos em um diretório específico, basta adicionar o caminho do diretório na função glob.glob("caminho/do/diretório/*") *.extensão
        
        