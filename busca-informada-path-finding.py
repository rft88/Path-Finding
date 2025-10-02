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

