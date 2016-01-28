from biblebooks.BibleAbbrDict import otbookdict, ntbookdict, getBookName, numchaps

def generateBibleBookAbbrs():
    for bookabbr in otbookdict:
        yield bookabbr
    for bookabbr in ntbookdict:
        yield bookabbr