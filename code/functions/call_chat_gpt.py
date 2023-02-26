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
        
        idx = np.argmax(similarity)
        sent_dict['type'] = summary[idx]['type']
        if sent_dict['type'] == 'audio':
            sent_dict['start'] = summary[idx]['start']
            sent_dict['sent'] = rf_sent
        elif sent_dict['type'] == 'pdf':
            sent_dict['sent'] = rf_sent
            
        refined_summary.append(sent_dict)

    return refined_summary


'''
# Set up the model and prompt
model_engine = MODEL_ENGINE
prompt = "reorder the sentences in the following paragraph to make it more coherent, but do not change a sentence. [7]The Fourier transform of a Gaussian function is another Gaussian function. [50]This makes it possible to see a connection between the Fourier series and the Fourier transform for periodic functions which have a convergent Fourier series. [27]The functions are often referred to as a Fourier transform pair. [2]The term Fourier transform refers to both this complex-valued function and the mathematical operation. [60]This function was specially chosen to have a real Fourier transform that can be easily plotted. [1]The output of the transform is a complex-valued function of frequency. [56]The following figures provide a visual illustration of how the Fourier transform measures whether a frequency is present in a particular function. [44]In these cases, the value of the Fourier transform at negative frequencies is distinct from the value at real frequencies, and they are important. [13]with a smaller frequency, then sine x plus sine 3x takes the y values of each function at each [21]Then the added functions would look like this. This is already much closer to the square wave, [0]In mathematics, the Fourier transform (FT) is a transform that converts a function into a form that describes the frequencies present in the original function."



prompt = "Modify the following paragraph to make it more coherent, but do not reorder, merge or split the sentences. " + response

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)
'''