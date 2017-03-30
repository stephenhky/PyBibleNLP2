# PyBibleNLP2
This repository demonstrate text analytics on the Bible. The first
translation available is the ESV (English Standard Bible) through
Crossway API. They can be converted to an SQLite database. However,
it is also nice if you have other translations that are converted
to this SQLite database format.

## Converting ESV Bible into an SQLite Database
Before conversion, go to <http://www.esvapi.org/> to sign up for a key.
Once you receive the key, run the script `convertCrosswayESVToSQLite.py`. 
Its help message is as follow:

```
usage: convertCrosswayESVToSQLite.py [-h] key sqlitepath

Convert Crossway ESV Bible into SQLite

positional arguments:
  key         ESV access key (please request your ESV access key at
              http://www.esvapi.org/)
  sqlitepath  path of SQLite database

optional arguments:
  -h, --help  show this help message and exit
```

## Converting SQLite Bible into Gensim Corpus
It is helpful to first convert the database into a gensim corpus before
analysis. It does some text preprocessing in the following steps:
* remove special characters
* remove numbers
* lower case
* remove stop words (according to nltk: <http://www.nltk.org/book/ch02.html>)
* stem (using [Porter stemmer](https://tartarus.org/martin/PorterStemmer/))

Then an output of the labels, gensim dictionary, and corpus will be
produced, with file path prefix given by the users. The code is 
`SQLiteToGensimCorpus.py`.
 
```
usage: SQLiteToGensumCorpys.py [-h] [--book]
                               sqlite_bible_path target_path_prefix

Converting SQLite Bible to Gensim Corpus

positional arguments:
  sqlite_bible_path   path of SQLite bible
  target_path_prefix  prefix of gensim corpus and dictionary

optional arguments:
  -h, --help          show this help message and exit
  --book              books (not chapters) as documents
```

# Model Training

The project depends also on `shorttext`: [stephenhky/PyShortTextCategorization](https://github.com/stephenhky/PyShortTextCategorization)  / [API](https://pythonhosted.org/shorttext/)