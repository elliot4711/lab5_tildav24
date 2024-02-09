from bintreeFile import Bintree
from LinkedQfile import LinkedQ
svenska = Bintree()

class ParentNode:
    def __init__(self, word, parent = None):
        self.word = word
        self.parent = parent
    
    def writechain(self):
        skriv(self)

class SolutionFound(Exception):
    pass

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()
        svenska.put(ordet)      

startord = input("Skriv in ditt startord: ")
slutord = input("Skriv in ditt slutord: ")

startordsnode = ParentNode(startord)

gamla = Bintree()
queue = LinkedQ()
queue.enqueue(startordsnode)

alphabet = ["a", "b", "c", "d", "e","f","g","h","i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v","w","x","y","z", "å","ä", "ö"]

def skriv(node):
    print(node.word)
    print(node.parent)
    while node.parent is not None:
        skriv(node.parent)


def makechildren(startordsnode, slutord, queue):
    gamla.put(startordsnode.word)
    original = startordsnode

    for i in range(len(startordsnode.word)):
        startord = list(original.word)
        for j in range(len(alphabet)):
            startord[i] = alphabet[j]
            ord1 = startord[0] + startord[1] + startord[2]
            if ord1 in svenska:
                if ord1 not in gamla: 
                    ordnod= ParentNode(ord1, startordsnode)
                    queue.enqueue(ordnod)
                    gamla.put(ord1)
                    if ord1 == slutord:
                        print(ord1)
                        ordnod.writechain()
                        raise SolutionFound

try:
    makechildren(startordsnode, slutord, queue)
    while not queue.isEmpty():
        nod = queue.dequeue()
        makechildren(nod, slutord, queue) 
except:
    print("No solution found")