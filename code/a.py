import nltk
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def clean_raw_text(sent):
    sent = re.sub(r"[^A-Za-z\d ]", "", sent)
    sent = sent.strip()
    sent = sent.replace('- ', '')
    sent = sent.replace('  ', ' ')
    sent = sent.replace('like', '')
    sent = sent.replace('want', '')
    return sent

def preprocessing(sents):
    processed_sents = []
    
    lemmatizer = WordNetLemmatizer()
    wn_stopwords = set(stopwords.words('english'))

    with open("../data/gist_stopwords.txt") as f:
        gist_file = f.read() 
        gist_stopwords = gist_file.split(",")
        f.close()
    
    gist_stopwords=[i.replace('"',"").strip() for i in gist_stopwords]
    
    for i, sent in enumerate(sents):
        raw_text = sent['raw']
        cleaned_raw_text = clean_raw_text(raw_text)
        tokens = nltk.word_tokenize(cleaned_raw_text)
        cleaned_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token not in wn_stopwords and token not in gist_stopwords]
        sent['tokens'] = cleaned_tokens
        processed_sents.append(sent)
    
    return processed_sents

with open("../data/gist_stopwords.txt") as f:
    gist_file = f.read() 
    gist_stopwords = gist_file.split(",")
    f.close()
gist_stopwords=[i.replace('"',"").strip() for i in gist_stopwords]
print(gist_stopwords)



wn_stopwords = stopwords.words('english')
print(wn_stopwords)

lista = ['i', 'am', 'english', 'readily']
print('i' not in gist_stopwords)
print('i' not in wn_stopwords)

stopword_list = gist_stopwords + wn_stopwords


print([a for a in lista if a not in stopword_list])