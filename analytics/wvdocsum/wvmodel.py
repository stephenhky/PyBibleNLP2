# from gensim.models import word2vec
import numpy as np
from nltk import word_tokenize
from scipy.spatial.distance import cosine

class WVModelRetriever:
    def __init__(self, dociter, wvmodel, pipeline=[]):
        self.dociter = dociter
        self.wvmodel = wvmodel
        self.pipeline = pipeline

        # size of vectors
        self.ndim = self.wvmodel.vector_size

    def train(self):
        self.doc_wvdict = {}
        for doc_label, doc_text in self.dociter:
            self.doc_wvdict[doc_label] = self.convert_text_to_vectors(doc_text)

    def convert_text_to_vectors(self, text):
        vec = np.zeros(self.ndim)
        for token in word_tokenize(text):
            if token in self.wvmodel:
                vec += self.wvmodel[token]
        vec /= np.linalg.norm(vec)
        return vec

    def queryDoc(self, text):
        wvvec = self.convert_text_to_vectors(text)
        sim = {}
        for doc_label in self.doc_wvdict:
            sim[doc_label] = 1 - cosine(wvvec, self.doc_wvdict[doc_label])
        return sorted(sim.items(), key=lambda p: p[1], reverse=True)