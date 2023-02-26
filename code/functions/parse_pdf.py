import nltk
from PyPDF2 import PdfReader
import io
from urllib.request import Request, urlopen

def pdf_to_text(object):
      # creating a pdf reader object
      remote_file = urlopen(Request(object['url'])).read()
      memory_file = io.BytesIO(remote_file)
      reader = PdfReader(memory_file)
      
      # getting a specific page from the pdf file
      text = ""
      for i in range(len(reader.pages)):
            # res+=reader.pages[i]
            text+=reader.pages[i].extract_text()
            text+="[PAGE]"
      
      # extracting text from page
      # text = page.extract_text()
      text = text.replace("\n"," ")
      
      processed_text = parse_text(text, object)
      
      return processed_text
      

def parse_text(text, object):    
    pages = text.split("[PAGE]")
    
    processed_sents = []
    
    for i, page in enumerate(pages):
          sents = nltk.sent_tokenize(page)
          
          for j, sent in enumerate(sents):
                sent_dict = {}
                sent_dict['type'] = object['type']
                sent_dict['raw'] = sent
                sent_dict['page'] = i
                sent_dict['id'] = object['id']
                sent_dict['url'] = object['url']
                
                processed_sents.append(sent_dict)
    
    return processed_sents