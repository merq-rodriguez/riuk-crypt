


<div style="text-align: center"> 

<img src="riuk.png">

## RiukCrypt
This simple script was carried out in an educational way to encrypt files in directories.
AES and SHA256 encryption is used to hash the secret key.
</div>

#### Install Requirements
```bash
pip3 install requirements.txt
```


##### Encript
```bash
$ python3 -B main.py  --folder '/home/folder_to_encrypt' --keysecret 'xxxxxxx' --action encrypt -e "jpeg|pdf"
```

##### Decript
```bash
$ python3 -B main.py  --folder '/home/folder_to_encrypt' --keysecret 'xxxxxxx' --action decrypt
```

# Ó

##### Make binary
```bash
$ make  
```

##### Encript
```bash
$ riuk --folder '/home/folder_to_encrypt' --keysecret 'xxxxxxx' --action encrypt -e "jpeg|pdf"
```

##### Decript
```bash
$ riuk --folder '/home/folder_to_encrypt' --keysecret 'xxxxxxx' --action decrypt
```