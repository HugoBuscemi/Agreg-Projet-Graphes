from graph import Graph
import sys
import os


def parcours(g, v, results, date):
    results[0][v][0] = date
    date += 1
    for w in g.adjacentTo(v):
        if results[0][w][0] == None:
            results[1].append((v,w))
            date = parcours(g,w,results,date)
        else:
            results[2].append((v,w))
    results[0][v][1] = date
    date += 1
    return date
            

def start_end_dates(g):
    vertices = g.vertices()
    results = {},[],[]
    for v in vertices:
        results[0][v] = [None,None]
    date = 0
    for v in vertices:
        if results[0][v][0] == None:
            date = parcours(g, v, results, date)
    return results


if __name__ == "__main__" :

    filename = sys.argv[1]
    g = Graph(filename)
    labels, boldedges, normaledges = start_end_dates(g)
    for v in labels.keys():
        start,end = labels[v]
        labels[v] = f"\"{start}/{end}\""
    name = filename.split('.')[0]+"_2"
    g.dot(name, boldedges, normaledges, labels)
    
