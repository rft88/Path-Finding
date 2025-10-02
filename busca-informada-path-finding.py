# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 17:51:32 2016

@author: Rodrigo
"""

#1 funcao teste objetivo

if self.problem.ObjectiveTest(current,target) == True:
                #if true, finish serach
    solution = True
    
            
#funcao sucessor

print("Visiting %r" % current)
            #expand new candidate solutions from current 
new_solutions = self.problem.ExpandSolution(current)
            
#funcao heuristica
            
for next_item in new_solutions:
                #check if each expanded solution was already visited
    if next_item not in came_from:
                    #if not, evaluate the associated heuristic
        priority = self.problem.Heuristic(target,next)
                    # and add to the priority queue for evaluation
        frontier.put(next_item,priority)
        came_from[next_item] = current
                    
#2
#funcao teste objetivo
                    
def ObjectiveTest(self,current,target): 
        """Return ``True`` if ``current`` state corresponds to the ``target`` state 
        """ 
        solution = False 
        if current == target:
            solution = True
        return  solution
        
#retorna verdadeiro caso o estado atual seja igual ao estado objetivo

#funcao sucessor
def ExpandSolution(self,current): 
        """Returns all possible states from ``current`` 
        """ 
        return  self.problem.neighbors(current)
        
#expande as solucoes a partir do estado atual
    
    
#funcao heuristica    
    
def Heuristic(self,target,current): 
        """Returns all possible states from ``current`` 
        """ 
        return  self.problem.get_edge_data(current, target)
        
        
#estima o custo do menor caminho do estado atual até o estado final mais próximo;

"""
#3
#o algoritmo parte de ouro fino e verifica se o mesmo eh o estado objetivo utilizando a funcao teste objetivo.
como o objetivo eh verginha, o algoritmo utiliza do algoritmo GreedySearch para escolher o caminho de menor custo que leva ao proximo no, que 
no caso eh congonhal.
a partir de congonhal, o mesmo processo eh repetido ate que o estado objetivo seja encontrado.

#4
a.
De Ouro Fino para Pouso Alegre, a funcao ExpandSolution expande os possiveis nós, e encontra somente Congonhal. O mesmo processo acontece no nó Congonhal,
que está conectado ao nó Pouso Alegre, que é o estado objetivo. Como o estado objetivo foi encontrado, a a busca é encerrada.

b.
partindo de ouro fino para campinas: 8 estados (todos) foram visitados, mas o nó Campinas não foi encontrado, pois não foi definido como um nó existente.

Comparação: no primeiro caso, apos os possiveis caminhos foram expandidos e a verificacao pode encontrar o estado objetivo depois de duas buscas.
Ja no segundo caso, a busca foi efetuada por todos os nós, porém o estado objetivo não foi encontrado, pois Campinas não foi definido como um nó.

#5
a.
Uma busca heurística é uma busca que utiliza uma função h(n) que, para cada nó n do espaço de busca, dá uma avaliação do custo para atingir o estado final.
Partindo de Ouro Fino para Pouso Alegre, o unico estado a ser expandido inicialmente é Congonhal, mas caso existissem outros estados conectados a Ouro Fino,
o algoritmo deveria fazer a busca primeiramente no nó com menor custo. O mesmo acontece saindo do proximo nó (Congonhal), onde o único nó subsequente é
Pouso Alegre (estado objetivo).

b.
PathFinfWithCostExample: A resposta dessa questao segue a mesma linha de raciocinio da letra a., porem o estado objetivo nao pode ser encontrado, por não ser um nó existente.
Sendo assim, o caminho não pode ser encontrado, mesmo percorrendo todos os nós com seus respectivos custos. 8 estados foram visitados (todos).

PathFindExample: 8 estados foram visitados, e o estado final não foi encontrado. Porém, a sequencia dos estados visitados foi um pouco diferente,
devido aos diferentes algoritmos de busca utilizados por cada algoritmo. Um usa heurística e o outro não.
"""