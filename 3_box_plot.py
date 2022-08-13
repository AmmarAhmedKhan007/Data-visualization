import seaborn as sns
import matplotlib.pyplot as plt
# seaborn.set_style('whitegrid')                      

tipe= sns.load_dataset('tips')
print(tipe)

sns.boxplot(x='day',y='tip',data=tipe)
plt.show()



# Practice:

import seaborn as sns
import pandas as pf
import numpy as np
import matplotlib.pyplot as plt                      

tipe= sns.load_dataset('tips')
# print (tipe.describe())
print(tipe)
sns.boxplot(x='tip',y='day',hue='smoker', color='red',data=tipe)
# sns.boxplot(x='day',y='tip',data=tipe)
plt.show()




import seaborn as sns
import pandas as pf
import numpy as np
import matplotlib.pyplot as plt

khashti = sns.load_dataset('titanic')
# print (khashti.head(5))
# print (khashti.describe())
print (khashti)
sns.boxplot(x='survived',y='age',showmeans =True, 
            meanprops={"marker":"+","markersize":"20","markeredgecolor":"red"}, 
            data=khashti)
plt.xlabel("How many Survived")                                   # Adding lables
plt.ylabel("AGE (years)")
plt.title("KITNAY DOOBAY KITNY BACHY ",size=20, weight="bold")          #change size & weight
plt.show()