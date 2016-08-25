import biblebooks.bibledocs_iterator as bibledocs
import biblebooks.gensimcorpus_builder as cpbuilder
import util.textpreprocessing as prep
import util.corpus_io as io
import argparse
from nltk import word_tokenize

def argument_parser():
    parser = argparse.ArgumentParser(description='Converting SQLite Bible to Gensim Corpus')
    parser.add_argument('sqlite_bible_path', help='path of SQLite bible')
    parser.add_argument('target_path_prefix', help='prefix of gensim corpus and dictionary')
    parser.add_argument('--book', action='store_true', default=False, help='books (not chapters) as documents')
    return parser

if __name__ == '__main__':
    parser = argument_parser()
    args = parser.parse_args()

    print 'Read the database'
    sqlite_bible = bibledocs.get_sqlite3_dbconn(args.sqlite_bible_path)
    doc_iterator = bibledocs.retrieve_docs_as_biblebooks(sqlite_bible) if args.book else bibledocs.retrieve_docs_as_biblechapters(sqlite_bible)
    print 'Build the corpus'
    doc_label, (dictionary, gensim_corpus) = cpbuilder.build_corpus(doc_iterator,
                                                                    preprocess=lambda s: word_tokenize(prep.preprocess_text(s, prep.pipeline1))
                                                                   )
    print 'Save the corpus'
    io.save_corpus(dictionary, gensim_corpus, args.target_path_prefix)
    io.save_doclabel(doc_label, args.target_path_prefix+'_doclabels.txt')