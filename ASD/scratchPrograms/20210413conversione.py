# Traccia 2021-04-13
def Algoritmo(T,k):
	start = True
	cT = T
	stT = stA = NULL
	while start or stT != NULL:
		if start:
			ret = NULL
			if cT != NULL :
				if cT -> key > k:
					# b = cT superflua posso ricavarla da cT
					push(stT, cT)
					cT = cT -> sx
					# start = True superfluo perchè start è gia True
				else if cT -> key < k:
					 # a = cT superflua posso ricavarla da cT
					 push(stT, cT)
					 cT = cT -> dx
			 	else: # T->key == k
			 		push(stT, cT)
			 		cT = cT -> sx
	 		else: # cT == NULL
	 			start = False
	 			last = cT	
		else: # !start
			cT = top(stT) # recupero il valore al top dello stack (ripristino il contesto) 
			if cT -> key > k: # torno da riga 5
				ret = BEST(ret, cT, k)
				pop(stT)
				last = cT
				# start = False
			else if cT -> key < k: # torno da riga 8
				ret = BEST(cT, ret, k)
				pop(stT)
				last = cT
				# start = False
			else: # ritorno da riga 10 o 11
				if cT -> dx != last: # sono in riga 10
					if cT -> dx == NULL: # ignoro la riga 11(è NULL)
						BEST(ret, NULL, k) # termino la chiamata
						pop(stT)
						last = cT
					else: # chiamata 11 da fare
						a = ret
						push(stA) # ho gia T sullo stack
						cT = cT -> dx
						start = True
				else: # 
					a = top(stA)
					ret = BEST(a, ret, k)
					pop(stT); pop(stA)
					last = cT
	return ret
