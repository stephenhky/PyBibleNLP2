from gensim import corpora
from shorttext.utils import tokenize

def build_gensumcorpus(documents):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    return dictionary, corpus

def build_corpus(doc_iterator, preprocess=tokenize):
    doc_labels = []
    doc_tokens = []
    for doc_label, doc_text in doc_iterator:
        doc_labels += [doc_label]
        doc_tokens += [preprocess(doc_text)]
    return doc_labels, build_gensumcorpus(doc_tokens)

