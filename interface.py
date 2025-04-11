import importlib
import threeDES, AES,TwoFish, ChaCha20, DES, BlowFish, Salsa20, DES, RC4, RSA, SHA, MD5
import checksum
import SensCheck
from tkinter import *

#à tester dès que possible
#ne marche pas pour l'instant, d'abord il faut bien régler FileHandler
#pour tous les (dé)cryptages, j'appelle crypt_all(chemin_source, clé, chemin_destination, fonction(=cryptage ou décryptage))
#du coup j'ai aussi des wrappers crypt et decrypt

crypto_methods=[AES]
hashing_methods=[MD5]
root = Tk()


def home():
    global root
    root.destroy()
    root=Tk()
    button_encrypt=Button(root, text="Encrypter", width=20, command=encrypt)
    button_encrypt.pack()
    button_decrypt=Button(root, text="Décrypter un fichier", width=20, command=decrypt)
    button_decrypt.pack()

def encrypt():
    global root
    global src
    global target
    global key
    global module_var
    global salt
    root.destroy()
    root=Tk()
    module_var=StringVar()
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
    salt_label=Label(root, text="Sel (si nécéssaire)")
    salt_label.pack()
    salt=Entry(root)
    salt.pack()
    button_lost=Button(root, text="Perdu ?", command=questions)
    button_lost.pack()
    for module in crypto_methods :
        radio_encrypt=Radiobutton(root, text=module.__name__, variable=module_var, value=module.__name__)
        radio_encrypt.pack()
    for module in hashing_methods : 
        radio_encrypt=Radiobutton(root, text=module.__name__, variable=module_var, value=module.__name__)
        radio_encrypt.pack()
    checksum_radio=Radiobutton(root, text="checksum", variable=module_var, value="checksum")
    checksum_radio.pack()
    blowfish_radio=Radiobutton(root, text="blowfish", variable=module_var, value="blowfish")
    blowfish_radio.pack()
    button_encrypt=Button(root, text="Crypter", width=20, command=crypt_selection)
    button_encrypt.pack()



def crypt_selection():
    global root
    global module_var
    global src
    global target
    global key
    global module
    global salt
    root.destroy()
    root=Tk()
    module=importlib.import_module(module_var)
    if module_var=="checksum":
        display_checksum()
    if module_var=="blowfish":
        just_to_handle_blowfish_cryptage()
    if module in crypto_methods:
        crypt_wrapper()
    else:
        display_hash()

def crypt_wrapper():
    global src
    global target
    global key
    global module
    module.crypt_all(src.get(), key.get(), target.get(), module.crypt)
    home()

def display_hash():
    global root
    global src
    global module
    fic = src.get()
    root.destroy()
    root=Tk()
    hash = module.hashing(fic)
    print(hash)
    text = Label(root, text="Voici le hash généré : "+ hash)
    text.pack()
    button_return=Button(root, width=20, text="Accueil", command=home)
    button_return.pack()

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
    button_return=Button(root, width=20, text="Accueil", command=home)
    button_return.pack()

def just_to_handle_blowfish_cryptage():
    global src
    global key
    global salt
    global target
    BlowFish.crypt_all(src, key, salt, target, BlowFish.encrypt)
    home()

def decrypt():
    global root
    global src
    global target
    global key
    global module_var
    module_var=StringVar()
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
    button_lost=Button(root, text="Perdu ?", command=questions())
    button_lost.pack()
    for module in crypto_methods:
        radio_decrypt=Radiobutton(root, text=module.__name__, variable=module_var, value=module.__name__)
        radio_decrypt.pack()
    decrypt_button=Button(root, width=20, text="Décrypter", command=decrypt_wrapper)
    decrypt_button.pack()


def questions():
    global root
    global type_var
    global deg_var
    root.destroy()
    root=Tk()
    type_var=IntVar()
    deg_var=IntVar()
    for i in range(3):
        radio_type=Radiobutton(root, text=SensCheck.question_type[i], variable=type_var, value=i)
        radio_type.pack()
    for i in range(3):
        radio_deg=Radiobutton(root, text=SensCheck.question_deg[i], variable=deg_var, value=i)
        radio_deg.pack()
    button_submit=Button(root, text="Trouver un algo", width=20, command=get_algorithm)
    button_submit.pack()


def get_algorithm():
    global type_var
    global deg_var
    global module_var
    global src
    global target
    global key
    global salt
    global root
    module_var=StringVar()
    root.destroy()
    root=Tk()
    recommended_algorithms=SensCheck.get_list_algo_suggestion(deg_var, SensCheck.type_algo(type_var))
    for algo in recommended_algorithms:
        radio_algo=Radiobutton(root, text=algo, variable=module_var, value=algo)
        radio_algo.pack()
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
    salt_label=Label(root, text="Sel (si nécéssaire)")
    salt_label.pack()
    salt=Entry(root)
    salt.pack()
    button_crypt=Button(root, text="Crypter", width=20, command=crypt_selection)
    button_crypt.pack()
    
        
    
def decrypt_wrapper():
    global src
    global target
    global key
    global module_var
    module=importlib.import_module(module_var)
    module.crypt_all(src.get(), key.get(), target.get(), module.decrypt)
    home()    
home()
root.mainloop()
