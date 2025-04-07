

#alors là je veux pas me casser la tête à implémenter des versions compliquées :>

def get_sum(text):
    sum=0
    src = open(text, "r", encoding='utf-8')
    for carac in src.read():
        sum+=ord(carac)
    return sum%256


def checksum(src, copy):
    initial_sum= get_sum(src)
    copy_sum = get_sum(copy)
    return initial_sum == copy_sum
