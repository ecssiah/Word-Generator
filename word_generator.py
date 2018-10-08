# -*- coding: utf-8 -*-

import random

vowel_list = "o oo i ii a aa e ee u uu"
consonant_list = "s n c p m r z l v j b d t h f ʒ w y ŋ g"
vowel_digraph_list = "oi oa oe ou io ia iu eo au eo eu uo ui ua ue"
consonant_digraph_list = "ch sh th"

vowels = vowel_list.split()
consonants = consonant_list.split()
vowel_digraphs = vowel_digraph_list.split()
consonant_digraphs = consonant_digraph_list.split()

for i in range(40):
    word = ""

    if random.randrange(2) == 0:
        if random.randrange(2) == 0:
            word += random.choice(vowel_digraphs)
        else:
            word += random.choice(vowels)

        if random.randrange(10) == 0:
            word += random.choice(consonant_digraphs)
        else:
            word += random.choice(consonants)

        if random.randrange(2) == 0:
            word += random.choice(vowels)
    else:
        if random.randrange(2) == 0:
            word += random.choice(consonant_digraphs)
        else:
            word += random.choice(consonants)
        
        if random.randrange(10) == 0:
            word += random.choice(vowel_digraphs)
        else:
            word += random.choice(vowels)

        if random.randrange(2) == 0:
            word += random.choice(consonants)

    print(word)
