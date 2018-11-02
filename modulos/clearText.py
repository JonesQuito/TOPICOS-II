#nltk.download('punkt')
#nltk.download('stopwords')
#nltk.download('rslp') Instala o stemmer português
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
    
    return ' '.join(tokens)
    