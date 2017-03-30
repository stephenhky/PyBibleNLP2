import argparse
import os

from shorttext.classifiers import LDAModeler, LSIModeler, RPModeler

import biblebooks.bibledocs_iterator as bit

def argument_parser():
    parser = argparse.ArgumentParser(description='Train topic models')
    parser.add_argument('bible_sqlitepath', help='location of the bible')
    parser.add_argument('dir', help='directory of the models')
    parser.add_argument('algo', help='algorithm (lda / lsi / rp)')
    return parser

nbs_topics = [128, 256, 512, 1024, 2048]
nb_repeats = 10

modelerdict = {'lda': LDAModeler, 'lsi': LSIModeler, 'rp': RPModeler}

def main(argnames):
    dbconn = bit.get_sqlite3_dbconn(argnames.bible_sqlitepath)
    for nb_topics in nbs_topics:
        for i in range(nb_repeats):
            print 'Training ', argnames.algo, '; nb_topics: ', nb_topics, '; round ', i

            modelname = argnames.algo+'_bntopics'+str(nb_topics)+'_chap_model'+str(i)+'.bin'
            topicmodeler = modelerdict[argnames.algo]()
            topicmodeler.train(bit.generate_classdict_chapters(dbconn), nb_topics)

            topicmodeler.save_compact_model(os.path.join(argnames.dir, modelname))

if __name__ == '__main__':
    parser = argument_parser()
    args = parser.parse_args()

    main(args)