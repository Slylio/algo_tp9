#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class EmptyQueueError(Error):
    """Exception raised when trying to dequeue from an empty queue."""
    
    def __init__(self, expression, message):
        """Creates an instance of class EmptyQueueError
        input   -- self : instance of class EmptyQueueError
                -- expression : expression in which the error occurred
                -- message : explanation of the error
        """
        self.expression = expression
        self.message = message

class Cell():
    """The class Cell allows to represent a list from chained elements of type Cell. Each element of the 
    list contains a value and a pointer towards the next element."""
    
    def __init__(self):
        """ Creates an instance of class Cell
        input   -- self : instance of class Cell
        """
        self.value = object
        self.next = None
    
    def __str__(self):
        """ Returns a string representing Cell self
        input   -- self : instance of class Cell
        output  -- string
        """
        result = str(self.value) + ', next:'
        if self.next == None:
            result += 'None'
        else:
            result += str(self.next.value)
        return '{ ' + result + ' }'
    
class QueueList:
    """The class QueueList allows to represent a queue implemented by a linked list."""

    def __init__(self):
        """  Creates an instance of class QueueList
         input    -- self
         output   -- self is an empty queue
        """
        self.mfront = None   # front cell
        self.mback = None    # back cell 
        self.size = 0
  
    def size_queue(self):
        """ Returns the size of the QueueList self
        input   -- self : instance of class QueueList
        output  -- int, the number of elements in the queue
        """
        return self.size
    
    def __str__(self):
        """ Returns a string representing the QueueList self
        input   -- self : instance of class QueueList
        output  -- string
        """
        result = '['
        if not(self.empty_queue()):
            elt = self.mfront
            while elt.next != None:
                result = result + str(elt.value) + ','
                elt = elt.next
            result = result + str(elt.value)   
        return result + ']'     

    def empty_queue(self):
        """ Returns True if the QueueList self is empty and False otherwise
        input   -- self : instance of class QueueList
        output  -- bool
        """
        if self.size>0: return True
        return False

    def enqueue(self, v):
        """ adds and element of value v at the end of QueueList
        The queue is modified by adding the Cell of value v at the end of the queue
        input    -- self: instance of class QueueList
                 -- v : object, value of the Cell
                    pre-cond: self is not full (not tested here)
        output   -- self which has been modified
                 the size of the queue is incremented
        """
        cellToInsert=Cell()
        cellToInsert.value=v

        if self.mfront==None:
            self.mfront=cellToInsert
            self.mback=cellToInsert
        else : 
            self.mback.next=cellToInsert
            self.mback=cellToInsert
        self.size+=1
        return self
        

    def front_value(self):
        """ Returns the value of the element at the front of the queue self
        input   -- self : instance of class QueueList
        output  -- v: value of the Cell element 
        """
        return self.front.value

    def front(self):
        """ Returns the element at the front of the queue self
        input   -- self : instance of class QueueList
        output  -- v: the Cell element 
        """
        if self.mfront!=None:
            return self.mfront
        return None

        
    def back_value(self):
        """ Returns the value of the element at the end of the queue self
        input   -- self : instance of class QueueList
        output  -- v: value of the Cell element 
        """
        if self.mback!=None:
            return self.mback.value
        return None

    def dequeue(self):          
        """ takes off the element at the front of the QueueList self
        input    -- self : instance of class QueueList
                    pre-cond: self is not empty
        output   -- self in which the element at the front of the queue has been taken off
                  post-cond: the size of the queue is decremented
        """
        if self.size==0:
            return self
        elif self.size==1:
            self.mback=None
            self.mfront=None
        else:
            c1= self.mfront
            c2= c1.next
            c1.next= None
            self.mfront=c2
        self.size-=1
        return self

if __name__ == "__main__":
    print("Hello QueueList !")

