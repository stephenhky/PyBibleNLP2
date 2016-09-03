

class BibleException(Exception):
    def __init__(self, msg):
        self._message = msg

    def _get_message(self):
        return self._message

    def __str__(self):
        return self._get_message()

class NoBibleBookException(BibleException):
    def __init__(self, bookabbr):
        self._message = 'No such book ('+bookabbr+') exists.'

class InvalidBibleLocationException(BibleException):
    def __init__(self, bookabbr, chap, verse):
        self._message = 'No such location '+bookabbr+' '+str(chap)+':'+str(verse)

class InvalidBibleChapterException(BibleException):
    def __init__(self, bookabbr, chap):
        self._message = 'The book '+bookabbr+' does not have chapter '+str(chap)

class TokenNotFoundException(BibleException):
    def __init__(self, token):
        self._message = 'Token ['+token+'] not found.'

class NoBibleTranslationException(BibleException):
    def __init__(self, transver):
        self._message = 'No such translation ('+transver+') supported.'

class ModelNotTrainedException(Exception):
    def __init__(self):
        self._message = 'Model not trained.'