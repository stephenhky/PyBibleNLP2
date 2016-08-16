# PyBibleNLP2
This repository demonstrate text analytics on the Bible. The first
translation available is the ESV (English Standard Bible) through
Crossway API. They can be converted to an SQLite database. 

## Converting ESV Bible into an SqLite Database
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
