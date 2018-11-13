"""
Definindo funções para leitura de arquivos
"""

'''
Recupera todos os arquivos contidos no diretório 'path' definido cujo tipo seja
igual ao especificado no segundo parâmetro 'type_file' 
    @Autor Jones Quito
'''
def getFilesByType(path, type_file):
    import os
    if type_file not in ['txt', 'pjg', 'png']:
        raise Erro("Type file is not valid. try 'txt', 'jpg' or 'png'")
    files = []
    for _, _, arquivo in os.walk(path):
        for nameFile in arquivo:
            if nameFile.endswith('.'+ type_file):
                files.append(nameFile)
    return files



'''
Recupera arquivos e diretórios dentro de um caminho passado como parâmetro 
@Autor Jones Quito
'''
def getAllFiles(path):
    import os
    files = []
    try:
        files = os.listdir(path)
    except:
        print("Arquivo não encontrado")
        return files
    
    return files


'''
Recupera todos os diretórios contidos no diretório 'path' definido. Não recupera subdiretórios
    @Autor Jones Quito
'''
def getDirectories(path, index):
    import os
    
    directories = []
    for _, directory, _ in os.walk(path):
        directories.append(directory)
    return directories[index]



###############################################

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('rslp') #Instala o stemmer português
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import RSLPStemmer

def stemmer(word):
    stemmer = nltk.stem.RSLPStemmer()
    return stemmer.stem(word)


def cleaner(text):
    text = re.sub('[^A-Za-z çáéíóúâôêãõ]', '', text)
    text = re.sub('  ', ' ', text)
    text = text.lower()

    tokenized_text = word_tokenize(text)

    stop_words = stopwords.words('portuguese')
    #stop_words = stopwords.words('english')

    tokens = []
    for palavra in tokenized_text:
        if ((palavra not in stop_words) and (len(palavra)>1)):
            palavra = stemmer(palavra)
            tokens.append(palavra)
    
    return ' '.join(tokens), len(tokenized_text)




