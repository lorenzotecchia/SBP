#Si scriva un algoritmo che, dati in ingresso un grafo G= (V, E), rappresentato per mezzo di una lista di adiacenza,
# un array Adi dimensione k ≤ V| I, tale che A[i] appartenente a V per ogni i € {O,., k}, e due vertici v, w € V,
#calcoli ni tempo lineare l'insieme dei vertici Z contenuto in V contenente tutti esoli quei vertici di A che soddisfano al seguente condizione:
#z appartenente a Z se e solo se tutti i percorsi in G che partono da ve terminano in w e non passano per z. 
#Successivamente, si analizzi li tempo di esecuzione dell'algoritmo proposto.

# dobbiamo verificare che esiste un percorso che non verifica la condizione: esiste un percorso in G che parte da v e termina in w passando per z.
# Due DFS: una per verificare che z è raggiungibile da v, e una sul grafo traposto per vedere se w è raggiungibile da z.
# Usiamo due array di colori: se un nodo è nero in entrambi ed appartiene ad A, allora quel nodo non va inserito nell'insieme Z.

def Algo(G, A, v, w):

	Z =	NULL
	Init(G)
	Init(G_t)

	G_t = GrafoTrasposto(G)

	color1 = DFS_Visit(G,v)
	color2 = DFS_Visit(G_t, w)

	for z in A:
		if color1[z] != color2[z]:
			Z.append(z)   # inserisce alla fine della lista/ array il vertice
	return Z


def Init(G):
	for v in V:
		color[v] = b


def DFS_Visit(G,v):
	color[v] = g
	for w in Adj[v]:
		if color[w] == b:
			color = DFS_visit(G,w)
	color[v] = n 
	return color

def GrafoTrasposto(G): 
	V_t = V
	for v in V_t:
		for w in Adj[v]:
			E_t = Insert(E_t,(w,v))
	return G_t
