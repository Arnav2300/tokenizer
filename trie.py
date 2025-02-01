MAX_CHAR=26
class Trie:
    def __init__(self):
        self.cnt=0
        self.node=[None for i in range(MAX_CHAR)]

def insert(root,s):
    temp=root
    n=len(s)
    for i in range(n):
        index=ord(s[i])-ord('a')
        if (not root.node[index]):
            root.node[index]=Trie()
        root=root.node[index]
    root.cnt+=1
    return temp

def search(root,s):
    