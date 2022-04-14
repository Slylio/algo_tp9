from http import client
from random import random
from random import uniform
import numpy as np
import matplotlib.pyplot as plt
import queue_list
class SimulFileAttente():
    def __init__(self):

        self.currentTime=0
        #on ne peut pas dépasser 8h soit 8*60*60 secondes
        self.tMax= 8*60*60
        #limites minimales
        self.serviceMin= 30
        self.serviceMax= 300
        #queue
        self.queue= queue_list.QueueList()
    
    class Client():
        def __init__(self,t,waitMin,waitMax) -> None:
            self.t= t
            waitMin,waitMax=30,80
            self.leaveTime=t+uniform(waitMin, waitMax)
    
    def simul(self,p):
        totalOfClients=0
        clientsServed=0
        serviceTimeCounter=0

        for _ in range (self.tMax):
            #boolean servant a savoir si on est occupé
            bool=False
            if serviceTimeCounter!=0:
                bool=True
                serviceTimeCounter-=1
            if bool==False:
                if not self.queue.empty_queue():
                    self.queue.dequeue()
                    serviceTimeCounter=int(uniform(self.serviceMax,self.serviceMin))
                    clientsServed+=1
            #ajout client
            if random()<p:
                self.queue.enqueue(self.Client(self.currentTime))
                totalOfClients+=1
        return clientsServed/totalOfClients

    def simul_bis(self,p):
        totalOfClients=0
        clientsNotServed=0
        serviceTimeCounter=0

        for time in range (self.tMax):
            bool=False
            if serviceTimeCounter!=0:
                bool=True
                serviceTimeCounter-=1
            if bool==False:
                if time>self.queue.mfront.value.leaveTime or self.queue.empty_queue():
                    clientsNotServed+=1
                    self.queue.dequeue()
                if not self.queue.empty_queue():
                    self.queue.dequeue()
                    serviceTimeCounter=int(uniform(self.serviceMax,self.serviceMin))
            #ajout client
            if random()<p:
                self.queue.enqueue(self.Client(self.currentTime,120,1800))
                totalOfClients+=1
        #les clients restants a la fin des 8h ne sont pas servis 
        clientsNotServed+=self.queue.size
        return clientsNotServed/totalOfClients

    def simul_ter(self,p):
        totalOfClients=0
        clientsNotServed=0
        serviceTimeCounter=0

        for time in range (self.tMax):
            bool=False
            if serviceTimeCounter!=0:
                bool=True
                serviceTimeCounter-=1
            for _ in range(self.queue.size):
                elt=self.queue.mfront.value
                self.queue.dequeue()
                if time>elt.leaveTime:
                    self.queue.enqueue(elt)
                else :
                    clientsNotServed+=1
            if bool==False:
                if not self.queue.empty_queue():
                    self.queue.dequeue()
                    serviceTimeCounter=int(uniform(self.serviceMax,self.serviceMin))
            if random()<p:
                self.queue.enqueue(self.Client(self.currentTime,120,1800))
                totalOfClients+=1
        clientsNotServed+=self.queue.size
        return clientsNotServed/totalOfClients
    
    def main(self):
        x=[]    #création des points en abcsisse
        y=[]    #en ordonnées
        i=0.00025
        count=1
        while i<=0.025:
            print (str(count)+" clients non servis/total= "+str(self.simul_ter(i)))
            x.append(i)
            y.append(self.simul_ter(i))
            i+=0.0025
            count+=1


        plt.plot(x,y)
        plt.show()
