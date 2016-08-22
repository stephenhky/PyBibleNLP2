from gensim import corpora
import sqlite3
from nltk import word_tokenize
import BibleAbbrDict as abbr

def build_gensumcorpus(documents):
    dictionary = corpora.Dictionary(documents)
    corpus = [dictionary.doc2bow(text) for text in documents]
    return dictionary, corpus

def retrieve_docs_as_biblechapters(biblesqlite_path):
    dbconn = sqlite3.connect(biblesqlite_path)
    cursor = dbconn.cursor()
    for book in abbr.otbookdict.keys() + abbr.ntbookdict.keys():
        for chap in range(1, abbr.numchaps[book]+1):
            doc_label = book+'_'+chap
            result = cursor.execute('select scripture from bible where book is "'+book+'" and chapter='+chap)
            doc_text = reduce(lambda s1, s2: ' '.join(s1, s2), [text for text in result])
            yield doc_label, doc_text
    cursor.close()

def retrieve_docs_as_biblebooks(biblesqlite_path):
    dbconn = sqlite3.connect(biblesqlite_path)
    cursor = dbconn.cursor()
    for book in abbr.otbookdict.keys() + abbr.ntbookdict.keys():
        doc_label = book
        result = cursor.execute('select scripture from bible where book is "'+book)
        doc_text = reduce(lambda s1, s2: ' '.join(s1, s2), [text for text in result])
        yield doc_label, doc_text
    cursor.close()

def build_corpus(doc_iterator, preprocess=lambda text: text):
    doc_labels = []
    doc_tokens = []
    for doc_label, doc_text in doc_iterator:
        doc_labels += [doc_label]
        doc_tokens += [word_tokenize(preprocess(doc_text))]
    return doc_labels, build_gensumcorpus(doc_tokens)

