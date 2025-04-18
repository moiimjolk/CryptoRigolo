import importlib
import threeDES, AES,TwoFish, ChaCha20, DES, BlowFish, Salsa20, DES, RC4, RSA, SHA, MD5, BlowFish
import checksum
import SensCheck
from tkinter import *

#à tester dès que possible
#ne marche pas pour l'instant, d'abord il faut bien régler FileHandler
#pour tous les (dé)cryptages, j'appelle crypt_all(chemin_source, clé, chemin_destination, fonction(=cryptage ou décryptage))
#du coup j'ai aussi des wrappers crypt et decrypt

crypto_methods=[AES, DES, RC4, RSA, BlowFish, TwoFish, ChaCha20, Salsa20]
hashing_methods=[MD5, SHA]
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
    global key3
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
    salt_label=Label(root, text="Sel/nonce/2e clé (si nécéssaire)")
    salt_label.pack()
    salt=Entry(root)
    salt.pack()
    key3_label= Label(root, text="3e clé (si nécéssaire)")
    key3_label.pack()
    key3 = Entry(root)
    key3.pack()
    button_lost=Button(root, text="Perdu ?", command=questions)
    button_lost.pack()
    for module in crypto_methods :
        radio_encrypt=Radiobutton(root, text=module.__name__, variable=module_var, value=module.__name__)
        radio_encrypt.pack()
    radio_MD5=Radiobutton(root, text="MD5", variable=module_var, value="MD5")
    radio_MD5.pack()
    radio_sha1=Radiobutton(root, text="SHA1", variable=module_var, value="SHA1")
    radio_sha1.pack()
    radio_sha256=Radiobutton(root, text="SHA256", variable=module_var, value="SHA256")
    radio_sha256.pack()
    radio_sha512=Radiobutton(root, text="SHA512", variable=module_var, value="SHA512")
    radio_sha512.pack()
    checksum_radio=Radiobutton(root, text="checksum", variable=module_var, value="Checksum")
    checksum_radio.pack()
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
    global key3
    if  "SHA" in module_var.get():
        module=SHA
    else:
        print(module_var.get())
        module=importlib.import_module(module_var.get())
    if module_var.get()=="Checksum":
        display_checksum()
    elif module_var.get()=="threeDES":
        just_to_handle_3DS_cryptage()
    elif "Fish" in module_var.get():
        just_to_handle_fish_cryptage()
    elif "20" in module_var.get():
        just_to_handle_20_cryptage()
    elif module in crypto_methods:
        crypt_wrapper()
    else:
        display_hash(module_var.get())

def crypt_wrapper():
    global src
    global target
    global key
    global module
    print(len(key.get()))
    module.crypt_all(src.get(), key.get(), target.get(), module.crypt)
    home()

def display_hash(algo):
    global root
    global src
    global module
    fic = src.get()
    
    if algo == "MD5":
        hash = module.hashing(fic)
    else:
        hash=module.algo(fic)
    root.destroy()
    root=Tk()
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

def just_to_handle_fish_cryptage():
    global src
    global key
    global salt
    global module
    global target
    module.crypt_all(src, key, salt, target, module.crypt)
    home()


def just_to_handle_fish_decryptage():
    global src
    global key
    global salt
    global target
    global module
    module.crypt_all(src, key, salt, target, module.decrypt)
    home()

def just_to_handle_3DS_cryptage():
    global src
    global key
    global salt
    global target
    global key3
    threeDES.crypt_all((threeDES.triple_des_encrypt_full, key, salt, key3, src, target))
    home()

def just_to_handle_3DS_decryptage():
    global src
    global key
    global key2
    global target
    global key3
    threeDES.crypt_all((threeDES.triple_des_decrypt_full, key, salt, key3, src, target))
    home()

def just_to_handle_20_cryptage():
    global src
    global key
    global key2
    global target
    global module
    module.crypt_all(key, key2, src, target)
    home()
    

def decrypt():
    global root
    global src
    global target
    global key
    global key2
    global key3
    global module_var
    
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
    key2_label= Label(root, text="2e clé (si nécéssaire)")
    key2_label.pack()
    key2 = Entry(root)
    key2.pack()
    key3_label= Label(root, text="3e clé (si nécéssaire)")
    key3_label.pack()
    key3 = Entry(root)
    key3.pack()
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
    for i in range(1,4):
        radio_type=Radiobutton(root, text=SensCheck.question_type[i-1], variable=type_var, value=i)
        radio_type.pack()
    for i in range(1,4):
        radio_deg=Radiobutton(root, text=SensCheck.question_deg[i-1], variable=deg_var, value=i)
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
    global key3 
    recommended_algorithms=SensCheck.get_list_algo_suggestion(deg_var.get(), SensCheck.type_algo(type_var.get()))
    root.destroy()
    root=Tk()
    module_var=StringVar()
    for algo in recommended_algorithms:
        radio_algo=Radiobutton(root, text=algo, variable=module_var, value=algo)
        radio_algo.pack()
        if algo == "SHA":
            radio_sha1=Radiobutton(root, text="SHA1", variable=module_var, value="SHA1")
            radio_sha1.pack()
            radio_sha256=Radiobutton(root, text="SHA256", variable=module_var, value="SHA256")
            radio_sha256.pack()
            radio_sha512=Radiobutton(root, text="SHA512", variable=module_var, value="SHA512")
            radio_sha512.pack()
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
    global key2
    global key3
    global module_var
    module=importlib.import_module(module_var.get())
    if "Fish" in module_var.get():
        just_to_handle_fish_decryptage()
    elif "20" in module_var.get():
        just_to_handle_20_cryptage()
    module.crypt_all(src.get(), key.get(), target.get(), module.decrypt)
    home()    
home()
root.mainloop()
