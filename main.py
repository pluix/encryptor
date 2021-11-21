import key_gen

key_gen.key()
main_key = key_gen.get_json(key_gen.key_fp)


# # Encrypts a given string based off of the given key dictionary
def encrypt(string, key):
    encryption = ""

    for x in string:
        encryption += key[x]

    return encryption


# # Decodes the encryption by reversing encrypt() based off of the given key dictionary
def decrypt(string, key):
    # decryption = ""
    swap_key = {y:x for x,y in key.items()}

    return encrypt(string, swap_key)


string = "The quick brown fox jumps over the lazy dog."
print(string)

encryption = encrypt(string, main_key)
print(encryption)

decryption = decrypt(encryption, main_key)
print(f"{decryption}\n")
