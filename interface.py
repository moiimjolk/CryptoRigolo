import importlib
import threeDES, AES,TwoFish, ChaCha20, DES, BlowFish, Salsa20, DES, RC4, RSA, SHA, MD5, BlowFish
import Checksum
import SensCheck
from tkinter import *

#peut retourner des erreurs dans le terminal alors que le programme est effectivement exécuté comme il faut au décryptage
#ainsi le code est tout de même décrypté

crypto_methods=[AES, DES, RC4, RSA, BlowFish, TwoFish, ChaCha20, Salsa20, threeDES]
hashing_methods=[MD5, SHA]
root = Tk()


def home():
    global root
    root.destroy()
    root=Tk()
    button_encrypt=Button(root, text="Encrypter", width=20, command=encrypt)
    button_encrypt.pack()
    button_decrypt=Button(root, text="Décrypter", width=20, command=decrypt)
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
    explainations = Label(root, text="La plupart des algos nécéssitent une clé seulement\n" \
    "Pour les hashs pas besoin de clé\n" \
    "TwoFish et BlowFish nécéssitent un salt, un nombre en binaire\n" \
    "ChaCha20 et Salsa20 nécéssitent 2 clés\n" \
    "3DES nécéssite 3 clés\n" \
    "RSA fournit ses clés au cryptage\n")
    explainations.pack()
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
        module=importlib.import_module(module_var.get())
    if module_var.get()=="Checksum":
        display_checksum()
    elif module_var.get()=="threeDES":
        just_to_handle_3DS_cryptage()
    elif "Fish" in module_var.get():
        just_to_handle_fish_cryptage()
    elif "20" in module_var.get():
        just_to_handle_20_cryptage()
    elif "RSA" == module_var.get():
        display_for_RSA()
    elif module in crypto_methods:
        crypt_wrapper()
    else:
        display_hash(module_var.get())

def crypt_wrapper():
    global src
    global target
    global key
    global module
    module.crypt_all(src.get(), key.get(), target.get(), module.crypt)
    home()

def display_hash(algo):
    global root
    global src
    global module
    fic = src.get()
    reader= open(fic,"r")
    if algo == "MD5":
        hash = module.hashing(fic)
    
    elif algo == "SHA1":
        hash=module.sha1_hash(reader.read())

    elif algo == "SHA256":
        hash=module.sha256_hash(reader.read())

    else:
        hash=module.sha512_hash(reader.read())
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
    if Checksum.checksum(fic_src, fic_target):
        text = Label(root, text="Le checksum s'est bien passé !")
        text.pack()
    else:
         text= Label(root, text="Le checksum a échoué, attention la source et la copie sont différentes")
         text.pack()
    button_return=Button(root, width=20, text="Accueil", command=home)
    button_return.pack()


def display_for_RSA():
    global root
    global src
    global target
    public_key, private_key= RSA.crypt_all(src.get(),"", "", target.get(), RSA.crypt)
    root.destroy()
    root=Tk()
    public_key_label=Label(root, text="Votre clé public est dans le fichier cle_publique ")
    public_key_label.pack()
    fic_pub=open("cle_publique.txt","w")
    fic_priv=open("cle_privee.txt", "w")
    fic_pub.write(str(public_key))
    fic_priv.write(str(private_key))
    fic_priv.close()
    fic_pub.close()
    private_key_label=Label(root, text="Votre clé privée est dans le fichier cle_privee ")
    private_key_label.pack()
    button_return=Button(root, width=20, text="Accueil", command=home)
    button_return.pack()

def just_to_handle_RSA():
    global src
    global target
    global key
    RSA.crypt_all(src.get(), "", key.get(), target.get(), RSA.decrypt)

def just_to_handle_fish_cryptage():
    global src
    global key
    global salt
    global module
    global target
    module.crypt_all(src.get(), key.get(), salt.get(), target.get(), module.crypt)
    home()


def just_to_handle_fish_decryptage():
    global src
    global key
    global salt
    global target
    global module
    module.crypt_all(src.get(), key.get(), salt.get(), target.get(), module.decrypt)
    home()

def just_to_handle_3DS_cryptage():
    global src
    global key
    global salt
    global target
    global key3
    threeDES.crypt_all(threeDES.triple_des_encrypt_full, key.get(), salt.get(), key3.get(), src.get(), target.get())
    home()

def just_to_handle_3DS_decryptage():
    global src
    global key
    global  salt
    global target
    global key3
    threeDES.crypt_all(threeDES.triple_des_decrypt_full, key.get(), salt.get(), key3.get(), src.get(), target.get())
    home()

def just_to_handle_20_cryptage():
    global src
    global key
    global salt
    global target
    global module
    module.crypt_all(key.get(), salt.get(), src.get(), target.get())
    home()
    

def decrypt():
    global root
    
    root.destroy()
    root=Tk()
    
    global src
    global target
    global key
    global salt
    global key3
    global module_var
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
    salt_label= Label(root, text="2e clé (si nécéssaire)")
    salt_label.pack()
    salt = Entry(root)
    salt.pack()
    key3_label= Label(root, text="3e clé (si nécéssaire)")
    key3_label.pack()
    key3 = Entry(root)
    key3.pack()
    explainations = Label(root, text="La plupart des algos nécéssitent une clé seulement\n" \
    "TwoFish et BlowFish nécéssitent un salt, un nombre en binaire\n" \
    "ChaCha20 et Salsa20 nécéssitent 2 clés\n" \
    "3DES nécéssite 3 clés\n" )
    explainations.pack()
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
    global salt
    global key3
    global module_var
    module=importlib.import_module(module_var.get())
    if "Fish" in module_var.get():
        just_to_handle_fish_decryptage()
    elif "20" in module_var.get():
        just_to_handle_20_cryptage()
    elif module_var.get()=="threeDES":
        just_to_handle_3DS_decryptage()
    elif module_var.get() == "RSA":
        just_to_handle_RSA()
    else:
        module.crypt_all(src.get(), key.get(), target.get(), module.decrypt)
    home()    
home()
root.mainloop()
