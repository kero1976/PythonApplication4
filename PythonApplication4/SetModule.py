import logging

logger = logging.getLogger(__name__)

def add(lists):
    """
    集合の足し算(和集合)
    {1,3,5},{2,5},{5,10} => {1,2,3,5,10}
    """
    logging.debug({'status' : 'run',
                   'param' : 'size:' + str(len(lists))
        })
    result = set()

    for list in lists:
        result = result.union(list)
    return result

def intersection(lists):
    """
    集合の積集合
    {1,3,5},{2,5},{5,10} => {5}
    """
    logging.debug({'status' : 'run',
                   'param' : 'size:' + str(len(lists))
        })
    result = set()
    first = False

    for list in lists:
        if not first:
            result = list
            first = True
        else:
            result = result.intersection(list)
    return result
