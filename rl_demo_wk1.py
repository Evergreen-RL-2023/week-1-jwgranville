'''
Joe Granville
Advanced Computing and Machine Learning
Machine Learning
2023/04/13
Machine Learning Workshop #1

computing averages and 1-armed bandit

3 ways to compute averages
The third method uses temporal difference
see Sutton and Barto
Q = Q + a*(R - Q), where in this case Q is the average
and R is the new value to be averaged

also use rand.gauss(0, 1) instead of i

'''

import random as rand

N = 4

seed = rand.random()

def average1():
    sum = 0
    for i in range(1, N):
        sum += i
    avg = sum / (N-1)
    print('avg1', avg)

def average2():
    avg = 0
    for i in range(1, N):
        avg = avg * (i-1)/i + 1
    print('avg2', avg)

def average3():
    avg = 0
    for i in range(1, N):
        avg = avg + ( i - avg ) / i
    print('avg3', avg)

def average1r( seed = None ):
    if ( seed != None ):
        rand.seed( seed )
    sum = 0
    for i in range(1, N):
        sum += rand.gauss(0, 1)
    avg = sum / (N-1)
    print('avg1r', avg)

def average2r( seed = None ):
    if ( seed != None ):
        rand.seed( seed )
    avg = 0
    for i in range(1, N):
        avg = avg * (i-1)/i + rand.gauss(0, 1) / i
    print('avg2r', avg)

def average3r( seed = None ):
    if ( seed != None ):
        rand.seed( seed )
    avg = 0
    for i in range(1, N):
        avg = avg + ( rand.gauss(0, 1) - avg ) / i
    print('avg3r', avg)

if __name__ == '__main__':
    average1()
    average2()
    average3()
    average1r(seed)
    average2r(seed)
    average3r(seed)

