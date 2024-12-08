from scipy.stats import levene
import pandas as pd 

iris = pd.read_csv('../tables/iris.csv')


w_stats, p_value = levene(iris.query('Species == "virginica"')['Sepal.Length'], iris.query('Species == "versicolor"')['Sepal.Length'])

print(w_stats, p_value)