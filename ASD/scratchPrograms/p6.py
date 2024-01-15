# Dato un grafo G e due vertici u, v e un insieme A \subseteq V, scrivere un algortimo che dato in ingresso il grafo, i due verticie e A,
# colcoli l'insieme z tale che z \in Z se e solo se:
# - z \in A, ovvero Z \subseteq A
# - Ogni percorso che parte da u raggiunge v non passa per z

def Algo(G, u, v, A):
    Z = A
    Init(G) # tutti i colori a bianco tranne z colorato a nero
    color1 = DFS_Visit(G, u)
    color2 = DFS_Vsit(G_t, v)
    for z in Z:
        if color1[z] == N && color2[z] == N:
            Z.remove(z)
    return Z



