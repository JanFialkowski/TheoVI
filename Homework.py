# coding: utf-8
import matplotlib.pyplot as plt
import numpy as np
omega = np.pi
tau = 1
dt = 0.01
K = 0
Lambda = 0.5
def fnocontrol(x):
    return [Lambda*x[0]+omega*x[1],-omega*x[0]+Lambda*x[1]]
length = tau/dt
Valuepairs = [[[]for i in xrange(2)] for j in xrange(4)]
x0 = 0.25
y0 = 0.0
for Pair in Valuepairs:
    Pair[0] = x0
    Pair[1] = y0
    
for Pair in Valuepairs:
    Pair[0].append(x0)
    Pair[1].append(y0)
    
while len(Valuepairs[0][0])!=length:
    for Pair in Valuepairs:
        Input = [Pair[0][-1],Pair[1][-1]]
        Output = fnocontrol(Input)
        Pair[0].append(Output[0])
        Pair[1].append(Output[1])
        
dt = 0.001
length = tau/dt
Valuepairs = [[[]for i in xrange(2)] for j in xrange(4)]
for Pair in Valuepairs:
    Pair[0].append(x0)
    Pair[1].append(y0)
    
while len(Valuepairs[0][0])!=length:
    for Pair in Valuepairs:
        Input = [Pair[0][-1],Pair[1][-1]]
        Output = fnocontrol(Input)
        Pair[0].append(Output[0]*dt+Input[0])
        Pair[1].append(Output[1]*dt+Input[1])
        
def f(x,xt):
    btw = fnocontrol(x)
    return[x[0]+dt*(btw[0]+K*(xt[0]-x[0])),x[1]+dt*(btw[1]+K*(xt[1]-x[1]))]
    
while len(Valuepairs[0][0])!=length+20000:
    for Pair in Valuepairs:
        if Valuepairs.index(Pair)==0:
            K=0
        else:
            K=0.15+0.05*Valuepairs.index(Pair)
        Input1 = [Pair[0][-1],Pair[1][-1]]
        Input2 = [Pair[0][int(-length)],Pair[1][int(-length)]]
        Output = f(Input1,Input2)
        Pair[0].append(Output[0])
        Pair[1].append(Output[1])
        
for pair in Valuepairs:
    plt.plot(pair[0],pair[1])
    
plt.show()
