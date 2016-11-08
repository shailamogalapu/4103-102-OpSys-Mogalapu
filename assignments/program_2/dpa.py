import threading
import os
from time import sleep 
from os import system
import curses
import locale
import time
import threading
import random
import json
import struct

    
        

"""=========================================================="""

# Layout of the table (P = philosopher, f = fork):
#          P0
#       f3    f0
#     P3        P1
#       f2    f1
#          P2

# Number of philosophers at the table. 
# There'll be the same number of forks.
numPhilosophers = 4

# Lists to hold the philosophers and the forks.
# Philosophers are threads while forks are locks.
philosophers = []
forks = []

screenLock = threading.Lock()

class Philosopher(threading.Thread):
    def __init__(self, index,wait):
        threading.Thread.__init__(self)
        self.index = index
        self.wait=wait
        

    def run(self):
        # Assign left and right fork
        leftForkIndex = self.index
        rightForkIndex = (self.index - 1) % numPhilosophers
        forkPair = ForkPair(leftForkIndex, rightForkIndex)
        
     
        # Eat forever
        while True:
            with self.wait:
               forkPair.pickUp()
	       print("Philosopher",self.index,"is eating.")
	       time.sleep(0.1)
               forkPair.putDown()
                

class ForkPair:
    def __init__(self, leftForkIndex, rightForkIndex):
        # Order forks by index to prevent deadlock
        if leftForkIndex > rightForkIndex:
            leftForkIndex, rightForkIndex = rightForkIndex, leftForkIndex
        self.firstFork = forks[leftForkIndex]
        self.secondFork = forks[rightForkIndex]
    

    def pickUp(self):
        # Acquire by starting with the lower index
        self.firstFork.acquire()
        self.secondFork.acquire()

    def putDown(self):
        # The order does not matter here
        self.firstFork.release()
        self.secondFork.release()

if __name__ == "__main__":

    wait=threading.Semaphore(2)
    
    # Create philosophers and forks
    for i in range(0, numPhilosophers):
        philosophers.append(Philosopher(i,wait))
        forks.append(threading.Lock())
       

    # All philosophers start eating
    for philosopher in philosophers:
        philosopher.start()

    # Allow CTRL + C to exit the program
    try:
        while True: sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        os._exit(0)
