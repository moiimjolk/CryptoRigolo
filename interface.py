import AES
import checksum
import MD5
from tkinter import *

#reste encore la partie questions

crypto_methods=[AES]
hashing_methods=[MD5]
root = Tk()


def home():
    global root
    button_encrypt=Button(root, text="Encrypter", width=20, command=encrypt)
    button_encrypt.pack()
    button_decrypt=Button(root, text="Décrypter un fichier", width=20, command=decrypt)
    button_decrypt.pack()

def encrypt():
    global root
    global src
    global target
    global key
    root.destroy()
    root=Tk()
    src_label= Label(root, text="Chemin source")
    src_label.pack()
    src = Entry (root)
    src.pack()
    target_label= Label(root, text="Chemin de destination")
    target_label.pack()
    target = Entry(root)
    target.pack()
    key_label= Label(root, text="Clé (si nécéssaire)")
    key_label.pack()
    key = Entry(root)
    key.pack()
    #button_lost=Button(root, text="Perdu ?", command=questions())
    #button_lost.pack()
    button_aes=Button(root, text="AES", width=20, command=crypt_wrapper_aes)
    button_aes.pack()
    button=Button(root, text="MD5", width=20, command=display_MD5)
    button.pack()
    button_checksum=Button(root, text="Checksum", width=20, command=display_checksum)
    button_checksum.pack()

def crypt_wrapper_aes():
    global src
    global target
    global key
    AES.crypt_all(src.get(), key.get(), target.get(), AES.crypt)

def display_MD5():
    global root
    global src
    fic = src.get()
    root.destroy()
    root=Tk()
    hash = MD5.hashing(fic)
    print(hash)
    text = Label(root, text="Voici le hash généré : "+ hash)
    text.pack()
def display_checksum():
    global root
    global src
    global target
    fic_src = src.get()
    fic_target= target.get()
    root.destroy()
    root=Tk()
    if checksum.checksum(fic_src, fic_target):
        text = Label(root, text="Le checksum s'est bien passé !")
        text.pack()
    else:
         text= Label(root, text="Le checksum a échoué, attention la source et la copie sont différentes")
         text.pack()

def decrypt():
    global root
    global src
    global target
    global key
    root.destroy()
    root=Tk()
    src_label= Label(root, text="Chemin source")
    src_label.pack()
    src = Entry (root)
    src.pack()
    target_label= Label(root, text="Chemin de destination")
    target_label.pack()
    target = Entry(root)
    target.pack()
    key_label= Label(root, text="Clé (si nécéssaire)")
    key_label.pack()
    key = Entry(root)
    key.pack()
    #button_lost=Button(root, text="Perdu ?", command=questions())
    #button_lost.pack()
    button_aes=Button(root, text="AES", width=20, command=decrypt_wrapper_aes)
    button_aes.pack()
    
def decrypt_wrapper_aes():
    global src
    global target
    global key
    AES.crypt_all(src.get(), key.get(), target.get(), AES.decrypt)    
home()
root.mainloop()
