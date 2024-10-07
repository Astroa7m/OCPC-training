def tree(nodes):
    # if there is only one item then it is the root
    if len(nodes) == 1:
        return nodes[0]
    nodes_separated = [nodes[i:3 + i] for i in range(0, len(nodes), 3)]

    parents = []

    for children in nodes_separated:
        value = children[0] * 2 + children[1] + children[2] * 2
        parents.append(value)

    return tree(parents)




while True:
    leaves_str = input()
    if leaves_str == "0":
        break

    leaves = [int(i) for i in leaves_str.strip().split()]
    leaves.pop() # removing the last number that indicates the stop of children
    print(tree(leaves))