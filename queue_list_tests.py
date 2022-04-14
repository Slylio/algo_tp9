#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue_list as ql

#%% Test des méthode enqueue et __str__
q1 = ql.QueueList()
print("q1:",q1)
for i in range(1,6):
    q1.enqueue(i)
    print("q1:",q1)

#%% Test des méthodes empty_queue et size_queue
q1 = ql.QueueList()
print("q1:", q1,'- Empty:',q1.empty_queue(), "- Size : ", q1.size_queue())
for i in range(1,6):
    q1.enqueue(i)
print("q1:", q1,'- Empty:',q1.empty_queue(), "- Size : ", q1.size_queue())

#%% Test des méthodes front_value et back_value
q1 = ql.QueueList()
for i in range(1,6):
    q1.enqueue(i)
print("q1:",q1,'- Empty:',q1.empty_queue(), "- Size : ", q1.size_queue())
print("front_value : ", q1.front_value())
print("back_value : ", q1.back_value())

#%% Test des méthodes dequeue, front_value et back_value
q1 = ql.QueueList()
for i in range(1,6):
    q1.enqueue(i)
for cpt in range(5):
    q1.dequeue()
    print("q1:",q1,'- Empty:',q1.empty_queue(), "- Size : ", q1.size_queue())
    print("front_value : ", q1.front_value())
    print("back_value : ", q1.back_value())
