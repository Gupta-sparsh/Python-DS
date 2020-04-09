# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:51:19 2020

@author: $parsh
"""
# tack Data Structure

class Stack():
    def __init__(self):
        self.items = []
        
    def push(self,item) :
        self.items.append(item)
        
    def pop(self) :
        return self.items.pop()
    
    def traverse(self):
        print(self.items)
        
    def is_empty(self) :
        print(self.items==[])
    
   
            
        

s = Stack()
s.push(1)
s.push(2)
s.push('a')
s.traverse()
s.pop()
s.traverse()

