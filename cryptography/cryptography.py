import nltk
import re
import random

from nltk.util import pr
nltk.download('words', quiet=True)
nltk.download('names', quiet=True)

from nltk.corpus import words, names
word_list = words.words()
name_list = names.words()

def encrypt(text,key):
    encrypted_text = ''
    # print (key)
    for i in text:
        # print(i)
        num = ord(i)
        # print(num)
        shifted_num = num + (key % 27)
        # print(shifted_num)
        shifted_text = chr(shifted_num)
        encrypted_text += shifted_text
        # print(encrypted_text)

    return encrypted_text


def decrypt(text,key):
    decrypted_text = ''
    # print (key)
    for i in text:
        # print(i)
        num = ord(i)
        # print(num)
        shifted_num = num - (key % 27)
        # print(shifted_num)
        shifted_text = chr(shifted_num)
        decrypted_text += shifted_text
        # print(decrypted_text)

    return decrypted_text


def crack(text):
    candidate_words = text.split()
    word_count = 0

    for i in candidate_words:
        word = re.sub(r'[^A-Za-z]+','', i)
        if word.lower() in word_list or word in name_list:
            word_count += 1
        else:
            pass
    return word_count


if __name__ == "__main__":

    pins = ["abcd","efgh"]
    
    for i in pins:
        key = random.randint(1, 26)
        print("plain pin", i)
        encrypted_pin = encrypt(i, key)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, key)
        print("decrypted_pin", decrypted_pin)

    candidates = ["a dark and stormy night","n qnex naq fgbezl avtug","j mjat jwm bcxavh wrpqc","call me Ishmael","Billy Pilgrim has become unstuck in time","All happy families are alike; each unhappy family is unhappy in its own way.",'"Where\'s Papa going with that ax?" said Fern to her mother as they were setting the table for breakfast.',"Off the hizzle fo shizzle",]
    for i in candidates:
        word_count = crack(i)
        percentage = int(word_count / len(i.split()) * 100)
        if percentage > 50:
            print(i, percentage)
