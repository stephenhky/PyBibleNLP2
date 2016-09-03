from gensim.models import LsiModel, TfidfModel
from gensim.similarities import MatrixSimilarity
from nltk import word_tokenize

import util.textpreprocessing as prep

class CorpusLsiModelWrapper:
    def __init__(self, corpus, dictionary, doc_labels, preprocessing_pipeline, numtopics,
                 weigh_tfidf=True):
        self.corpus = corpus
        self.dictionary = dictionary
        self.doc_labels = doc_labels
        self.pipeline = preprocessing_pipeline
        self.numtopics = numtopics
        self.weigh_tfidf = weigh_tfidf

    def train(self):
        if self.weigh_tfidf:
            self.tfidf_model = TfidfModel(self.corpus)
            self.masked_corpus = self.tfidf_model[self.corpus]
        else:
            self.masked_corpus = self.corpus

        self.model = LsiModel(self.masked_corpus, num_topics=self.numtopics)
        self.index = MatrixSimilarity(self.model[self.masked_corpus])

    def convertTextToReducedVector(self, text):
        tokens = word_tokenize(prep.preprocess_text(text, self.pipeline))

