import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()

iris_df =  pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
# print(iris_df.head())

# iris_df.info()
# print(iris_df.describe())
sns.pairplot(iris_df, hue = 'label')
plt.show()
