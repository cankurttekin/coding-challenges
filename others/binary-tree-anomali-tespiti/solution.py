def search_anomaly(node, parent, visited):
  if not node:
    return False
  if node in visited:
    return True
  visited.add(node)

  l_branch = search_anomaly(node.left, node, visited)
  r_branch = search_anomaly(node.right, node, visited)

  return l_branch or r_branch

def test_search_anomaly():
    class Node:
        def __init__(self, value = None):
            self.left  = None
            self.right = None
            #self.value = None

    n1 = Node()
    n2 = Node()
    n3 = Node()
    n4 = Node()
    n5 = Node()
    n6 = Node()
    n7 = Node()
    n8 = Node("test")
    n9 = Node()
    n1.left  = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n7.left = n8
    n8.left = n5

    print("n1 = root\n"+
    "n1.left  = n2\n"
    "n1.right = n3\n\n"+
    "n2.left = n4\n"+
    "n2.right = n5\n\n"+
    "n3.left = n6\n"+
    "n3.right = n7\n\n"+
    "n7.left = n8\n\n"+
    "!!n8.left = n5\n")
    print(search_anomaly(n1, None, visited = set()))
test_search_anomaly()
