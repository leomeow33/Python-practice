class BinTNode:
    def __init__(self, dat, left = None, right = None):
        self.data = dat
        self.left = left
        self.right = right
def pre_order(t):
    if t is None:
        return
    proc(t.data)
    pre_order(t.left)
    pre_order(t.right)

def level_order(t):
     if t == None:
        return
     lst = []
     lst.append(t)
     print(lst)
     while lst:
         current=lst.pop(0)
         print(current.data)
         if current.left!=None:
            lst.append(current.left)
         if current.right!=None:
             lst.append(current.right)
def proc(x):
    print(x, end = '')
t = BinTNode(1, BinTNode(2, BinTNode(4), BinTNode(5)), BinTNode(3, BinTNode(6), BinTNode(7)))
level_order(t)

