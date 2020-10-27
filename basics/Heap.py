# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 18:23:47 2020
@author: Saawan
"""

class Heap(object):
    Heap_size=10
    def __init__(self):
        self.heap=[0]*Heap_size
        self.currentPostition=-1
        #   "editor.codeActionsOnSave": null,
    def insert(self,item)
        if self.isFull():
            print("heap is full")
            return 
        self.currentPostition=self.currentPostition+1
        self.heap[currentPosition]=item
        self.fixUp(self.currentPosition)

    def fixUp(self,index):
        parentIndex=int((index-1)/2)
        while parentIndex>=0 and self.heap[parentIndex]<self.heap[index]:
            temp=self.heap[index]
            self.heap[index]=self.heap[parentIndex]
            self.heap[parentIndex]=temp
            parentIndex=(int)((index-1)/2)

    def isFull(self):
        if self.currentPostition==Heap_size:
            return True
        else:
            return False