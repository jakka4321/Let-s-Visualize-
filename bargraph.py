import matplotlib.pyplot as plt
import numpy as np
data={'test1':82, 'test2':78 ,'test3':68, 'test4':93, 'test5':77}
tests=list(data.keys())
marks=list(data.values())
plt.bar(tests,marks,color='blue',width=0.5,alpha=0.5)
plt.xlabel("Cycle tests")
plt.ylabel("Marks")
plt.title("Cycle tests marks 2020")
plt.show()