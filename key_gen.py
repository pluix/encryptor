import json
import random
import os

key_fp = "key.json"
chars_fp = "characters.json"


def get_json(fp):
    with open(fp, "r") as file:
        json_file = json.load(file)
    file.close()
    return json_file


# # Creates an encryption key by pairing a list of characters to a randomized version of said list
def new_key():
    characters = get_json(chars_fp)
    y = []
    key = {}

    for x in characters:
        y.append(x)

    random.shuffle(y)

    for z in range(0, len(characters)):
        key[characters[z]] = y[z]

    with open(key_fp, "w", encoding='utf-8') as file:
        # json_file = json.dumps(key)
        json.dump(key, file, ensure_ascii=False, indent=4)
    file.close()

    print("Made key.")
    print(f"Key: {key}\n")

    return key


# # Creates new or returns current key
def key():
    if os.path.exists(key_fp):
        make = input("Key exists. Make new key? (y/n) ")
        if make.lower() == "y":
            new_key()
        else:
            print(f"Key: {get_json(key_fp)}\n")
    else:
        new_key()
