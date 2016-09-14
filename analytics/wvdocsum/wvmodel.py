from gensim.models.word2vec import Word2Vec
import numpy as np
from nltk import word_tokenize
from scipy.spatial.distance import cosine
import util.textpreprocessing as prep
import util.exceptions as exceptions

class WVModelRetriever:
    def __init__(self, dociter, wvmodel, pipeline=prep.stopword_removal_pipeline):
        self.dociter = dociter
        self.wvmodel = wvmodel
        self.pipeline = pipeline

        # size of vectors
        self.ndim = self.wvmodel.vector_size

        # flag initialized
        self.trained = False

    def train(self):
        self.doc_wvdict = {}
        for doc_label, doc_text in self.dociter:
            self.doc_wvdict[doc_label] = self.convert_text_to_vectors(doc_text)
        self.trained = True

    def convert_text_to_vectors(self, text):
        vec = np.zeros(self.ndim)
        for token in word_tokenize(prep.preprocess_text(text, self.pipeline)):
            if token in self.wvmodel:
                vec += self.wvmodel[token]
        vec /= np.linalg.norm(vec)
        return vec

    def queryDoc(self, text):
        if not self.trained:
            raise exceptions.ModelNotTrainedException()
        wvvec = self.convert_text_to_vectors(text)
        sim = {}
        for doc_label in self.doc_wvdict:
            sim[doc_label] = 1 - cosine(wvvec, self.doc_wvdict[doc_label])
        return sorted(sim.items(), key=lambda p: p[1], reverse=True)

def get_wvmodel_retriever(dociter, word2vec_model_path, binary=True, *args, **kwargs):
    wvmodel = Word2Vec.load_word2vec_format(word2vec_model_path, binary=binary)
    return WVModelRetriever(dociter, wvmodel, *args, **kwargs)