import DirModule
import logging
import FileModule
import KeywordModule
import UnionMmodule
import SetModule


formatter = "%(asctime)s:%(levelname)s:%(funcName)s:%(message)s"
logging.basicConfig(filename='log.txt' , level=logging.DEBUG, format=formatter)



lists = []
lists.append({1,3,5})
lists.append({2,5})
lists.append({5,10})
lines = SetModule.intersection(lists)
print(lines)