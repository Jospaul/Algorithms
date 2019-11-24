class node:
    value = 0
    right = ''
    left = ''

    def __init__(self):
        self.value=0
        self.right = None
        self.left = None


class tree:
    treeval = [[20,50,True],[16,50,False],[13,20,True],[11,20,False],[9,16,True],[7,16,False]]
    mytree = node()
    for val in treeval:
        trnode = node()
        trnode.value = val[1]
        if not val[2]:
            trnode.right = node()
            trnode.right.value = val[0]
        else:
            trnode.left = node()
            trnode.left.value = val[0]

        if mytree.right is None and mytree.left is None:
            mytree = trnode
        elif mytree.right is None:
            if mytree.value == trnode.value:
                mytree.right = trnode
        else:
            mytree.left = trnode
