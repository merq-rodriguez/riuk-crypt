import os
import re 
from os import path, walk

class Find:
    def __init__(self, path):
        self.__path=path

    def findFiles(self, extentions):
        rx = re.compile(extentions)
        r = []
        for vpath, dnames, fnames in walk(self.__path):
            r.extend([path.join(vpath, x) for x in fnames if rx.search(x)])

        return r