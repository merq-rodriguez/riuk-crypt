from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def getKey(password):
    hasher = SHA256.new(password.encode("utf-8"))
    return hasher.digest()

def encrypt(message, key, key_size=256):
    try:
        message = pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
    except Exception as e:
        print("Not encrypt",e)

def decrypt(ciphertext, key):
    try:
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")
    except Exception as e:
        print("Not decrypt", e)
    

def encrypt_file(file_name, key):
    try:
        with open(file_name, 'rb') as fo:
          plaintext = fo.read()
        enc = encrypt(plaintext, key)
        with open(file_name + ".enc", 'wb') as fo:
          fo.write(enc)
        return True
    except Exception as e:
        print("Not encrypt file", e)

def decrypt_file(file_name, key):
    try:
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
            dec = decrypt(ciphertext, key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        return True
    except Exception as e:
        print("Not decrypt file", e)


