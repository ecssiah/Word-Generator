# -*- coding: utf-8 -*-

import random

vowels = "o oo i ii a aa e ee u uu"
consonants = "s n c p m r z l v j b d t h f ʒ w y ŋ g"
vowel_digraphs = "oi oa oe ou io ia iu eo au eo eu uo ui ua ue"
consonant_digraphs = "ch sh th"

V = vowels.split()
C = consonants.split()
VD = vowel_digraphs.split()
CD = consonant_digraphs.split()

for i in range(40):
    word = ""

    if random.randrange(2) == 0:
        if random.randrange(2) == 0:
            word += random.choice(VD)
        else:
            word += random.choice(V)

        if random.randrange(10) == 0:
            word += random.choice(CD)
        else:
            word += random.choice(C)

        if random.randrange(2) == 0:
            word += random.choice(V)
    else:
        if random.randrange(2) == 0:
            word += random.choice(CD)
        else:
            word += random.choice(C)
        
        if random.randrange(10) == 0:
            word += random.choice(VD)
        else:
            word += random.choice(V)

        if random.randrange(2) == 0:
            word += random.choice(C)

    print(word)
