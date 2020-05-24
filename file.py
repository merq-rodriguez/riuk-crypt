from os import listdir, mkdir, rmdir, remove
from shutil import rmtree, copy2

class File:
     
    def removeFile(self, path):
        return remove(path)

    def copyFile(self, src, destination):
        return copy2(src, destination)
  
    def createFile(self, data, src, fileName, key):
        try:
            with open(fileName+'.config', 'w') as fo:
                fo.write(data)
        except Exception as e:
            print("Not created file", e)

