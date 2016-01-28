from biblebooks import getBookName, numchaps, generateBibleBookAbbrs
from xml.dom.minidom import parseString
import urllib
import urllib2
import sqlite3

baseurl = 'http://www.esvapi.org/v2/rest/'

class CrosswayOnlineESVParser:
    def __init__(self, key):
        self.key = key

    def query(self, bookabbr, chapidx):
        bookname = getBookName(bookabbr)
        query_args = {'key': self.key, 'passage': bookname+' '+str(chapidx), 'output-format': 'crossway-xml-1.0'}
        query_url = baseurl+'passageQuery?'+urllib.urlencode(query_args)
        return urllib2.urlopen(query_url)

class OnlineESVToSQLiteConverter:
    def __init__(self, online_parser, sqlitefilepath):
        self.parser = online_parser
        self.dbconn = sqlite3.connect(sqlitefilepath)
        self.cursor = self.dbconn.cursor()

    def run(self):
        self.create_table()
        self.convert_all()

    def closeDB(self):
        self.dbconn.commit()
        self.dbconn.close()

    def create_table(self):
        self.cursor.execute('''
            create table BIBLE (BOOK TEXT, CHAPTER INTEGER, VERSE INTEGER, SCRIPTURE TEXT)
        ''')
        self.dbconn.commit()

    def extract_verse(self):
        for bookabbr in generateBibleBookAbbrs():
            for chapidx in range(1, numchaps[bookabbr]+1):
                print getBookName(bookabbr), chapidx
                xmlstr = '\n'.join(self.parser.query(bookabbr, chapidx))
                dom = parseString(xmlstr)
                for item in dom.getElementsByTagName('verse-unit'):
                    nodenames = map(lambda node: node.nodeName, item.childNodes)
                    versenum = -1
                    versetext = ''
                    for posid, nodename in zip(range(len(nodenames)), nodenames):
                        if nodename == 'verse-num':
                            versenum = int(item.childNodes[posid].firstChild.nodeValue)
                        if nodename == '#text':
                            versetext += ' '+item.childNodes[posid].nodeValue.strip()
                        if nodename == 'woc':
                            versetext += ' '+item.childNodes[posid].firstChild.nodeValue.strip()
                    if versenum>0:
                        yield (bookabbr, chapidx, versenum, versetext)

    def convert_all(self):
        for infotuple in self.extract_verse():
            self.cursor.executemany('insert into BIBLE (BOOK, CHAPTER, VERSE, SCRIPTURE) values (?, ?, ?, ?)',
                                    [infotuple])
        self.dbconn.commit()

