#Ceasar Cypher - By Sean Foster


data = open("Mystery.txt", 'r')

def encrpyt():
    g =[data]
    key = 13
    for x in range(len(g)):
        if g[x].isupper():
            g[x] = chr(((ord(g[x]) - 65 - key) % 26) + 65)

    for x in range(len(g)):
        if g[x].islower():
            g[x] = chr(((ord(g[x]) - 65 - key) % 26) + 65)

def decrypt():
    g = list[data]
    key = 13
    for x in range(len(g())):
        if g[x].isupper():
            g[x] = chr(((ord(g[x])-65 + key)%26)+65)

    for x in range(len(g())):
        if g[x].islower():
            g[x] = chr(((ord(g[x]) - 65 + key) % 26) + 65)


def main():
    encrpyt()
main()