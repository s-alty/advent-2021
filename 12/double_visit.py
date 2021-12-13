import sys

found_paths = []

class Node:
    def __init__(self, label):
        self.label = label
        self.edges = set()

def build_graph(lines):
    nodes = {}
    for line in lines:
        first, second = line.strip().split('-')

        first_node = nodes.get(first, Node(first))
        second_node = nodes.get(second, Node(second))
        first_node.edges.add(second)
        second_node.edges.add(first)
        nodes[first] = first_node
        nodes[second] = second_node
    return nodes

def can_visit(label, path):
    if label == 'start' or label == 'end':
        return label not in path

    if label.isupper():
        return True

    if label not in path:
        return True

    # we can visit a single small cave twice
    small_cave_visits = [p for p in path if not p.isupper()]
    return len(small_cave_visits) == len(set(small_cave_visits))

def paths(graph, current, path):
    path = path + [current.label]

    if current.label == 'end':
        found_paths.append(path)
        return

    # we can visit any upper case edge or any lower case edge that hasn't been visited

    possibilities = [l for l in current.edges if can_visit(l, path)]
    for p in possibilities:
         paths(graph, graph[p], path)


if __name__ == '__main__':
    graph = build_graph(sys.stdin)
    paths(graph, graph['start'], [])
    print(len(found_paths))
