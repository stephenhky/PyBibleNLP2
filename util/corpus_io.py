from gensim import corpora

def save_corpus(dictionary, corpus, prefix):
    dictionary.save(prefix+'_dictionary.dict')
    corpora.MmCorpus.serialize(prefix+'_corpus.mm', corpus)

def load_corpus(prefix):
    corpus = corpora.MmCorpus(prefix+'_corpus.mm')
    dictionary = corpora.Dictionary.load(prefix+'_dictionary.dict')
    return corpus, dictionary

def save_doclabel(doc_labels, outputfilename):
    outputfile = open(outputfilename, 'wb')
    outputfile.writelines(doc_labels)
    outputfile.close()

def load_doclabel(inputfilename):
    inputfile = open(inputfilename, 'rb')
    doc_labels = [label.strip() for label in inputfile.readlines()]
    inputfile.close()
    return doc_labels