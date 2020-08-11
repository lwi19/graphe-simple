# GRAPH-SIMPLE


# Introduction

Ce programme explore différents graphes simples construits soit par table, soit par fonction.
Détermine les composantes connexes et calcule le plus court chemin entre deux sommets pris au hasard.

Ne tient compte que des graphes simples non-orientés.

Le calcul du plus court chemin est très performant pour le graphe aléatoire g_06
exemple: pour un graphe de 5 millions de sommets et 15 millions d'arrêtes aléatoires, le calcul prend moins de trois minutes.

Il est possible de fixer le générateur de nombres aléatoires pour avoir toujours le même graphe avec la fonction 
seed(n) où n est un nombre entier.


# Utilisation
python3.8 graph-simple.py

La commande chmod +x graphe-simple.py permet d'exécuter directement le programme en terminal


# Tests
python3 -m unittest discover  -p "*test.py" -s ./tests -v


# Results 
Graph name:       G_06 - Random graph\
This graph is undirected, not connected\
have 500_000 vertices, 999_996 edge(s) and 9_588 component(s)  

Bunches | Vertices by bunch
--- | ---
9_215      |    1
344        |    2
27         |    3
1          |    4
1          |    490_012


Shortest path from 330982 to 217306 in graph G_06 is length : 10  
path=[330982, 53551, 173147, 164415, 352668, 461480, 313891, 38808, 406201, 120078, 217306]





# Fichiers
Fichiers | Desc
--- | ---
graphe-simple.py | Programme principal
./util/graph_lib.py | Librairie de fonctions
./data/some_of_them.py | Quelques examples de graphes en tableau et en fonction
./test/graphe_test.py | Utilisé avec Unittest
Readme.FR.md | Ce fichier            
Readme.md | This file in English
  
#  Exigences (requirements)
1. Python >=3.8
1. (optionel) Le programme externe CProfileV: pip install CProfileV



# Profilage et trace
python3 -m unittest discover  -p "*test.py" -s ./tests -v  
Testeras les graphes selon le module graph_test.py  
Note: Les valeurs très élevées prennent plus de temps à calculer

python3 -m trace --count -C ./cover/ graphe-simple.py  
Produira un trace du nombre d'appels pour toutes les fonctions

python3.8 -m trace --trace -C ./cover/ --timing Graphes.py  
Produira une trace en fonction du temps d'exécution pour chaque appel de fonctions   

(optionel)  
La commande python3.8 -m cProfile -o output.prf ./graphe-simple.py  
suivi de cprofilev -f output.prf  
Donnera un résultat à l'adresse: http:/127.0.0.4:4000  




# Liens utiles
[Lexique de la théorie des graphes (wikipedia)](https://fr.wikipedia.org/wiki/Lexique_de_la_th%C3%A9orie_des_graphes)

[Quelques définitions](https://www.momirandum.com/graphes/theorie-des-graphes/Connexite.html)

[Introduction à l'algorithme A*](https://www.redblobgames.com/pathfinding/a-star/introduction.html#breadth-first-search)  

[Profilage de fonctions avec cprofilev](https://github.com/ymichael/cprofilev)  
  



#  TODO / DONE 

- [ ] Créer la matrice d"adjacence
- [ ] Créer la matrice d"incidence
- [ ] Graphe dual 
- [ ] Diamètre du graphe   
- [ ] Fonction  is_isomorphic(graph1, graph2)
- [ ] Fonction is_eulerian()
- [ ] function is_hamiltonian()
- [ ] Fonction is_planar() 
- [ ] Better presentation of com 
- [ ] Trouve les chaines possibles  (existe ?, la plus courte) entre deux sommets.
- [ ] DFS est bien mais pas du tout rapide comparé à BFS
- [ ] Chaque arête a un poids de '1' qui n'est pas utilisé mais pourrait l'être éventuellement


Place maintenant à l'amélioration et à vos commentaires!






