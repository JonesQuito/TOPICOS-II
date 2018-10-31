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