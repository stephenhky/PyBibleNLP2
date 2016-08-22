from gensim import corpora
import sqlite3
from nltk import word_tokenize
from operator import add
import BibleAbbrDict as abbr

def build_gensumcorpus(documents):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    return dictionary, corpus

def build_biblechapters_corpus(biblesqlite_path, preprocess=lambda text: text):
    dbconn = sqlite3.connect(biblesqlite_path)
    cursor = dbconn.cursor()
    doc_labels = []
    doc_tokens = []
    for book in abbr.otbookdict.keys() + abbr.ntbookdict.keys():
        for chap in range(1, abbr.numchaps[book]+1):
            doc_labels += [book+'_'+chap]
            result = cursor.execute('select scripture from bible where book is "'+book+'" and chapter='+chap)
            doc_tokens += [reduce(add, [word_tokenize(preprocess(text)) for text in result])]
    cursor.close()
    return build_gensumcorpus(doc_tokens)
