import nltk

def parse_pdf(doc):    
    pages = doc.split("page")
    
    processed_sents = []
    
    for i, page in enumerate(pages):
          sents = nltk.sent_tokenize(doc)
          
          for j, sent in enumerate(sents):
                sent_dict = {}
                sent_dict['type'] = 'pdf'
                sent_dict['raw'] = sent
                sent_dict['page'] = i
                
                processed_sents.append(sent_dict)
    
    return processed_sents