from graph import Graph
import sys
import os

if __name__ == "__main__" :
    filename = sys.argv[1]
    g = Graph(filename)
    edges = []
    for v in g.vertices():
        for w in g.adjacentTo(v):
            if v <= w:
                edges.append((v,w))
    name = filename.split('.')[0]
    filename = name + ".dot"
    with open(filename, 'w') as f:
        f.write("graph " + name + " {")
        for v,w in edges:
            f.write(f"\t{v} -- {w};")
        f.write("}")
    ext = "pdf"
    os.system(f"neato -o{name}.{ext} -T{ext} {name}.dot")
