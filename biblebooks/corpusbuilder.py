from gensim import corpora
import sqlite3
import BibleAbbrDict as abbr

def build_gensumcorpus(documents):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    return dictionary, corpus

def build_biblebook_corpus(biblesqlite_path, pipeline=[]):
    dbconn = sqlite3.connect(biblesqlite_path)
    cursor = dbconn.cursor()
