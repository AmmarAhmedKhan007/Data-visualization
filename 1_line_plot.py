#Syntax:

# Import libraries
# Load datasets
# Draw a line plot 
# set title 
#Adding limits 
#Set style 

import seaborn as sns                          #IMPORT LIRARIES
import matplotlib.pyplot as plt

phool = sns.load_dataset("titanic")            #LOAD DATASET
# plt.figure(figsize=(8, 6))                     #FIGURE SIZE
print (phool)

sns.lineplot (x='survived', y='age', data=phool)        #LINEPLOT
plt.title (" LINEPLOT ")                       #SET TITLE

sns.set_style('dark')                          #SET STYLE
sns.set_style(style=None, rc=None)
# plt.xlim()                                   #SET LIMITS
# plt.ylim()
plt.show()