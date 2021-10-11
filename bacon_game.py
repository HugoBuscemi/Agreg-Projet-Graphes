from graph import Graph
import sys
from time import sleep

kb = "Bacon, Kevin"

def find_bacon_number(g, main_actor):
    next_actors = [kb] # Prochain acteur à distance de KB
    distance = 0 # Futur bacon number
    predecessor = {} # dictionnaire de qui a joué avec qui au plus proche de KB
    predecessor[kb]  =  (kb,None) # KB est le plus proche de lui même
    
    while next_actors != []: #Tant qu'il rest des acteurs à voir
        
        current_actors = []
        for next_actor in next_actors: #Pour chaque acteur à voir
            
            if next_actor == main_actor: # Si c'est le bon on peut retourner
                
                return distance, predecessor
            
            else: # Sinon
                
                movies = g.adjacentTo(next_actor) # Films dans lequels l'acteur a joué
                
                for movie in movies: # pour chacun des films
                    
                    for actor in g.adjacentTo(movie): #pour chaque acteur ayant joué dans le film
                        
                        if not(actor in predecessor.keys()): # Si l'acteur n'a pas déjà été vu (donc n'a pas de prédécesseur)
                            
                            predecessor[actor] = (next_actor, movie) # On rajoute sa precedance
                            current_actors.append(actor) # On le regardera ensuite
                            
        next_actors = current_actors.copy() # On remet à jour la liste nes nouveaux acteurs à voir
        distance += 1
    return float('inf'),{}

if __name__ == "__main__" :
    main_actor = sys.argv[1]
    g = Graph("movies.txt", '/')
    distance, predecessor = find_bacon_number(g, main_actor)
    print("distance = ",distance)
    actor = main_actor
    while actor != kb:
        next_actor, movie = predecessor[actor]
        print(actor, " has played with ", next_actor, " in ", movie)
        actor = next_actor
    
