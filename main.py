from bintreeFile import Bintree
from LinkedQfile import LinkedQ
svenska = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        svenska.put(ordet)      

startord = input("Skriv in ditt startord: ")
slutord = input("Skriv in ditt slutord: ")

gamla = Bintree()
q = LinkedQ()

alphabet = ["a", "b", "c", "d", "e","f","g","h","i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z", "å","ä", "ö"]

foundPath = False

def makechildren(startord, slutord, q):
    gamla.put(startord)
    original = startord
    for i in range(len(startord)):
        startord = list(original)
        for j in range(len(alphabet)):
            startord[i] = alphabet[j]
            ord1 = startord[0] + startord[1] + startord[2]
            if ord1 in svenska:
                if ord1 not in gamla: 
                    q.enqueue(ord1)
                    gamla.put(ord1)
                    if ord1 == slutord:
                        print("Det finns en väg till", slutord) 
                        global foundPath
                        foundPath = True

    

makechildren(startord, slutord, q)
while not q.isEmpty():
    nod = q.dequeue()
    makechildren(nod, slutord, q)
if foundPath == False:
    print("Ingen väg hittades")