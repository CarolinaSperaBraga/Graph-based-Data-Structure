#!/usr/bin/env python
# coding: utf-8

# In[52]:

# Cria a classe Node, com o vértice e o o vértice adjacente a ele
class Node(object):
    def __init__(self, vertice):
        self.vertice = vertice
        self.next = None

# Cria a classe Grafo, com a estrutura de uma Linked List
class Grafo(object):
    def __init__(self, vertices):
        self.V = vertices
        self.grafo =[None]*(self.V+1)
        
        
    # Define a função insere, que cria a adjacencia entre dois vértices
    def insere(self, v1, v2):
        node = Node(v2)
        # Para inserir a aresta no final da lista de arestas, primeiro checa se a lista é vazia
        temp = self.grafo[v1]
        if temp == None:
            self.grafo[v1] = node
        else:
            # Passa de item por item comparando para saber se a aresta já existe
            while temp: 
                if temp.vertice == v2:
                    print("aresta ja existe")
                    return
                # Mas sem perder o último item da lista
                if temp.next == None: break
                temp = temp.next
            temp.next = node
        
        # Semelhante ao v1 mas sem as comparações, pois já sabemos que a aresta não existe
        # Insere a adjacencia na lista de adjacencia de ambos os vértices, pois a lista é
        # não direcionada
        node = Node(v1)
        temp = self.grafo[v2]
        if temp == None:
            self.grafo[v2] = node
        else:
            while temp.next != None: temp = temp.next
            temp.next = node
        print("aresta inserida com sucesso")
         
            
    # Define a função vizinhos, que imprime as adjacencias de derterminado vértice
    def vizinhos(self, v):
        if v in range(1,self.V+1):
            # Uma string que concatena todas as arestas, impressa no final
            temp = self.grafo[v]
            s = str(v) + ": "
            while temp:
                s = s + str(temp.vertice) + " | "
                temp = temp.next
            print(s[:])  
        else:
            print("vertice nao existe")
    
    
    # Define a função imprime, que imprime o grafo como lista de adjacencia
    def imprime(self):
        for i in range(1,self.V+1):
            # Uma string que concatena todas as arestas, impressa no final
            s = str(i) + ":  "
            try:
                temp = self.grafo[i]
            except:
                continue
            while temp: 
                s = s + str(temp.vertice) + " | "
                temp = temp.next
            print(s[:])
    
    
    # Define a função remove, que remove uma aresta entre dois vértices       
    def remove(self, v1, v2):
        # Se a aresta for removida do primeiro vértice, ela existe e será removida do segundo
        if self.__remocao(v1, v2):
            self.__remocao(v2, v1)
            print("aresta removida com sucesso")
            return
        print("aresta nao existe")
    
    # Remoção de aresta de um único vértice em uma função privada
    def __remocao(self, v1, v2):
        temp = self.grafo[v1]
        # Se o vértice tem 0 arestas, não faz comparações
        if temp == None: return False
        # Se for a primeira aresta da lista, faz as adjacências começarem da aresta seguinte
        if temp.vertice == v2:
            self.grafo[v1] = temp.next
            return True
        temp2 = None
        # Passa de aresta por aresta, guardando a penúltima, se achar a aresta alvo,
        # a anterior referencia a seguinte do alvo como 'next'
        while temp:
            if temp.vertice == v2:
                temp2.next = temp.next
                return True
            temp2 = temp
            temp = temp.next
        return False
    
    
    # Cria a função adjacentes que diz se existe aresta entre dois vértices
    def adjacentes(self, v1, v2):
        # Passa de aresta por aresta nas adjacências do primeiro vértice procurando o segundo
        temp = self.grafo[v1]
        while temp:
            if temp.vertice == v2:
                print("sao adjacentes")
                return
            temp = temp.next
        print("nao sao adjacentes")



N = int(input()) # Indica o número de vértices do grafo
n = 0
l = []
# Inputs fornecidos pelo usuário
while n != "sair":
    n = input()
    l.append(n)  

g = Grafo(N)
# Leitura das operações a serem realizadas
for i in range(len(l)):
    if l[i] == "insere":
        vi = l[i+1].split()
        vi = [int(i) for i in vi]
        g.insere(vi[0],vi[1])   
    if l[i] == "remove":
        vr = l[i+1].split()
        vr = [int(i) for i in vr]
        g.remove(vr[0],vr[1])
    if l[i] == "adjacentes":
        va = l[i+1].split()
        va = [int(i) for i in va]
        g.adjacentes(va[0],va[1])
    if l[i] == "vizinhos":
        vv = int(l[i+1])
        g.vizinhos(vv)
    if l[i] == "imprime":
        g.imprime()

