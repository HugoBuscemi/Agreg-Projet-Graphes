from graph import Graph
import sys

if __name__ == "__main__" :
    filename = "movies.txt"
    actor = sys.argv[1]
    g = Graph(filename, '/')
    for film in g.adjacentTo(actor):
        print(film)
