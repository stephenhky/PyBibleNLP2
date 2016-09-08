# from gensim.models import word2vec
import numpy as np
from nltk import word_tokenize
from scipy.spatial.distance import cosine
from keras.models import Sequential
from keras.layers import Convolution1D, Activation, Dropout
from keras.optimizers import SGD

import util.textpreprocessing as prep
import util.exceptions as exceptions
import analytics.wvdocsum.wvmodel as wv


class CNNWVModelRetriever(wv.WVModelRetriever):

    def train(self):
        CNNWVModelRetriever.train(self)
        self.trained = False      # turn the flag to False first
        model = Sequential()
        model.add(Convolution1D(100, 1))
        model.add(Activation('relu'))
        model.add(Dropout(0.25))
        sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
        model.compile(loss='categorical_crossentropy', optimizer=sgd)
        model.fit()

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