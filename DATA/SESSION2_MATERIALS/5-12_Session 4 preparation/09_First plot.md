# First plot

Type: Exercise

Run the code below to verify that you have all the necessary libraries installed and configured correctly.

``` python
%matplotlib ipympl

import matplotlib.pyplot as plt

x = [0,1,2,3,4,5]
y1 = [0,1,2,3,4,5]
y2 = [0,1,4,9,16,25]

plt.plot(x, y1, label='Plot 1')
plt.plot(x, y2, label='Plot 2')  
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
```
