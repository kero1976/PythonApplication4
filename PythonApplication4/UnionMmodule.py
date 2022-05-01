import logging
import FileModule
import KeywordModule

logger = logging.getLogger(__name__)

def union_keyword(files):
    """
    指定したファイルリストの一覧の内容を結合してキーワード化する
    """
    logging.debug({'status' : 'run',
                   'param' : 'size:' + str(len(files))
        })
    work = []
    for file in files:
        work += FileModule.file_read(file)

    result = []
    result = KeywordModule.create_keyword(work)
    logging.debug({'status' : 'success',
                   'param' : 'size:' + str(len(files)),
                   'resultcount' : 'size:' + str(len(result))
                   })
    return result

def list_keyword(files):
    """
    指定したファイルリストの内容を二次元配列でキーワード化する
    """
    logging.debug({'status' : 'run',
                   'param' : 'size:' + str(len(files))
        })
    result = []
    for file in files:
        result.append( set(FileModule.file_read(file)))


    logging.debug({'status' : 'success',
                   'param' : 'size:' + str(len(files)),
                   'resultcount' : 'size:' + str(len(result))
                   })
    return result