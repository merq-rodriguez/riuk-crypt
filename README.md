


<div style="text-align: center"> 

<img src="riuk.png">

## RiukCrypt
This simple script was carried out in an educational way to encrypt files in directories.
AES and SHA256 encryption is used to hash the secret key.
</div>

#### Install Requirements
```bash
pip3 install -r requirements.txt
```


##### Encript
Use -e param for set extensions to encrypt: 

* **web** = 'htm|html|mht|mhtml|xml|yml'
* **word** = 'docx|docm|dotx|doc|dotm|odt|ods|rtf|txt|wps|xps'
* **excel** = 'xlsx|xlsm|xltx|xltm|xlsb|xlam|csv|dbf|dif|prn|slk|xla|xlam|xls|xlt|xlw|xps'
* **power_point** = 'pptx|pptm|potx|potm|ppam|ppa|ppsx|ppsm|sldx|sldm|thmx|bmp|emf|odp|pot|pps|ppt'
* **pdf** = 'pdf'
* **images** = 'gif|jpg|jpeg|png|svg|ai|eps|odg|wmf|cdr|tif|tiff|psd|raw'
* **videos** = 'mp4|avi|mpeg|mpeg-2|mkv|flv|mov|wmv'
* **audio** = 'mp3|gsm|dct|vox|smaf|aiff|au|alac|ogg|vorbis|opus|mpc|tta|aac|wma|wav|atrac|ram|iklax|midi'
* **development** = 'json|js|py|go|cpp|c|o|java|css|'

User -e '.*' for encrypt all extensions in folder

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

## Stay in touch

* Author - [Stiven Rodriguez](https://twitter.com/stiiven_uchiha)
* Twitter - [@stiiven_uchiha](https://twitter.com/stiiven_uchiha)