import argparse
import os

from shorttext.classifiers import VarNNEmbeddedVecClassifier
from shorttext.classifiers import frameworks
from shorttext.utils import load_word2vec_model

import biblebooks.bibledocs_iterator as bit

def argument_parser():
    parser = argparse.ArgumentParser(description='Train topic models')
    parser.add_argument('bible_sqlitepath', help='location of the bible')
    parser.add_argument('dir', help='directory of the models')
    parser.add_argument('algo', help='algorithm (CNN / CLSTM / DoubleCNN)')
    parser.add_argument('wvmodel_path', help='Path of the pre-trained Word2Vec model. (None if not needed)')
    return parser

frameworkdict = {'CNN': frameworks.CNNWordEmbed,
                 'CLSTM': frameworks.CLSTMWordEmbed,
                 'DoubleCNN': frameworks.DoubleCNNWordEmbed}

nb_filters = 1200
ngrams_options = [2, 3, 4]
nb_repeats = 3

def main(argnames):
    print 'Loading Word2Vec model...'
    wvmodel = load_word2vec_model(argnames.wvmodel_path)

    print 'Loading data...'
    dbconn = bit.get_sqlite3_dbconn(argnames.bible_sqlitepath)
    biblecorpus = bit.generate_classdict_chapters(dbconn)

    print 'Training...'
    for ngrams in ngrams_options:
        for i in range(nb_repeats):
            print 'Training ', argnames.algo, '; ngrams: ', ngrams, '; round ', i

            modelname = argnames.algo+'_'+str(ngrams)+'gram_chap_model'+str(i)+'.bin'

            kmodel = frameworkdict[argnames.algo](len(biblecorpus.keys()), n_gram=ngrams, nb_filters=nb_filters)
            classifier = VarNNEmbeddedVecClassifier(wvmodel)
            classifier.train(biblecorpus, kmodel)
            classifier.save_compact_model(os.path.join(argnames.dir, modelname))

if __name__ == '__main__':
    parser = argument_parser()
    args = parser.parse_args()

    main(args)