#ada bugs, kalo waktu habis, si thread get_input ga destroy. trus minta enter

#v 0.2
#!/usr/bin/python
import random, os
from threading import Thread
import time
import sys
import math

hiraganaa,katakanaa, romaji = [1, 1, 1]
with open("hiragana", "r") as reader:
 hiraganaa = reader.read().split(",")
with open("katakana", "r") as reader:
 katakanaa = reader.read().split(", ")
with open("romaji", "r") as reader:
 romaji = reader.read().split(", ")

#alphabet = input("(K) Katakana or (H) hiragana or (B) Both? ").lower()
from_level = 0
to_level = 10

the_level = int(input("""Welcome to japan training game v 0.3.\n by Kevin Agusto

please select the level by the number and hit enter
1.hiragana single alphabet
2.katakana single alphabet
3.hiragana and katakana single alphabet
4.hiragana sentence
5.katakana sentence
6.hiragana and katakana sentence

the level: """))


waktu = []
for i in range(2, 11):
 waktu.append(i)
 waktu.append(i)



def to_dict(list0, list1):
 if ((len(list0))!=(len(list1))):
  raise ValueError("The length of list0 and list 1 is not the same")
 to_return = []
 list00 = []
 list11 = []
 for i in range(len(list0)):
  for a in list0[i].split(" "):
   if (a!=""):
    list00.append(a)
  for b in list1[i].split(" "):
   if (b!=""):
    list11.append(b)

 for i in range(len(list00)):
  to_return .append([list00[i], list11[i]])
 return to_return


romaji = romaji[from_level: to_level+1]
katakanaa = katakanaa[from_level: to_level+1]
hiraganaa = hiraganaa[from_level: to_level+1]

if True:
 jawab = ""
 the_pos = {}
 if ((the_level==1)|(the_level==4)):
  the_pos = to_dict(romaji, hiraganaa)
 elif ((the_level==2)|(the_level==5)):
  the_pos = to_dict(romaji, katakanaa)
 elif ((the_level==3)|(the_level==6)):
  romaji.extend(romaji)
  hiraganaa.extend(katakanaa)
  the_pos = to_dict(romaji, hiraganaa)
 else:
  print("Invalid level")
  exit(0)


ansask = ["", ""]
jawab = ""
level = 1
def tunggu(sec):
 global jawab
 global level
 cur_level = level
 sec = int(math.floor(sec))
 det = 0
 habis = True
 while (sec>=det):
  if (jawab!=""):
   habis = False
   break
  time.sleep(0.1)
  det+=0.1
 if (habis& (level==cur_level)):
  jawab += "WRONG"

def get_input():
 global jawab
 global ansask
 try:
  x = input("\n%s : "%(ansask[1]))
 except KeyboardInterrupt:
  exit(0)
 if (x==""):
  jawab+="WRONG"
 jawab += x

ber_det = int(input("Seconds per level: "))
def game():
 global jawab
 global ansask
 global level
 if ((the_level>3)):
  temp0 = ""
  temp1 = ""
  for i in range(random.randrange(1, 5)):
   charcount = random.randrange(3, 6)
   for a in range(charcount):
    ran = the_pos[random.randrange(0, len(the_pos))]
    temp0+=ran[0]
    temp1+=ran[1]
   temp0+=" "
   temp1+=" "
  ansask[0] = temp0
  ansask[1] = temp1 
 else:
  ansask[0], ansask[1] = the_pos[random.randrange(0, len(the_pos))]

 ansask[0] = ansask[0].rstrip(" ")
 ansask[1] = ansask[1].rstrip(" ")
 a = Thread(target=tunggu, args=[ber_det]).start()
 Thread(target=get_input, args=[]).start()
 while (jawab==""):
  pass
 to_return = True
 if (jawab==ansask[0]):
  print("CORRECT")
  to_return = True
 else:
  print("\nWRONG, %s. press enter to continue"%(ansask[0]) )
  input()
  to_return = False
 jawab = ""
 level += 1
 return to_return 

sudah = False
while (True):
 try:
  print("Level %d\n\n\n" %(level))
  if (not(sudah)):
   for i in list(range(1, 4))[::-1]:
    print(i)
    time.sleep(1)
   print("\n\n")
   sudah = True

  game()
  print("\n\n")
 except KeyboardInterrupt:
  exit(0);
