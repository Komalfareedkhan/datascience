# from turtle import color
# from matplotlib import style
from matplotlib.font_manager import _Weight
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(style="ticks",color_codes=True)
titanic=sns.load_dataset("titanic")
plt.figure(figsize=(10,8))
sns.boxplot(x="sex",y="age",data=titanic,showmeans=True,meanprops={"marker":"^","markersize":"10","markeredgecolor":"red"})
plt.title("Sex vs Age",size=30,)
plt.xlabel("Type of sex",size=20)
plt.ylabel("People age",size=20)
plt.show()