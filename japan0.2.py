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

alphabet = input("(K) Katakana or (H) hiragana or (B) Both? ").lower()
from_level = int(input("From level (input number in range 1-10): ")) - 1
to_level = int(input("To level (input number in range 1-10: ")) - 1

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
 if (alphabet=="k"):
  the_pos = to_dict(romaji, katakanaa)
 elif (alphabet=="h"):
  the_pos = to_dict(romaji, hiraganaa)
 else:
  romaji.extend(romaji)
  hiraganaa.extend(katakanaa)
  the_pos = to_dict(romaji, hiraganaa)

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
  jawab += "SALAH"
def get_input():
 global jawab
 global ansask
 x = input("\n%s : "%(ansask[1]))
 if (x==""):
  jawab+="SALAH"
 jawab += x

ber_det = int(input("Berapa detik: "))
def game():
 global jawab
 global ansask
 global level
 ansask[0], ansask[1] = the_pos[random.randrange(0, len(the_pos))]
 a = Thread(target=tunggu, args=[ber_det]).start()
 Thread(target=get_input, args=[]).start()
 while (jawab==""):
  pass
 to_return = True
 if (jawab==ansask[0]):
  print("Benar")
  to_return = True
 else:
  print("Salah, %s. tekan Enter untuk lanjut"%(ansask[0]) )
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
