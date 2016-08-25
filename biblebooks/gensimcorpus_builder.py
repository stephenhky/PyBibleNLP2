from gensim import corpora
from nltk import word_tokenize

def build_gensumcorpus(documents):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    return dictionary, corpus

def build_corpus(doc_iterator, preprocess=lambda text: word_tokenize(text)):
    doc_labels = []
    doc_tokens = []
    for doc_label, doc_text in doc_iterator:
        doc_labels += [doc_label]
        doc_tokens += [preprocess(doc_text)]
    return doc_labels, build_gensumcorpus(doc_tokens)

