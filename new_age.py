#data visualization
# step.1(import libraries)
import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#step.2 (set the theme)

# step.3(Data set loading) we can also import our own data
cancer=pd.read_csv("cancer_b.csv")
print(cancer)
# import seaborn as sns
# import matplotlib.pyplot as plt
#sns.set_theme(style="ticks",color_codes=True)
# step.4(Plot basic graph)(plot with only one variable x)
# p=sns.countplot(x="sex",data=boat)
# plt.show()

#plot with 2 variables
# p=sns.countplot(x="sex",hue= "class",data=boat)
# p.set_title("PLOT FOR COUNTING")
# plt.show()


