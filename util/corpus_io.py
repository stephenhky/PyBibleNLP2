from gensim import corpora

def save_corpus(dictionary, corpus, prefix):
    dictionary.save(prefix+'_dictionary.dict')
    corpora.MmCorpus.serialize(prefix+'_corpus.mm', corpus)

def load_corpus(prefix):
    corpus = corpora.MmCorpus(prefix+'_corpus.mm')
    dictionary = corpora.Dictionary.load(prefix+'_dictionary.dict')
    return corpus, dictionary