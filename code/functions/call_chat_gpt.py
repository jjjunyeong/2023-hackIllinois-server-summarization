import openai
import nltk
import re
from config import *
from functions.get_summary import get_word_overlap_similarity
import numpy as np

# Set up the OpenAI API client
openai.api_key = OPENAI_API_KEY

def paraphrase(summary):
    prompt_summary = " ".join([sent['raw'] for sent in summary])
    
    prompt = "Paraphrase the paragraph to make it more cohesive and reasonable. " + prompt_summary
    
    # Generate a response
    completion = openai.Completion.create(
        engine=MODEL_ENGINE,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    
    refined_sents = nltk.sent_tokenize(response)
    
    refined_summary = []
    
    for rf_sent in refined_sents:
        sent_dict = {}
        similarity = []
        
        for org_sent in summary:
            sim = get_word_overlap_similarity(nltk.word_tokenize(rf_sent), nltk.word_tokenize(org_sent['raw']))
            similarity.append(sim)
        
        # if similarity is empty 
        idx = np.argmax(similarity)
        sent_dict['type'] = summary[idx]['type']
        if sent_dict['type'] == 'video':
            sent_dict['start'] = summary[idx]['start']
            sent_dict['summ'] = rf_sent
        elif sent_dict['type'] == 'pdf':
            sent_dict['summ'] = rf_sent
            
        refined_summary.append(sent_dict)

    return refined_summary