import os
import pytest
from math import floor, sin
from CryptoRigolo.MD5 import *


def test_constants_r_and_k():
    assert len(r) == 64
    assert len(k) == 64
    assert all(isinstance(x, int) for x in k)

test_constants_r_and_k()

def test_text_to_bits():
    
    file = open("input.txt","w", encoding="utf-8")
    file.write("a")
    file.close()
    bits, length = text_to_bits("input.txt")
    
    expected_bits = "1100001"
    expected_length = len(expected_bits)
    assert bits == expected_bits
    assert length == expected_length

test_text_to_bits()

def test_processing_input():

    file = open("input.txt","w", encoding="utf-8")
    file.write("a")
    file.close()
    initial_bits, init_length = text_to_bits("input.txt")
    padded_bits = processing_input("input.txt")
    padded_length = len(padded_bits)

    assert padded_length  % 512 == 0

    assert padded_bits.startswith(initial_bits)

    assert padded_bits[len(initial_bits)] == "1"

test_processing_input()

def test_append_length():

    bits = "1010" 
    initial_length = 7
    new_length = append_length(initial_length, bits)

    assert new_length == 7 + 3

test_append_length()



def test_cut_in_blocks():

    bits = "0" * 1024  
    blocks = cut_in_blocks(bits)
    assert len(blocks) == 2
    for block in blocks:
        assert len(block) == 512

test_cut_in_blocks()


def test_cut_in_very_small_blocks_exact():

    block = "0" * 64
    small_blocks = cut_in_very_small_blocks(block)
    assert len(small_blocks) == 2
    for part in small_blocks:
        assert len(part) == 32

test_cut_in_very_small_blocks_exact()

def test_cut_in_very_small_blocks_non_exact():
    block = "0" * 96
    small_blocks = cut_in_very_small_blocks(block)
    assert len(small_blocks) == 3
    for part in small_blocks:
        assert len(part) == 32
test_cut_in_very_small_blocks_non_exact()


def test_leftrotate_no_rotation():
    """
    Vérifie qu'aucune rotation (number_of_bits=0) ne modifie le nombre.
    Par exemple, leftrotate(9, 0) doit retourner 9.
    """
    assert leftrotate(9, 0) == 9

def test_leftrotate_one_rotation():

    assert leftrotate(9, 1) == 3

def test_leftrotate_two_rotations():

    assert leftrotate(9, 2) == 6

def test_leftrotate_three_rotations():

    assert leftrotate(9, 3) == 12

def test_leftrotate_full_rotation():

    assert leftrotate(9, 4) == 9

def test_leftrotate_with_single_bit():

    for n in range(10):
        assert leftrotate(1, n) == 1






def test_hashing():

    file_path = open("input.txt","w", encoding="utf-8") 
    file_path.write("abc")
    file_path.close()
    hash_str = hashing("input.txt")
    assert len(hash_str) > 0
    print(hash_str)
test_hashing()
