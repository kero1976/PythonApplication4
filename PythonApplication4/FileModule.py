import csv
import logging
import DirModule

logger = logging.getLogger(__name__)

def file_read(filePath):
    """
    ファイルを読み込み、リストにして返す
    """
    logging.debug({'status' : 'run',
                   'param' : filePath
        })
    result = []
    files = DirModule.file_names(filePath)
    if not len(files) == 1:
        logging.debug({'status' : 'fail',
                       'param' : filePath,
                       'message' : 'file not found.'
                       })
        return
    with open(filePath,'r') as f:
        result = f.read().splitlines()

    logging.debug({'status' : 'success',
                   'param' : filePath,
                   'resultcount' : len(result)
                   })
    return result

def file_write(filePath, lines):
    """
    ファイルに書き込む
    """
    logging.debug({'status' : 'run',
                   'param[0]' : filePath,
                   'param[1]' : 'size:' + str(len(lines))
        })
    with open(filePath, mode='w') as f:
        f.write('\n'.join(lines))

    logging.debug({'status' : 'success',
                   'param[0]' : filePath,
                   'param[1]' : 'size:' + str(len(lines))
        })