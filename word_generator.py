import random

vowels = "o i a e u"
consonants = "s n c p m r z l v j b d t h f Zh w y ng g"
diphthongs = "oo oi oa oe ou io ii ia iu eo aa au eo ee eu uo ui ua ue uu"
consonant_digraphs = "ch sh th"

V = vowels.split()
C = consonants.split()
D = diphthongs.split()
G = consonant_digraphs.split()

for i in range(100):
  word = ""

  if random.randrange(100) < 50:
    word += random.choice(V)
  else:
    word += random.choice(D)

  if random.randrange(100) < 50:
    word += random.choice(C)

  if random.randrange(100) < 30:
    word += random.choice(D)
  else:
    word += random.choice(C)

  if random.randrange(100) < 50:
    word += random.choice(C)

  print(word)
