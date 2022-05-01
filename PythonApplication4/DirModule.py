import glob
import logging
import os

logger = logging.getLogger(__name__)

def file_names(dir):
    """
    指定した引数のフォルダにあるファイルをすべて返す
    フォルダは返さない
    """
    logging.debug({'status' : 'run',
                   'param' : dir
        })
    result = []
    logging.debug('  絶対パス:{}'.format(os.path.abspath(dir)))
    if not os.path.exists(dir):
        logging.debug({'status' : 'fail',
                       'param' : dir,
                       'message' : 'is not exists.'})
        return result
    files = glob.glob(dir + "\**", recursive=True)
    for file in files:
        if os.path.isdir(file):
            logging.debug('  {} is Directory'.format(file))
        else:
            logging.debug('  {} is File'.format(file))
            result.append(file)

    logging.debug({'status' : 'success',
                   'param' : dir,
                   'resultcount' : len(result)
        })
    return result


def file_ext_sarch(dir,ext):
    """
    指定した拡張子のファイルのみを取得する
    """
    logging.debug({'status' : 'run',
                   'param[0]' : dir,
                   'param[1]' : ext
        })
    result = []
    files = file_names(dir)
    for file in files:
        if(file.lower().endswith(ext.lower())):
            logging.debug("  {} is OK,".format(file))
            result.append(file)
        else:
            logging.debug("  {} is NG.".format(file))


    logging.debug({'status' : 'success',
                   'param[0]' : dir,
                   'param[1]' : ext,
                   'resulecount' : len(result)
                   })
    return result

def file_name_sarch(dir,name):
    """
    指定したファイルのみ選択する
    """
    logging.debug({'status' : 'run',
                   'param[0]' : dir,
                   'param[1]' : name
        })
    result = []
    files = file_names(dir)
    for file in files:
        if(file.lower().find(name.lower()) != -1):
            logging.debug("  {} is OK,".format(file))
            result.append(file)
        else:
            logging.debug("  {} is NG.".format(file))


    logging.debug({'status' : 'success',
                   'param[0]' : dir,
                   'param[1]' : name,
                   'resulecount' : len(result)
                   })
    return result

def file_extname_changed(dir,old,new):
    """
    指定したフォルダ内のファイルの拡張子を変更する。
    """
    logging.debug({'status' : 'run',
                   'param' : dir
        })
    files = file_names(dir)
    for file in files:
        if(file.endswith(old)):
            os.rename(file, file[:-len(old)] + new)