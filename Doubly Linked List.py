# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:10:10 2020
@author: $parsh
"""
class DoubleNode:
    def __init__(self, value=None):
        self.value = value
        self.radd = None
        self.ladd = None
                
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value) :
        if self.head is None:
            new_node = DoubleNode(value)
            self.head = new_node
            return
        else :
            new_node = DoubleNode(value)
            cur_node = self.head
            while cur_node.radd :
                cur_node = cur_node.radd
            cur_node.radd = new_node
            new_node.ladd = cur_node
            new_node.radd = None
            
            
    def prepend(self,value) :
        if self.head is None:
            new_node = DoubleNode(value)
            self.head = new_node
            return
        else :
            new_node = DoubleNode(value)
            cur_node = self.head
            cur_node.ladd = new_node
            new_node.radd = cur_node
            self.head = new_node
            new_node.ladd = None
            
                
                
            
            
            
            
            
    def display(self):
            elems = []
            cur_node = self.head
            while cur_node :
                elems.append(cur_node.value)
                cur_node = cur_node.radd
            print(elems)
     
   
        
        
mylist = DoublyLinkedList()

mylist.prepend(1)
mylist.prepend(2)
mylist.prepend(3)
mylist.append(4)
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)


print(mylist)
mylist.display()

