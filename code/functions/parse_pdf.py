import nltk

def parse_pdf(pdf_file_path):
    
    with open(pdf_file_path) as f:
        doc = f.read()
        f.close()
    
    sents = nltk.sent_tokenize(doc)
      
    processed_sents = []
    for i, sent in enumerate(sents):
      sent_dict = {}
      cleaned_sent = sent
      sent_dict['type'] = 'pdf'
      sent_dict['raw'] = sent
      sent_dict['id'] = i

      processed_sents.append(sent_dict)
    
    return processed_sents