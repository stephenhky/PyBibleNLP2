import sqlite3

from biblebooks import BibleAbbrDict as abbr

def retrieve_docs_as_biblechapters(dbconn):
    cursor = dbconn.cursor()
    for book in abbr.otbookdict.keys() + abbr.ntbookdict.keys():
        for chap in range(1, abbr.numchaps[book]+1):
            doc_label = book+'_'+str(chap)
            result = cursor.execute('select scripture from bible where book is "'+book+'" and chapter='+str(chap))
            doc_text = reduce(lambda s1, s2: ' '.join([s1, s2]), [texttuple[0] for texttuple in result])
            yield doc_label, doc_text
    cursor.close()

def retrieve_docs_as_biblebooks(dbconn):
    cursor = dbconn.cursor()
    for book in abbr.otbookdict.keys() + abbr.ntbookdict.keys():
        doc_label = book
        result = cursor.execute('select scripture from bible where book is "'+book+'"')
        doc_text = reduce(lambda s1, s2: ' '.join([s1, s2]), [texttuple[0] for texttuple in result])
        yield doc_label, doc_text
    cursor.close()

def get_sqlite3_dbconn(biblesqlite_path):
    return sqlite3.connect(biblesqlite_path)