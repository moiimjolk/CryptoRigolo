def read(src):
    """Gives a list of the ASCII code of each letter"""
    fic = open(src, "r", encoding='utf-8')
    list=[]
    for carac in fic.read():
        list.append(ord(carac))
    fic.close()

def write(target, list):
    """Write the file with the letters given in list """
    fic = open(target, "w", encoding='utf-8')
    for carac in list:
        fic.write(carac)
    fic.close()

#j'ai fait le strict minimum ici j'abuse
#mais en même temps je sais pas quoi faire de plus
#d'ailleurs je sais même pas s'il est nécéssaire ce module...