# 1 : Non-sécurisé
# 2 : Sécurisé
# 3 : Très Sécurisé
# ---------------------------------------------------
# Petite notes :
#
# RSA n'est pas en 3 parce que j'ai diminué le nombre de bit pris en compte mais ça reste toujours très viable
#
# type_algo : renvoie le dico des algo spécifique
# get_list_algo_suggestion : renvoie la liste du degrès choisis
#
# Explication de get_list_algo_suggestion, asym_algos et hash_algos n'ont pas de deg 1, donc dans le elif il va 
# dans le deg le plus proche donc +1, pareil pour le dernier cas -1 car asym_algos n'a pas de deg 3

question_type = [
    "Souhaitez-vous un algorithme qui sert à cacher un message et pouvoir le relire ensuite (comme un cadenas) ?",  # Sym
    "Souhaitez-vous un algorithme pour sécuriser un échange entre deux personnes (comme un cadenas avec une seule clé pour chacun) ?",  # Asym
    "Souhaitez-vous un algorithme qui sert uniquement à vérifier l’intégrité d’un fichier ou mot de passe (comme une empreinte digitale) ?"  # Hash
]

question_deg = [
    "Votre priorité est-elle d'aller vite, même si ce n'est pas très sécurisé ?", #1
    "Souhaitez-vous un bon compromis entre sécurité et performance, sans que ce soit trop complexe ?", #2
    "Souhaitez-vous une sécurité maximale, même si cela demande plus de ressources ou de temps ?" #3
]

sym_algos = {
    1: ["AES", "TwoFish", "ChaCha20"],
    2: ["3DES", "BlowFish", "Salsa20"],
    3: ["DES", "RC4"]
}

asym_algos = {
    2: ["RSA"]
}

hash_algos = {
    2: ["SHA"],
    3: ["MD5"]
}

def type_algo(input):
    if input == 1 : return sym_algos
    if input == 2 : return asym_algos
    if input == 3 : return hash_algos

def get_list_algo_suggestion(deg, type):
    if deg in type : return type[deg]
    elif deg == 1 : return type[deg + 1]
    else : return type[deg - 1]

# test

type = type_algo(1)
deg = 1
print(get_list_algo_suggestion(deg, type))
