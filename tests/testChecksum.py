import pytest
from CryptoRigolo.Checksum import *

def test_get_sum_known_text():
    content = "Hello"
    expected = (ord('H') + ord('e') + ord('l') + ord('l') + ord('o')) % 256

    file = open("input.txt","w", encoding="utf-8")
    file.write(content)
    file.close()
    result = get_sum("input.txt")
    assert result == expected

def test_get_sum_empty_file():
    file = open("empty.txt", "w",encoding="utf-8")
    file.write("")
    file.close()
    result = get_sum(str(file))
    assert result == 0

def test_checksum_identical_files():
    content = "Checksum Test 123!@#"
    file1 = open("file1.txt", "w", encoding="utf-8")
    file2 =  open("file2.txt", "w", encoding="utf-8")
    file1.write(content, encoding="utf-8")
    file2.write(content, encoding="utf-8")
    file1.close()
    file2.close()
    assert checksum(str(file1), str(file2)) is True

def test_checksum_different_files():
    file1 = open("file1.txt", "w", encoding="utf-8")
    file2 =  open("file2.txt", "w", encoding="utf-8")
    file1.write("abcd", encoding="utf-8")
    file2.write("abce", encoding="utf-8")
    file1.close()
    file2.close()
    assert checksum(str(file1), str(file2)) is False

def test_checksum_with_non_ascii():
    content = "éàçù"
    file1 = open("file1.txt", "w", encoding="utf-8")
    file2 =  open("file2.txt", "w", encoding="utf-8")
    file1.write(content, encoding="utf-8")
    file2.write(content, encoding="utf-8")
    file1.close()
    file2.close()
    
    assert checksum(str(file1), str(file2)) is True
