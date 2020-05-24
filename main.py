from os import listdir, mkdir, rmdir, makedirs, path, readlink, symlink,  path, getcwd, environ, walk
from cryptfile import encrypt_file, decrypt_file, getKey
from file import File
from find import Find
import re
import sys, getopt

class Encryption:
    def __init__(self, path, secretkey):
        self.__key = getKey(str(secretkey))
        self.__path = path
        self.__file = File()
 
    def encryptFolder(self, extentions):
        find = Find(self.__path)
        array = find.findFiles(extentions)
        for i in array:
            result = self.encryptFile(i)
            if result == True:
                self.__file.removeFile(i)
                print("[+] Encript: "+i)

    def decryptFolder(self):
        find = Find(self.__path)
        array = find.findFiles(r'\.(enc)')
        for i in array:
            encrypt = self.decriptFile(i)
            if encrypt == True:
                print("[-] Decript: "+i)
                self.__file.removeFile(i)                
    
    def encryptFile(self, fileName):
        pathFile = path.join(self.__path, fileName)
        return encrypt_file(pathFile, self.__key)
        
  
    def decriptFile(self, pathFile):
        return decrypt_file(pathFile, self.__key)

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action", action="store", required=True, choices=['encrypt', 'decrypt'], help='Debe especificar la action que desea realizar (encript ó decript)')   
    parser.add_argument("-f", "--folder", action="store", required=True, help="Debe especificar la ruta del directorio a cifrar o descifrar")   
    parser.add_argument("-k", "--keysecret", action="store", required=True, help="Debe agregar la clave secreta")   
    parser.add_argument("-e", "--extentions", action="store", required=False, help="Ingrese las extenciones")   
    args = parser.parse_args()
    
    key = args.keysecret
    folder = args.folder
    action = args.action
    extentions = str(args.extentions)
    
    encry = Encryption(path=folder, secretkey=key)
    ext = r'\.('+extentions+')'
    
    if action == 'encrypt':
        encry.encryptFolder(ext)
    elif action == 'decrypt':
        encry.decryptFolder()

main()

        