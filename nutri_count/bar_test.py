
# libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
x = display()
y = (10460, 65, 22, 275, 50, 62, 6) #kJ und der Rest Gramm, 19-25 Jahre alter Mann

# Create a color if the y axis value is equal or greater than 0
my_color = np.where(y >= 0, 'orange', 'skyblue')

# The vertical plot is made using the vline function
plt.vlines(x=x, ymin=0, ymax=y, color=my_color, alpha=0.4)
plt.scatter(x, y, color=my_color, s=1, alpha=1)

# Add title and axis names
plt.title("Evolution of the value of ...", loc='left')
plt.xlabel('Value of the variable')
plt.ylabel('Group')

# Show the graph
plt.show()