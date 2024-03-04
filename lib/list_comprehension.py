#!/usr/bin/env python3

def return_evens(num_list):
    even_numbers= [n for n in num_list if n%2 == 0]
    return even_numbers
num_list=([0, 1, 3, 5, 7, 8, 9])
print(return_evens(num_list))

def make_exclamation(sentence_list):
    exclamation_list = [sentence + "!" for sentence in sentence_list]
    return exclamation_list
sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
print(make_exclamation(sentence_list))