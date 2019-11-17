import pandas as pd
from matplotlib import pyplot as plt


data = pd.read_csv('train.csv' , encoding = "ISO-8859-1")



print('rand sampling \n\n')
print(data.sample(20))

labels = data['Sentiment'].sample(30)
print(labels)

labels.plot()
plt.xlabel("interestinglabvel")
plt.ylabel("anotherinterestinglabeñ")
plt.show()
