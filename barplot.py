from turtle import color
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# sns.set_style("ticks",color_codes=True)
# titanic=sns.load_dataset("titanic")
# sns.boxplot(x="sex",y="age",data=titanic,showmeans=True)
# #plt.set_title("plot for counting")
# plt.show()
import plotly.express as px
tips = px.data.tips()
#tips
plt=px.scatter(tips, x="total_bill", y="tip", color="smoker")
plt.show()