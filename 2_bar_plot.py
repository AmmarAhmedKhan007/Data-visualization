import seaborn as sns                          
import matplotlib.pyplot as plt

khashti = sns.load_dataset("titanic")            
print (khashti)

sns.barplot (x='who', y='alone',hue='sex' ,data=khashti,ci=None)        #ci=None  for remove line on upper 
                                                                      #order=["female","male"] to change order
                                                                      #color= "red" to change color
plt.title (" BAR GRAPH ")                       

plt.show()






