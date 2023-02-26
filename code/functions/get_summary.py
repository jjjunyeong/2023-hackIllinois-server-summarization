from config import *
import nltk
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import networkx as nx
# import gensim.downloader as gensim

def get_word_overlap_similarity(sent1, sent2):
    overlapped_words = list(set(sent1).intersection(set(sent2)))
    return len(overlapped_words) / (len(sent1) + len(sent2))

def create_word_corpus(document):
    word_corpus = []
    for sent in document:
        for word in sent['tokens']:
            word_corpus.append(word)
            
    return list(set(word_corpus))

def sent_to_vec(word_corpus, sent):
    vec = []
    for word in word_corpus:
        if word in sent:
            vec.append(1)
        else:
            vec.append(0)
    return vec


def get_cosine_similarity(word_corpus, sent1, sent2):
    vec1 = np.array(sent_to_vec(word_corpus, sent1))
    vec2 = np.array(sent_to_vec(word_corpus, sent2))
    return vec1 @ vec2 / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def build_graph(nodes, edges, weights):
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges, weights=weights)
    # G.add_weighted_edges_from(edges)
    
    return G
    

def summarize(document):
    # if consine similarity is used, create word corpus from whole documents
    if SIM_METHOD == 'cosine':
        word_corpus = create_word_corpus(document)

    # calculate the similarity matrix between sentences
    similarity_matrix = np.zeros((len(document), len(document)))

    for i in range(0, len(document)):
        for j in range(i+1, len(document)):
            if SIM_METHOD == 'word overlap':
                similarity_matrix[i, j] = get_word_overlap_similarity(document[i]['tokens'], document[j]['tokens'])
            elif SIM_METHOD == 'cosine':
                similarity_matrix[i, j] = get_cosine_similarity(word_corpus, document[i]['tokens'], document[j]['tokens'])
    
    # print(similarity_matrix)
    # set a threshold for sentence similarity measure
    simIdx = np.argwhere(similarity_matrix > SIM_THRESHOLD)

    # build a graph
    # each sentence is a node,
    # edge exists if sentence similarity is above threshold
    nodes = list(range(len(document)))
    edges = simIdx
    weights = [similarity_matrix[edge] for edge in simIdx]
    # weighted_edges = [(edge[0], edge[1], similarity_matrix[edge]) for edge in simIdx]
    
    G = build_graph(nodes, edges, weights)

    # use pagerank algorithm to find important nodes
    scores = nx.pagerank(G, max_iter=1000)
    sorted_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    # set a threshold for summary
    final_doc = []

    summary_len = int(len(document) * SUMM_THRESHOLD)

    for i, _ in sorted_docs[:summary_len]:
        final_doc.append(document[i])

    return final_doc