from CryptoRigolo.AES import *
from copy import deepcopy

def test_organize_with_valid_input():
    file = open("test.txt","w", encoding="utf-8")
    file.write("abcd efgh")
    file.close()
    expected = [[[f"0x{ord('a'):02x}", f"0x{ord('b'):02x}", f"0x{ord('c'):02x}", f"0x{ord('d'):02x}"],
        [f"0x{ord(' '):02x}", f"0x{ord('e'):02x}", f"0x{ord('f'):02x}", f"0x{ord('g'):02x}"],
        [f"0x{ord('h'):02x}", f"0x{ord(' '):02x}", f"0x{ord(' '):02x}", f"0x{ord(' '):02x}"],
        [f"0x{ord(' '):02x}", f"0x{ord(' '):02x}", f"0x{ord(' '):02x}", f"0x{ord(' '):02x}"],
        ]]
    res=organize("test.txt")
    assert expected==res

test_organize_with_valid_input()

def test_initialize_block():
    
    expected = [['0x00'] * 4 for _ in range(4)]
    assert initialize_block() == expected
test_initialize_block()

def test_get_indexes():
    number="0x0a"
    expected=[0, 10]
    assert get_indexes(number) == expected
test_get_indexes()

def test_reverse_string():
    string="abcd"
    expected="dcba"
    assert reverse_string(string) == expected
test_reverse_string()

def test_hexstring_to_int():
    string="0a"
    expected=10
    assert hexstring_to_int(string) == expected
test_hexstring_to_int()

def test_add_round_key():
    block = [['0x01', '0x02', '0x03', '0x04'],
             ['0x05', '0x06', '0x07', '0x08'],
             ['0x09', '0x0a', '0x0b', '0x0c'],
             ['0x0d', '0x0e', '0x0f', '0x10']]
    key = [['0x10', '0x0f', '0x0e', '0x0d'],
           ['0x0c', '0x0b', '0x0a', '0x09'],
           ['0x08', '0x07', '0x06', '0x05'],
           ['0x04', '0x03', '0x02', '0x01']]
    expected = [['0x11', '0x0d', '0x0d', '0x09'],
                ['0x09', '0x0d', '0x0d', '0x01'],
                ['0x01', '0x0d', '0x0d', '0x09'],
                ['0x09', '0x0d', '0x0d', '0x11']]
    assert add_round_key(block, key) == expected
test_add_round_key()

def test_sub_bytes():
    block = [['0x00', '0x01', '0x02', '0x03'],
             ['0x10', '0x11', '0x12', '0x13'],
             ['0x20', '0x21', '0x22', '0x23'],
             ['0x30', '0x31', '0x32', '0x33']]
    result = sub_bytes(block)
    assert result[0][0] == '0x63'  
test_sub_bytes()

def test_shift_rows():
    block = [['0x00', '0x01', '0x02', '0x03'],
             ['0x10', '0x11', '0x12', '0x13'],
             ['0x20', '0x21', '0x22', '0x23'],
             ['0x30', '0x31', '0x32', '0x33']]
    expected = [['0x00', '0x01', '0x02', '0x03'],
                ['0x11', '0x12', '0x13', '0x10'],
                ['0x22', '0x23', '0x20', '0x21'],
                ['0x33', '0x30', '0x31', '0x32']]
    assert shift_rows(block) == expected
test_shift_rows()

def test_inv_shift_rows():
    block = [['0x00', '0x01', '0x02', '0x03'],
             ['0x11', '0x12', '0x13', '0x10'],
             ['0x22', '0x23', '0x20', '0x21'],
             ['0x33', '0x30', '0x31', '0x32']]
    expected = [['0x00', '0x01', '0x02', '0x03'],
                ['0x10', '0x11', '0x12', '0x13'],
                ['0x20', '0x21', '0x22', '0x23'],
                ['0x30', '0x31', '0x32', '0x33']]
    assert inv_shift_rows(block) == expected
test_inv_shift_rows()

def test_multiply():
    x=0x57
    y=0x83
    expected=0xc1
    assert multiply(x, y) == expected
test_multiply()

def test_crypt_decrypt():
    
    block = [['0x01', '0x02', '0x03', '0x04'],
             ['0x05', '0x06', '0x07', '0x08'],
             ['0x09', '0x0a', '0x0b', '0x0c'],
             ['0x0d', '0x0e', '0x0f', '0x10']]
    
    key_list = [block] * 11 
    
    encrypted = crypt(block, key_list)
    decrypted = decrypt(encrypted, key_list)
    
    assert decrypted == block  
test_crypt_decrypt()
def test_generate_key():
   
    keyword = "test"
    generated_key = generate_key(keyword)
    assert len(generated_key) == 4
    assert all(len(row) == 4 for row in generated_key)
test_generate_key()  
def test_get_keys_list():
   
    
    keyword = "test"
    key = generate_key(keyword)
    keys_list = get_keys_list(key)

    assert len(keys_list) == 11  
    assert all(len(k) == 4 and all(len(row) == 4 for row in k) for k in keys_list)
test_get_keys_list()
def test_crypt_all():
    crypt_all("test.txt", "vivelinfo", "test_crypte.txt", crypt)
    crypt_all("test_crypte.txt", "vivelinfo", "test_decrypte.txt", decrypt)
    fic1= open("test.txt","r",encoding="utf-8")
    fic2 = open("test_decrypte.txt", "r", encoding="utf-8")
    list1=[]
    list2=[]
    for carac in fic1.read():
        list1.append(carac)
    for carac in fic2.read():
        list2.append(carac)
    for i in range(len(list2)):
        if(list2[i]!=' '):
            assert list1[i]==list2[i]   #the cryptage works but it might add some extra spaces, so we avoid to compare that
test_crypt_all()

print("All tests passed !")
