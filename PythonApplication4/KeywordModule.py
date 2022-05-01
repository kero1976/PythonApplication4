import FileModule
import logging

logger = logging.getLogger(__name__)

def read_keyword(filePath):
    """
    KeyWordファイルを読み込み、ソートしてデータとして返す
    空行は取り除く
    """
    logging.debug({'status' : 'run',
                   'param' : filePath
        })
    result = []
    lines = FileModule.file_read(filePath)
    result = create_keyword(lines)

    logging.debug({'status' : 'success',
                   'param' : filePath,
                   'resulecount' : len(result)
        })
    return result

def create_keyword(lines):
    """
    キーワードとして重複を取り除き、ソートする。空行は取り除く
    """
    logging.debug({'status' : 'run',
                   'param' : 'size:' + str(len(lines))
        })
    result = []
    result = list(filter(None, sorted(set(lines), reverse=True)))
    logging.debug({'status' : 'success',
                   'param' :  str(len(lines)),
                   'resulecount' : len(result)
        })
    return result