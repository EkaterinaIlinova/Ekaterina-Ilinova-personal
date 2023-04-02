# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 14:24:22 2022

@author: Ekaterina Ilinova
"""
#Convert Binary Search Tree to Sorted Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
    
        def helper(node):
            nonlocal last, first
            
            if node:
                helper(node.left)
                
                if last:
                    last.right=node
                    node.left=last
                else:
                    first=node
                last=node
                helper(node.right)
            
            
       
        
        if not root:
            return None
        
        last, first=None,None
        
        helper(root)
        
        last.right=first
        first.left=last
        return first