from graph import Graph
import sys
import os


def parcours(g, v, results, date):
    results[v][0][0] = date
    date += 1
    for w in g.adjacentTo(v):
        if results[w][0][0] == None:
            results[v][1].append(w)
            date = parcours(g,w,results,date)
        else:
            results[v][2].append(w)
    results[v][0][1] = date
    date += 1
    return date
            

def start_end_dates(g):
    vertices = g.vertices()
    results = {}
    for v in vertices:
        results[v] = ([None,None],[],[])
    date = 0
    for v in vertices:
        if results[v][0][0] == None:
            date = parcours(g, v, results, date)
    return results

def dot(dates_n_tree, name):
    filename = name + ".dot"
    with open(filename, 'w') as f:
        f.write("digraph " + name + " {")
        for v in dates_n_tree.keys():
            start_date, end_date = dates_n_tree[v][0]
            f.write(f"\t{v} [ label=\"{start_date}/{end_date}\"];\n")
            for w in dates_n_tree[v][1]:
                f.write(f"\t{v} -> {w}[ penwidth=4];\n")
            for w in dates_n_tree[v][2]:
                f.write(f"\t{v} -> {w}[];\n")
        f.write("}")
    ext = "pdf"
    os.system(f"neato -o{name}.{ext} -T{ext} {name}.dot")

if __name__ == "__main__" :

    filename = sys.argv[1]
    g = Graph(filename)
    dates_n_tree = start_end_dates(g)
    name = filename.split('.')[0]+"_2"
    dot(dates_n_tree, name)
    
