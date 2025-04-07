from copy import deepcopy
from math import *


#fonctionnel mais faux 
#au moins ça m'a l'air de produire une signature unique T_T



r=[7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22,  7, 12, 17, 22, 5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20,  5,  9, 14, 20, 4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23,  4, 11, 16, 23, 6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21,  6, 10, 15, 21]
k=[floor(abs(sin(i+1))) * 2**32 for i in range(64)]


def text_to_bits(text):
    src = open(text,"r")
    length=0
    bits = ""
    for carac in src.read():
        current_bit= str(format(ord(carac), "b"))
        bits+= current_bit
        length+= len(current_bit)
    return bits, length

def processing_input(text):
    bits, length = text_to_bits(text)
    first=True
    while  (length - 448)%512 != 0:
        if first:
            bits+= "1"
            first=False
        else:
            bits+="0"
        length+=1
    return bits

def append_length(length, bits):
    bit = f"{length:0b}"
    bits+=(f"{length:0b}")
    return length + len(bit)

def producing_variables():
    a= 0x67452301
    b= 0xefcdab89
    c= 0x98badcfe
    d= 0x10325476
    return a, b, c, d

def cut_in_blocks(bits):
    blocks=[]
    current_block=""
    bits_counter=0
    for number in bits:
        if bits_counter == 512:
            blocks.append(current_block)
            bits_counter=0
            current_block=""
        current_block+= number
        bits_counter+=1
    return blocks

def cut_in_very_small_blocks(block):
    blocks=[]
    current_block=""
    bits_counter=0
    for number in block:
        if bits_counter == 32:
            blocks.append(current_block)
            bits_counter=0
            current_block=""
        current_block+= number
        bits_counter+=1
    blocks.append(current_block)
    return blocks
    

def leftrotate(number, number_of_bits):
    string_binary_number = f"{number:0b}"
    string_to_tab=[]
    res=""
    for bit in string_binary_number:
        string_to_tab.append(bit)
    for i in range(number_of_bits):
        string_to_tab[len(string_to_tab)-1]=string_to_tab.pop(0)
    for bit in string_to_tab:
        res+= str(bit)
    return int(res, base=2)

def computing(blocks, a, b, c, d):
    """Needs to use 32-bits blocks in a big 512-bits one"""
    
    for i in range(64):
        if(i<=15 and i>=0):
            f = (b& c) | ((~b) & d)
            g= i
        elif(i<=31 and i>=16):
            f=(d & b) | ((~d) & c)
            g = (5*i + 1)%16
        elif(i<=47 and i>=32):
            f = b ^ c ^ d
            g = (3*i + 5)% 16
        elif(i<=48 and i<=63):
            f=c ^(b| (~d))
            g = (7*i)%16
        temp=d
        d=c
        c=b
        b=leftrotate((a+f+k[i]+int(blocks[g], base=2)), r[i]) +b

        a=temp
    return a, b, c, d
    
def iterating(blocks):
    a, b, c, d = producing_variables()
    for block in blocks:
        abis, bbis, cbis, dbis = computing(block, a, b, c, d)
        a= a + abis
        b = b + bbis
        c= c+cbis
        d= d+ dbis 
    return hex(a)[2:len(hex(a))] + hex(b)[2:len(hex(a))] + hex(c)[2:len(hex(a))] + hex(d)[2:len(hex(a))]    #slices used to avoid having 0x into the hash

def hashing(text):
    src = open(text,"r")
    length=0
    for carac in src.read():
        length+=1
    blocks = processing_input(text)
    append_length(length, blocks)
    big_blocks = cut_in_blocks(blocks)
    for i in range(len(big_blocks)):
        big_blocks[i]=cut_in_very_small_blocks(big_blocks[i])
    return iterating(big_blocks)

