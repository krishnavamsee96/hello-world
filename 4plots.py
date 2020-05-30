# Krishna Vamsee Duggaraju
# 800688160

from matplotlib.pyplot import *
from numpy import *
from copy import *

t = arange(0,1,0.01)
y = 2.0*sin(2*pi*t)
y3 = copy(y)
y4 = copy(y)

#enumerate:
N = len(y)
y1 = zeros(N)
for i, y_i in enumerate(y):
    if y_i < 0.5:
        y1[i] = 0
    else:
        y1[i] = y_i
figure(1)
clf()
plot(t, y, 'r--')
plot(t, y1, label = 'Enumerate')
legend(loc=1)

#cryptic:
y2 = copy(y)
figure(2)
y2[y2 < 0.5] = 0
clf()
plot(t, y, 'r--')
plot(t, y2, label = 'cryptic')
legend(loc=1)

#where:
inds = where(y < 0.5)[0]
y3[inds] = 0
figure(3)
plot(t, y, 'r--')
plot(t, y3, label = 'where')
legend(loc=1)

#forloop:
N = len(y)
y4 = zeros(N)
for i in range(N):
    y_i = y[i]
    if y_i < 0.5 :
        y4[i] = 0
    else: 
        y4[i] = y_i
figure(4)
plot(t, y, 'r--')
plot(t, y4, label = 'forloop')
legend(loc=1)

show()
