
# SCRIPTS COPIED FROM ( EXAMPLE GALLERY OF SEABORN)



import seaborn as sns
import pandas as pf
import numpy as np
import matplotlib.pyplot as plt
nk = sns.load_dataset('dots')
print (nk)

sns.relplot(x='time',y='firing_rate',hue='coherence' ,kind='line' ,data=nk)
plt.show()




# SCATTER PLOT :

import seaborn as sns
import pandas as pf
import numpy as np
import matplotlib.pyplot as plt
nk = sns.load_dataset('diamonds')
print (nk)
# clarity_ranking = ('SI2','SI1','VS1','VS2',)
sns.scatterplot(x='carat',y='price',hue='clarity',data=nk)
plt.show()


# BOX PLOT & STRIP PLOT


import seaborn as sns
import pandas as pf
import numpy as np
import matplotlib.pyplot as plt
nk = sns.load_dataset('diamonds')
print (nk)
#clarity_ranking = ('SI2','SI1','VS1','VS2',)
sns.boxplot(x='carat',y='price',hue='clarity',data=nk)
# sns.stripplot(x='carat',y='price',hue='clarity',data=nk)
# plt.show()
plt.show()



# Scatterplot with multiple semantics

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

# Load the example diamonds dataset
diamonds = sns.load_dataset("diamonds")
print (diamonds)

# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
sns.scatterplot(x="carat", y="price",
                hue="clarity", size="depth",
                palette="ch:r=-.2,d=.3_r",
                hue_order=clarity_ranking,
                sizes=(1, 8), linewidth=0,
                data=diamonds, ax=ax)

plt.show()