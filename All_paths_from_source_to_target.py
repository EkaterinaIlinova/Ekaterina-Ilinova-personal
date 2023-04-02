# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 13:53:57 2022

@author: Ekaterina Ilinova
"""
#For a given DAG with n nodes labeled from 0 to n - 1, find all feasible paths from node 0 to node n - 1.

#The graph is represented as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
       
        n=len(graph)
        self.paths=[]
        self.target=len(graph)-1
        
        def backtrack(current, path):
            if current==self.target:
                self.paths.append(list(path))
                
            else:
                for nextnode in graph[current]:
                    path.append(nextnode)
                    backtrack(nextnode,path)
                    path.pop()
        
        backtrack(0,[0])
        return self.paths
        