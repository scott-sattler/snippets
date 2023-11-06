
class Node:
    def __init__(self, val=None, right=None):
        self.val = val
        self.right = right


head = Node()
head.right = Node(1)
head.right.right = Node(2)
head.right.right.right = Node(3)
size = 3  # structures such as LRU Cache have len(map)

node = head
oof = [[node := node.right, node.val][1:] for _ in range(size)]

print(oof)


# no size compensation
node = head
ite = [0]
owie = [[node := node.right, (ite.append(_) if node.right else _), node.val][2:] for _ in ite]

print(owie)
