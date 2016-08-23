# import all necessary libraries
from nltk.stem import PorterStemmer
from nltk.tokenize import SpaceTokenizer
from nltk.corpus import stopwords
import re

# initialize the instances for various NLP tools
tokenizer = SpaceTokenizer()
stemmer = PorterStemmer()

# define each steps
pipeline1 = [lambda s: re.sub('[^\w\s]', '', s),
             lambda s: re.sub('[\d]', '', s),
             lambda s: s.lower(),
             lambda s: ' '.join(filter(lambda s: not (s in stopwords.words()), tokenizer.tokenize(s))),
             lambda s: ' '.join(map(lambda t: stemmer.stem(t), tokenizer.tokenize(s)))
             ]
pipeline2 = [lambda s: re.sub('[^\w\s]', '', s),
             lambda s: re.sub('[\d]', '', s),
             lambda s: s.lower(),
             lambda s: ' '.join(filter(lambda s: not (s in stopwords.words()), tokenizer.tokenize(s)))
             ]

# pipeline handling
def preprocess_text(text, pipeline):
    return text if len(pipeline)==0 else preprocess_text(pipeline[0](text), pipeline[1:])
