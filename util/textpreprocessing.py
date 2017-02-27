# import all necessary libraries
from shorttext.utils.textpreprocessing import stopwordset     # stopword
from shorttext.utils import tokenize
import re

# define each steps
pipeline2 = [lambda s: re.sub('[^\w\s]', '', s),
             lambda s: re.sub('[\d]', '', s),
             lambda s: s.lower(),
             lambda s: ' '.join(filter(lambda s: not (s in stopwordset), tokenize(s)))
             ]
stopword_removal_pipeline = [lambda s: ' '.join(filter(lambda s: not (s in stopwordset), tokenize(s)))]

