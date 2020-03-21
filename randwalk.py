# random walk
import time
from math import modf
import random
from matplotlib import pyplot as cg

# Global varibales
initial = [5,5]
direction = {0:[-1,0],
             1:[0,1],
             2:[1,0],
             3:[0,-1],
             4:[-1,1],
             5:[1,1],
             6:[1,-1],
             7:[-1,-1]}
steps = int()
des = [[5,5]]

def randomGen(lt):
    timestamp = modf(time.time())
    time.sleep(1);
    ranFactor2 = int(timestamp[1])
    ranFactor = ranFactor2 + random.randint(1,10)
    return int(ranFactor % int(lt))

def move():
    path = direction[randomGen(8)]
    for i in range(2):
        initial[i] = initial[i] + path[i]
    print(initial)
    
    print("final "+str(des))




def main():
    steps = int(input("Enter number of steps: "))
    print("Sit back and relax......")
    print("Moving starts")
    print(initial)
    for i in range(steps):
        move();
    print("Moving ends for "+str(steps)+" steps")
    print(des)
    # cg.plot()
    # cg.show()


main()
