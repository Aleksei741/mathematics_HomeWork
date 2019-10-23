import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt




def equations(p):
    x,y = p
    return y - x**2 + 1, np.exp(x) + x * (1 - y) - 1

x1 , y1 = fsolve(equations , (-2,3))
x2 , y2 = fsolve(equations , (3,10))
x3 , y3 = fsolve(equations , (4,15))

print(x1, y1)
print(x2, y2)
print(x3, y3)


x = np.linspace(-2, 4.5, 100)
x_res = list()
y = list()
for i in x:
    y_ = i ** 2 - 1
    if(np.exp(i) + i -1)/i > y_:
        x_res.append(i)
        y.append(i ** 2 - 1)

plt.plot(x_res, y)
plt.xlabel('х')  # наименование оси абсцисс
plt.ylabel('у')  # наименование оси ординат

plt.show()