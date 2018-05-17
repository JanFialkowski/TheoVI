import matplotlib.pyplot as plt
import numpy as np

r1=np.linspace(0,3,1000).tolist()
r2=np.linspace(3,3.5,2500).tolist()
r3 = np.linspace(3.5,3.75,5000).tolist()
r4 = np.linspace(3.75,4.0,10000).tolist()
r1.extend(r2)
r1.extend(r3)
r1.extend(r4)
r = r1
#print r
r = np.array(r)
x0 = 0.5
X = np.array([x0 for i in xrange(len(r))])
print X

def logistic(x):
    return r*x*(1-x)

t=0
while 10000 > t:
    X = logistic(X)
    t+=1
    print "prepping:" ,t/100.
t=0
while 1000 > t:
    plt.scatter(r,X,s=1, marker=".", color = "xkcd:black")
    X = logistic(X)
    print "Doing:" ,(t)/10.
    t+=1
plt.show()
